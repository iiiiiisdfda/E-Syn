# AST 数据来源说明

## AST 是由哪个工具计算的？

**ASTSize 和 ASTDepth 是由 `analyzer` 工具计算的。**

## 数据流程

### 1. **数据收集流程**

```
AIG/MIG 电路
    ↓
ABC (转换为 EQN)
    ↓
circuitparser (处理多输出)
    ↓
s-converter/infix2lisp (转换为 S-expression)
    ↓
analyzer (计算 ASTSize 和 ASTDepth) ← 这里！
    ↓
输出到 .data 文件
    ↓
parse_data (解析到 CSV)
```

### 2. **analyzer 工具的位置**

**路径：** `sym_reg/analyzer/target/release/analyzer`

**调用方式：**
```bash
analyzer <sexpr_file> <dot_name> > <output_data_file>
```

**在 `data_collect_mig.py` 中的调用：**
```python
analyzer_path = "../sym_reg/analyzer/target/release/analyzer"
dot_name = f"simple_circuit_{i}"
os.system(f"{analyzer_path} {sexpr_file} {dot_name} > {data_file} 2>&1")
```

### 3. **analyzer 工具的功能**

`analyzer` 工具（`sym_reg/analyzer/src/main.rs`）会：

1. **读取 S-expression 文件**
   ```rust
   let mut input_file = File::open(input_path)?;
   let mut contents = String::new();
   input_file.read_to_string(&mut contents)?;
   ```

2. **统计操作符**（第 210 行）
   ```rust
   let operator_counts = count_operators(&contents);
   // 输出: +, !, *, & 的数量
   ```

3. **计算 ASTSize 和 ASTDepth**（第 220 行）
   ```rust
   let (size, depth) = count_ast_size_and_depth(&contents, &dot_name);
   println!("ASTSize: {}", size);
   println!("ASTDepth: {}", depth);
   ```

4. **计算其他统计信息**
   - SUM_LIB
   - SUM_NODE
   - AVE_LIB

### 4. **AST 计算的具体实现**

**代码位置：** `sym_reg/analyzer/src/main.rs` 第 187-201 行

```rust
fn count_ast_size_and_depth(s: &str, dot_name: &str) -> (usize, usize) {
    // 1. 解析 S-expression 为 RecExpr<Prop>
    let expr: RecExpr<Prop> = s.parse().unwrap();
    
    // 2. 创建 ASTSize 和 ASTDepth 计算器
    let mut ast_size = AstSize;
    let mut ast_depth = AstDepth;
    
    // 3. 计算 ASTSize（节点总数）
    let size = ast_size.cost_rec(&expr);
    
    // 4. 计算 ASTDepth（最大深度）
    let depth = ast_depth.cost_rec(&expr);
    
    // 5. 生成 DOT 图文件（可选）
    let mut egraphout = EGraph::new(ConstantFold {});
    egraphout.add_expr(&expr);
    egraphout.dot().to_dot(output_file_path);
    
    (size, depth)
}
```

### 5. **ASTSize 和 ASTDepth 的计算方法**

**ASTSize（第 165-174 行）：**
```rust
pub struct AstSize;
impl<L: Language> CostFunction<L> for AstSize {
    fn cost<C>(&mut self, enode: &L, mut costs: C) -> Self::Cost {
        enode.fold(1, |sum, id| sum.saturating_add(costs(id)))
    }
}
```
- **计算方式**：递归累加所有节点
- **结果**：AST 中节点的总数

**ASTDepth（第 176-185 行）：**
```rust
pub struct AstDepth;
impl<L: Language> CostFunction<L> for AstDepth {
    fn cost<C>(&mut self, enode: &L, mut costs: C) -> Self::Cost {
        1 + enode.fold(0, |max, id| max.max(costs(id)))
    }
}
```
- **计算方式**：递归计算最大深度
- **结果**：从根节点到最深叶子节点的层数

### 6. **输出格式**

`analyzer` 工具输出到 `.data` 文件：

