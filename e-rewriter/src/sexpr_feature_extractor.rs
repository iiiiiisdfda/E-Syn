// S-expression 格式電路特徵提取器
// 從 S-expression 字符串中提取適合用於機器學習訓練的特徵

use std::collections::{HashMap, HashSet};

#[derive(Debug, Clone)]
enum SExprNode {
    Leaf(String),
    Node {
        operator: String,
        children: Vec<SExprNode>,
    },
}

impl SExprNode {
    fn is_leaf(&self) -> bool {
        matches!(self, SExprNode::Leaf(_))
    }
    
    fn operator(&self) -> Option<&str> {
        match self {
            SExprNode::Node { operator, .. } => Some(operator),
            _ => None,
        }
    }
    
    fn children(&self) -> &[SExprNode] {
        match self {
            SExprNode::Node { children, .. } => children,
            _ => &[],
        }
    }
}

pub struct SExprFeatureExtractor {
    root: Option<SExprNode>,
    variables: HashSet<String>,
    node_dependencies: HashMap<String, HashSet<String>>,
    fanout: HashMap<String, usize>,
    all_nodes: Vec<SExprNode>,
}

impl SExprFeatureExtractor {
    pub fn new() -> Self {
        SExprFeatureExtractor {
            root: None,
            variables: HashSet::new(),
            node_dependencies: HashMap::new(),
            fanout: HashMap::new(),
            all_nodes: Vec::new(),
        }
    }

    pub fn parse_sexpr(&mut self, sexpr_str: &str) -> Result<(), String> {
        let sexpr_str = sexpr_str.trim();
        let mut pos = 0;
        
        self.root = Some(self.parse_expr(sexpr_str, &mut pos)?);
        self.build_dependencies();
        
        Ok(())
    }

    fn parse_expr(&mut self, sexpr_str: &str, pos: &mut usize) -> Result<SExprNode, String> {
        self.skip_whitespace(sexpr_str, pos);
        
        if *pos >= sexpr_str.len() {
            return Err("Unexpected end of input".to_string());
        }
        
        // 如果是葉節點（變數）
        if sexpr_str.chars().nth(*pos) != Some('(') {
            let var_name = self.parse_atom(sexpr_str, pos);
            if !var_name.is_empty() {
                self.variables.insert(var_name.clone());
                return Ok(SExprNode::Leaf(var_name));
            }
            return Err("Empty atom".to_string());
        }
        
        // 移除外層左括號
        *pos += 1;
        self.skip_whitespace(sexpr_str, pos);
        
        // 解析運算符（第一個 token）
        let operator = self.parse_atom(sexpr_str, pos);
        if operator.is_empty() {
            return Err("Missing operator".to_string());
        }
        
        self.skip_whitespace(sexpr_str, pos);
        
        // 解析子表達式
        let mut children = Vec::new();
        while *pos < sexpr_str.len() {
            let ch = sexpr_str.chars().nth(*pos);
            if ch == Some(')') {
                break;
            }
            
            match self.parse_expr(sexpr_str, pos) {
                Ok(child) => children.push(child),
                Err(e) => {
                    if e == "Unexpected end of input" {
                        break;
                    }
                    return Err(e);
                }
            }
            self.skip_whitespace(sexpr_str, pos);
        }
        
        // 跳過右括號
        if *pos < sexpr_str.len() && sexpr_str.chars().nth(*pos) == Some(')') {
            *pos += 1;
        }
        
        Ok(SExprNode::Node {
            operator,
            children,
        })
    }

    fn parse_atom(&self, sexpr_str: &str, pos: &mut usize) -> String {
        let start = *pos;
        while *pos < sexpr_str.len() {
            let ch = sexpr_str.chars().nth(*pos).unwrap();
            if ch.is_whitespace() || ch == '(' || ch == ')' {
                break;
            }
            *pos += 1;
        }
        sexpr_str[start..*pos].to_string()
    }

