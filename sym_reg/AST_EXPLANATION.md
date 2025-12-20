# AST（抽象语法树）说明

## AST 是什么？

**AST** = **Abstract Syntax Tree**（抽象语法树）

### 基本概念

AST 是一种树形数据结构，用于表示程序或表达式的语法结构：
- **节点**：表示操作符或操作数
- **边**：表示操作符与操作数之间的关系
- **根节点**：表示整个表达式
- **叶子节点**：表示变量或常量

### 在电路分析中的应用

在这个项目中，AST 用于表示**逻辑表达式的结构**。

## 示例

### S-expression 表达式
```
(* (+ a b) (! c))
```

### 对应的 AST 结构
```
        *
       / \
      +   !
     / \   \
    a   b   c
```

**树结构说明：**
- 根节点：`*` (AND)
- 左子树：`+` (OR) 操作，包含 `a` 和 `b`
- 右子树：`!` (NOT) 操作，包含 `c`

## ASTSize（AST 大小）

### 定义
AST 中**节点的总数**（包括所有操作符和操作数）。

### 计算方法
```rust
pub struct AstSize;
impl<L: Language> CostFunction<L> for AstSize {
    fn cost<C>(&mut self, enode: &L, mut costs: C) -> Self::Cost {
        enode.fold(1, |sum, id| sum.saturating_add(costs(id)))
    }
}
```

**计算逻辑：**
- 每个节点贡献 1
- 递归累加所有子节点的数量
- 结果 = 1（当前节点）+ 所有子节点的 ASTSize 之和

### 示例
对于 `(* (+ a b) (! c))`：
- `*` 节点：1 + (左子树大小) + (右子树大小)
- `+` 节点：1 + 1 + 1 = 3（a, b, +）
- `!` 节点：1 + 1 = 2（c, !）
- 总大小：1 + 3 + 2 = **6 个节点**

## ASTDepth（AST 深度）

### 定义
从根节点到**最深叶子节点**的路径长度（层数）。

### 计算方法
```rust
pub struct AstDepth;
impl<L: Language> CostFunction<L> for AstDepth {
    fn cost<C>(&mut self, enode: &L, mut costs: C) -> Self::Cost {
        1 + enode.fold(0, |max, id| max.max(costs(id)))
    }
}
```

**计算逻辑：**
- 每个节点贡献 1 层
- 取所有子节点深度的最大值
- 结果 = 1（当前层）+ 子节点深度的最大值

### 示例
对于 `(* (+ a b) (! c))`：
```
层 1: *
层 2: +, !
层 3: a, b, c
```
深度 = **3 层**

## 在 CSV 数据中的意义

在 `mig_circuit_analysis.csv` 中：

| 列名 | 含义 | 示例值 |
|------|------|--------|
| `ASTSize` | AST 节点总数 | 584 |
| `ASTDepth` | AST 最大深度 | 25 |

### 为什么重要？

1. **电路复杂度指标**：
   - `ASTSize` 越大 → 电路越复杂（更多节点）
   - `ASTDepth` 越大 → 电路层级越深（关键路径更长）

2. **与物理属性的关系**：
   - `ASTSize` 通常与 `area`（面积）相关
   - `ASTDepth` 通常与 `delay`（延迟）相关

3. **用于机器学习**：
   - 作为特征预测电路的物理属性
   - 帮助模型理解电路的结构特征

## 实际例子

从 `simple_circuit_0.data`：
```
ASTSize: 584
ASTDepth: 25
```

这表示：
- 该电路的 AST 有 **584 个节点**
- AST 的最大深度为 **25 层**
- 说明这是一个相对复杂的电路

## 计算流程

1. **输入**：S-expression 字符串
   ```
   (& (& ... (表达式) ...))
   ```

2. **解析**：将字符串解析为 `RecExpr<Prop>`
   ```rust
   let expr: RecExpr<Prop> = s.parse().unwrap();
   ```

3. **计算 ASTSize**：
   ```rust
   let mut ast_size = AstSize;
   let size = ast_size.cost_rec(&expr);
   ```

4. **计算 ASTDepth**：
   ```rust
   let mut ast_depth = AstDepth;
   let depth = ast_depth.cost_rec(&expr);
   ```

5. **输出**：`ASTSize: 584`, `ASTDepth: 25`

## 总结

- **AST** = 抽象语法树，表示表达式的树形结构
- **ASTSize** = 树中节点的总数（复杂度指标）
- **ASTDepth** = 树的最大深度（层级指标）
- 这两个特征用于描述电路的结构复杂度，是机器学习模型的重要输入特征