```
&: 22
+: 11
!: 173
*: 172
ASTSize: 584        ← 由 analyzer 计算
ASTDepth: 25        ← 由 analyzer 计算
SUM_LIB: 5627
SUM_NODE: 378
AVE_LIB: 15.8061797752809
```

### 7. **在 CSV 中的位置**

在 `mig_circuit_analysis.csv` 中：
```
+,!,*,&,ASTSize,ASTDepth,lev,power,area,delay
```

- **ASTSize** 和 **ASTDepth** 来自 `analyzer` 工具的输出
- 它们被解析并写入 CSV 文件的第 5 和第 6 列

## AST 是从 S-expression 来的吗？

**是的！AST 完全是从 S-expression 计算出来的。**

### 完整的数据流程

```
AIG/MIG 电路 (.aig)
    ↓
ABC (转换为 EQN)
    ↓ simple_circuit_0.eqn
circuitparser (处理多输出)
    ↓ simple_circuit_0_processed.eqn
s-converter/infix2lisp (转换为 S-expression)
    ↓ simple_circuit_0.sexpr ← S-expression 文件
analyzer (读取 S-expression，计算 AST)
    ↓
解析 S-expression → RecExpr<Prop>
    ↓
计算 ASTSize 和 ASTDepth
    ↓ simple_circuit_0.data
parse_data (解析到 CSV)
    ↓ mig_circuit_analysis.csv
```

### 关键代码证据

**1. analyzer 读取 S-expression 文件（第 207-209 行）：**
```rust
let input_path = &args[1];  // 传入的是 .sexpr 文件路径
let mut input_file = File::open(input_path)?;
let mut contents = String::new();
input_file.read_to_string(&mut contents)?;  // 读取 S-expression 内容
```

**2. 解析 S-expression 为 AST（第 188 行）：**
```rust
let expr: RecExpr<Prop> = s.parse().unwrap();  // 将 S-expression 字符串解析为 RecExpr
```

**3. 从 RecExpr 计算 ASTSize 和 ASTDepth（第 191-192 行）：**
```rust
let size = ast_size.cost_rec(&expr);   // 从解析后的 AST 计算节点数
let depth = ast_depth.cost_rec(&expr);  // 从解析后的 AST 计算深度
```

### S-expression 示例

**文件：** `simple_circuit_0.sexpr`
```
(& (& (& (& (& ... 0 pi19) (! pi20)) (* pi17 (! pi18))) ...)
```

这是一个嵌套的 S-expression，表示电路的逻辑结构。

**analyzer 的工作：**
1. 读取这个 S-expression 字符串
2. 解析为 `RecExpr<Prop>`（这就是 AST）
3. 遍历 AST 计算：
   - **ASTSize**：节点总数（包括所有操作符和变量）
   - **ASTDepth**：从根到最深叶子的层数

## 总结

| 数据项 | 来源工具 | 输入格式 | 说明 |
|--------|---------|---------|------|
| `+`, `!`, `*`, `&` | `analyzer` | **S-expression** | 操作符统计 |
| **ASTSize** | **`analyzer`** | **S-expression** | **从 S-expression 解析的 AST 节点总数** |
| **ASTDepth** | **`analyzer`** | **S-expression** | **从 S-expression 解析的 AST 最大深度** |
| `SUM_LIB`, `SUM_NODE`, `AVE_LIB` | `analyzer` | **S-expression** | Liberty 统计 |
| `lev`, `power`, `area`, `delay` | `mockturtle` 或 `ABC` | AIG/MIG 文件 | 物理属性 |

**关键点：**
- **ASTSize 和 ASTDepth 都是从 S-expression 计算出来的**
- `analyzer` 读取 `.sexpr` 文件（S-expression 格式）
- 使用 egg 库的 `RecExpr` 将 S-expression 解析为 AST
- 从解析后的 AST 计算 `ASTSize`（节点总数）和 `ASTDepth`（最大深度）
- 输出到 `.data` 文件，然后被解析到 CSV

**所以回答你的问题：是的，AST 是从 S-expression 来的！**