    fn skip_whitespace(&self, sexpr_str: &str, pos: &mut usize) {
        while *pos < sexpr_str.len() {
            let ch = sexpr_str.chars().nth(*pos).unwrap();
            if !ch.is_whitespace() {
                break;
            }
            *pos += 1;
        }
    }

    fn build_dependencies(&mut self) {
        self.node_dependencies.clear();
        self.fanout.clear();
        self.all_nodes.clear();
        
        let mut node_counter = 0;
        
        if let Some(ref root) = self.root {
            Self::traverse_static(
                root,
                None,
                &mut node_counter,
                &mut self.node_dependencies,
                &mut self.fanout,
                &mut self.all_nodes,
            );
        }
    }

    fn traverse_static(
        node: &SExprNode,
        parent_id: Option<String>,
        node_counter: &mut usize,
        node_dependencies: &mut HashMap<String, HashSet<String>>,
        fanout: &mut HashMap<String, usize>,
        all_nodes: &mut Vec<SExprNode>,
    ) {
        if node.is_leaf() {
            // 葉節點是變數（parent_id 只用於葉節點）
            if let SExprNode::Leaf(var_name) = node {
                if let Some(ref pid) = parent_id {
                    node_dependencies
                        .entry(pid.clone())
                        .or_insert_with(HashSet::new)
                        .insert(var_name.clone());
                    *fanout.entry(var_name.clone()).or_insert(0) += 1;
                }
            }
            return;
        }
        
        // 為內部節點生成唯一 ID（總是生成新 ID，與 Python 版本一致）
        // 注意：parent_id 參數在非葉節點時不使用，總是生成新的 node_id
        let node_id = format!("node_{}", *node_counter);
        *node_counter += 1;
        all_nodes.push(node.clone());
        
        // 記錄依賴關係
        for child in node.children() {
            if child.is_leaf() {
                if let SExprNode::Leaf(var_name) = child {
                    node_dependencies
                        .entry(node_id.clone())
                        .or_insert_with(HashSet::new)
                        .insert(var_name.clone());
                    *fanout.entry(var_name.clone()).or_insert(0) += 1;
                }
            } else {
                // 為子節點生成 ID 並記錄依賴（在遞歸調用之前生成 ID，但計數器還未遞增）
                // 這與 Python 版本一致：child_id = f"node_{node_counter[0]}"（此時 node_counter[0] 還未遞增）
                // 然後在 traverse 內部會生成新的 node_id 並遞增計數器
                let child_id = format!("node_{}", *node_counter);
                node_dependencies
                    .entry(node_id.clone())
                    .or_insert_with(HashSet::new)
                    .insert(child_id.clone());
                // 遞歸處理子節點，傳入預分配的 child_id（但這個 child_id 在 traverse_static 內部不會被使用）
                // 實際上，traverse_static 內部總是生成新的 node_id，所以 child_id 只是用於建立依賴關係
                Self::traverse_static(
                    child,
                    Some(child_id),
                    node_counter,
                    node_dependencies,
                    fanout,
                    all_nodes,
                );
            }
        }
    }

    fn collect_all_nodes(&self, node: &SExprNode) -> Vec<SExprNode> {
        let mut nodes = Vec::new();
        if !node.is_leaf() {
            nodes.push(node.clone());
            for child in node.children() {
                nodes.extend(self.collect_all_nodes(child));
            }
        }
        nodes
    }

    fn calculate_logic_depth(&self, node: &SExprNode) -> usize {
        // 如果是葉節點（輸入變數），深度為 0
        if node.is_leaf() {
            return 0;
        }
        
        // 計算所有子節點的最大深度
        let mut max_child_depth = 0;
        for child in node.children() {
            let child_depth = self.calculate_logic_depth(child);
            max_child_depth = max_child_depth.max(child_depth);
        }
        
        // 當前節點的深度 = 1 + 最大子節點深度
        1 + max_child_depth
    }

    pub fn extract_structural_features(&self) -> HashMap<String, f64> {
        let mut features = HashMap::new();
        
        let all_nodes_list = if let Some(ref root) = self.root {
            self.collect_all_nodes(root)
        } else {
            Vec::new()
        };
        
        features.insert("num_internal_nodes".to_string(), all_nodes_list.len() as f64);
        
        // 計算邏輯深度（從根節點到葉節點的最長路徑）
        let max_logic_depth = if let Some(ref root) = self.root {
            self.calculate_logic_depth(root)
        } else {
            0
        };
        features.insert("max_logic_depth".to_string(), max_logic_depth as f64);
        
        // 計算平均邏輯深度（對於多輸出情況，這裡使用根節點的深度）
        // 注意：S-expression 通常是單一表達式，所以平均深度等於最大深度
        features.insert("avg_logic_depth".to_string(), max_logic_depth as f64);
        
        // 計算扇入扇出
        let fanin_counts: Vec<usize> = self.node_dependencies
            .values()
            .map(|deps| deps.len())
            .collect();
        
        if !fanin_counts.is_empty() {
            let sum: usize = fanin_counts.iter().sum();
            features.insert("avg_fanin".to_string(), sum as f64 / fanin_counts.len() as f64);
            features.insert("max_fanin".to_string(), *fanin_counts.iter().max().unwrap() as f64);
        } else {
            features.insert("avg_fanin".to_string(), 0.0);
            features.insert("max_fanin".to_string(), 0.0);
        }
        
        if !self.fanout.is_empty() {
            let sum: usize = self.fanout.values().sum();
            features.insert("avg_fanout".to_string(), sum as f64 / self.fanout.len() as f64);
            features.insert("max_fanout".to_string(), *self.fanout.values().max().unwrap() as f64);
        } else {
            features.insert("avg_fanout".to_string(), 0.0);
            features.insert("max_fanout".to_string(), 0.0);
        }
        
        features
    }

    fn count_operators(&self, node: &SExprNode) -> HashMap<String, usize> {
        let mut counts: HashMap<String, usize> = [
            ("&".to_string(), 0),
            ("+".to_string(), 0),
            ("*".to_string(), 0),
            ("!".to_string(), 0),
            ("^".to_string(), 0),
        ]
        .iter()
        .cloned()
        .collect();
        
        fn traverse(n: &SExprNode, counts: &mut HashMap<String, usize>) {
            if !n.is_leaf() {
                if let Some(op) = n.operator() {
                    *counts.entry(op.to_string()).or_insert(0) += 1;
                }
                for child in n.children() {
                    traverse(child, counts);
                }
            }
        }
        
        if let Some(ref root) = self.root {
            traverse(root, &mut counts);
        }
        
        counts
    }

    fn calculate_max_nesting(&self, node: &SExprNode, current_depth: usize) -> usize {
        if node.is_leaf() {
            return current_depth;
        }
        
        let mut max_depth = current_depth;
        for child in node.children() {
            let child_depth = self.calculate_max_nesting(child, current_depth + 1);
            max_depth = max_depth.max(child_depth);
        }
        
        max_depth
    }

    pub fn extract_syntactic_features(&self) -> HashMap<String, f64> {
        let mut features = HashMap::new();
        
        let op_counts = self.count_operators(self.root.as_ref().unwrap());
        let count_and = op_counts.get("&").unwrap_or(&0) + op_counts.get("*").unwrap_or(&0);
        let count_or = *op_counts.get("+").unwrap_or(&0);
        let count_xor = *op_counts.get("^").unwrap_or(&0);
        let count_not = *op_counts.get("!").unwrap_or(&0);
        let total_operators = count_and + count_or + count_xor + count_not;
        
        features.insert("count_and".to_string(), count_and as f64);
        features.insert("count_or".to_string(), count_or as f64);
        features.insert("count_xor".to_string(), count_xor as f64);
        features.insert("count_not".to_string(), count_not as f64);
        features.insert("total_operators".to_string(), total_operators as f64);
        
        if total_operators > 0 {
            features.insert("ratio_and".to_string(), count_and as f64 / total_operators as f64);
            features.insert("ratio_or".to_string(), count_or as f64 / total_operators as f64);
            features.insert("ratio_xor".to_string(), count_xor as f64 / total_operators as f64);
            features.insert("ratio_not".to_string(), count_not as f64 / total_operators as f64);
        } else {
            features.insert("ratio_and".to_string(), 0.0);
            features.insert("ratio_or".to_string(), 0.0);
            features.insert("ratio_xor".to_string(), 0.0);
            features.insert("ratio_not".to_string(), 0.0);
        }
        
        let all_nodes_list = if let Some(ref root) = self.root {
            self.collect_all_nodes(root)
        } else {
            Vec::new()
        };
        features.insert("num_parentheses".to_string(), (all_nodes_list.len() * 2) as f64);
        
        // 注意：max_nesting_depth 會在 extract_expression_complexity_features 中重新計算
        // 這裡先計算一個初始值（從根節點開始的深度）
        let max_nesting = if let Some(ref root) = self.root {
            self.calculate_max_nesting(root, 0)
        } else {
            0
        };
        // 插入初始值，但會被 extract_expression_complexity_features 中的值覆蓋
        features.insert("max_nesting_depth".to_string(), max_nesting as f64);
        
        features
    }

    fn get_expression_length(&self, node: &SExprNode) -> usize {
        if node.is_leaf() {
            return 1;
        }
        1 + node.children().iter().map(|c| self.get_expression_length(c)).sum::<usize>()
    }

    pub fn extract_expression_complexity_features(&self) -> HashMap<String, f64> {
        let mut features = HashMap::new();
        
        let all_nodes_list = if let Some(ref root) = self.root {
            self.collect_all_nodes(root)
        } else {
            Vec::new()
        };
        
        // expr_length 計算已註釋掉
        // let mut expr_sizes = Vec::new();
        // if let Some(ref root) = self.root {
        //     fn collect_sizes(n: &SExprNode, extractor: &SExprFeatureExtractor, sizes: &mut Vec<usize>) {
        //         if !n.is_leaf() {
        //             let size = extractor.get_expression_length(n);
        //             sizes.push(size);
        //             for child in n.children() {
        //                 collect_sizes(child, extractor, sizes);
        //             }
        //         }
        //     }
        //     collect_sizes(root, self, &mut expr_sizes);
        // }
        // 
        // if !expr_sizes.is_empty() {
        //     let sum: usize = expr_sizes.iter().sum();
        //     let mean = sum as f64 / expr_sizes.len() as f64;
        //     let max = *expr_sizes.iter().max().unwrap();
        //     let min = *expr_sizes.iter().min().unwrap();
        //     
        //     let variance: f64 = expr_sizes.iter()
        //         .map(|&x| {
        //             let diff = x as f64 - mean;
        //             diff * diff
        //         })
        //         .sum::<f64>() / expr_sizes.len() as f64;
        //     
        //     features.insert("avg_expr_length".to_string(), mean);
        //     features.insert("max_expr_length".to_string(), max as f64);
        //     features.insert("min_expr_length".to_string(), min as f64);
        //     features.insert("std_expr_length".to_string(), variance.sqrt());
        // } else {
        //     features.insert("avg_expr_length".to_string(), 0.0);
        //     features.insert("max_expr_length".to_string(), 0.0);
        //     features.insert("min_expr_length".to_string(), 0.0);
        //     features.insert("std_expr_length".to_string(), 0.0);
        // }
        
        // 設置默認值
        // features.insert("avg_expr_length".to_string(), 0.0);
        // features.insert("max_expr_length".to_string(), 0.0);
        // features.insert("min_expr_length".to_string(), 0.0);
        // features.insert("std_expr_length".to_string(), 0.0);
        
        let mut nesting_depths = Vec::new();
        if let Some(ref root) = self.root {
            fn collect_nesting(n: &SExprNode, depth: usize, depths: &mut Vec<usize>) {
                if !n.is_leaf() {
                    depths.push(depth);
                    for child in n.children() {
                        collect_nesting(child, depth + 1, depths);
                    }
                }
            }
            collect_nesting(root, 0, &mut nesting_depths);
        }
        
        if !nesting_depths.is_empty() {
            let sum: usize = nesting_depths.iter().sum();
            let mean_nesting = sum as f64 / nesting_depths.len() as f64;
            let max_nesting = *nesting_depths.iter().max().unwrap();
            let min_nesting = *nesting_depths.iter().min().unwrap();
            
            let variance_nesting: f64 = nesting_depths.iter()
                .map(|&x| {
                    let diff = x as f64 - mean_nesting;
                    diff * diff
                })
                .sum::<f64>() / nesting_depths.len() as f64;
            
            features.insert("avg_nesting_depth".to_string(), mean_nesting);
            features.insert("max_nesting_depth".to_string(), max_nesting as f64);
            features.insert("min_nesting_depth".to_string(), min_nesting as f64);
            features.insert("std_nesting_depth".to_string(), variance_nesting.sqrt());
        } else {
            features.insert("avg_nesting_depth".to_string(), 0.0);
            features.insert("max_nesting_depth".to_string(), 0.0);
            features.insert("min_nesting_depth".to_string(), 0.0);
            features.insert("std_nesting_depth".to_string(), 0.0);
        }
        
        features
    }

    pub fn extract_graph_features(&self) -> HashMap<String, f64> {
        // 圖特徵已移除，因為 EQN 和 S-expression 的圖結構本質不同
        // - EQN：基於壓縮表示的圖（中間變數定義一次，可重用）
        // - S-expression：基於完全展開的圖（每次使用都是獨立節點）
        let mut features = HashMap::new();
        features
    }

    pub fn extract_all_features(&mut self, sexpr_str: &str) -> Result<HashMap<String, f64>, String> {
        self.parse_sexpr(sexpr_str)?;
        
        let mut features = HashMap::new();
        features.extend(self.extract_structural_features());
        features.extend(self.extract_syntactic_features());
        features.extend(self.extract_expression_complexity_features());
        features.extend(self.extract_graph_features());
        
        Ok(features)
    }

    /// 提取所有特征并返回为固定顺序的 Vec<f64>（27个特征）
    /// 按照 CSV 训练数据中的特征顺序返回（与 mlp_model_area.rs 中的标准化参数顺序对齐）
    pub fn extract_features_vector(&mut self, sexpr_str: &str) -> Result<Vec<f64>, String> {
        let features = self.extract_all_features(sexpr_str)?;
        
        // 按照 CSV 文件中的特征顺序（训练时使用的顺序），与 mlp_model_area.rs 对齐
        // 这个顺序必须与 graph50000new.csv 中的特征列顺序一致
        let feature_names = vec![
            "num_internal_nodes",      // 0
            "max_logic_depth",         // 1
            "avg_logic_depth",         // 2
            "avg_fanin",               // 3
            "max_fanin",               // 4
            "avg_fanout",              // 5
            "max_fanout",              // 6
            "count_and",               // 7
            "count_or",                // 8
            "count_xor",               // 9
            "count_not",               // 10
            "total_operators",         // 11
            "ratio_and",               // 12
            "ratio_or",                // 13
            "ratio_xor",               // 14
            "ratio_not",               // 15
            "num_parentheses",         // 16
            "max_nesting_depth",       // 17
            // "avg_expr_length",         // 18
            // "max_expr_length",         // 19
            // "min_expr_length",         // 20
            // "std_expr_length",         // 21
            "avg_nesting_depth",       // 22
            "min_nesting_depth",       // 23
            "std_nesting_depth",       // 24
            // 圖特徵已移除：graph_nodes, graph_edges, graph_density, avg_degree
        ];
        
        let mut result = Vec::new();
        for name in feature_names {
            result.push(*features.get(name).unwrap_or(&0.0));
        }
        
        Ok(result)
    }
}

impl Default for SExprFeatureExtractor {
    fn default() -> Self {
        Self::new()
    }
}

