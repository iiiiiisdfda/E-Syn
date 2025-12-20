# Prop 语言定义说明

## `define_language!` 宏

第 20-31 行使用 egg 库的 `define_language!` 宏定义了 `Prop` 语言：

```rust
define_language! {
    enum Prop {
        Bool(bool),
        "*" = And([Id; 2]),
        "!" = Not(Id),
        "+" = Or([Id; 2]),
        "->" = Implies([Id; 2]),
        "let" = Let([Id; 2]),
        "&" = Concat([Id; 2]),  // 第 28 行
        Symbol(Symbol),
    }
}
```

## 第 28 行详解

```rust
"&" = Concat([Id; 2])
```

### 语法结构

- `"&"` - **字符串字面量**：表示在 S-expression 中使用的操作符名称
- `=` - **赋值符号**：将字符串映射到 Rust 枚举变体
- `Concat` - **枚举变体名**：Rust 中生成的枚举变体名称
- `[Id; 2]` - **参数类型**：表示 `Concat` 接受 2 个 `Id` 类型的参数

### 含义

这行代码定义了：
- **操作符名称**：`&`（在 S-expression 中使用）
- **操作符类型**：`Concat`（连接操作符）
- **参数数量**：2 个参数（二元操作符）
- **参数类型**：`Id`（e-graph 中的节点 ID）

### 生成的 Rust 代码

`define_language!` 宏会生成类似这样的枚举：

```rust
enum Prop {
    Bool(bool),
    And([Id; 2]),      // 对应 "*"
    Not(Id),           // 对应 "!"
    Or([Id; 2]),       // 对应 "+"
    Implies([Id; 2]),  // 对应 "->"
    Let([Id; 2]),      // 对应 "let"
    Concat([Id; 2]),   // 对应 "&"  ← 第 28 行定义的
    Symbol(Symbol),
}
```

### 使用示例

在 S-expression 中：
```
(& expr1 expr2)
```

会被解析为：
```rust
Prop::Concat([id1, id2])
```

其中 `id1` 和 `id2` 是 `expr1` 和 `expr2` 在 e-graph 中的节点 ID。

## 所有操作符定义

| 行号 | S-expression 符号 | Rust 枚举变体 | 参数数量 | 含义 |
|------|------------------|--------------|---------|------|
| 22 | `Bool` | `Bool(bool)` | 0 | 布尔常量 |
| 23 | `*` | `And([Id; 2])` | 2 | AND（逻辑与） |
| 24 | `!` | `Not(Id)` | 1 | NOT（逻辑非） |
| 25 | `+` | `Or([Id; 2])` | 2 | OR（逻辑或） |
| 26 | `->` | `Implies([Id; 2])` | 2 | 蕴含 |
| 27 | `let` | `Let([Id; 2])` | 2 | Let 绑定 |
| **28** | **`&`** | **`Concat([Id; 2])`** | **2** | **连接（多输出）** |
| 29 | `Symbol` | `Symbol(Symbol)` | 0 | 符号/变量 |

## `Concat` 的特殊处理

在第 64-67 行，`Concat` 在 `ConstantFold` 分析中的处理：

```rust
Prop::Concat([a, b]) => Some((
    x(a)? > x(b)?,  // 比较两个表达式的布尔值
    format!("(& {} {})", x(a)?, x(b)?).parse().unwrap(),
)),
```

**注意：**
- `Concat` 被当作比较操作（`x(a)? > x(b)?`）
- 这可能是为了在常量折叠时处理 `&` 操作符
- 但实际上 `&` 主要用于连接多个输出，不是逻辑操作

## 总结

第 28 行 `"&" = Concat([Id; 2])` 的含义：
- **定义**：在 Prop 语言中添加 `&` 操作符
- **类型**：二元操作符（2 个参数）
- **用途**：连接多个输出信号（由 `circuitparser` 生成）
- **处理**：在常量折叠时被当作比较操作

这是 egg 库中定义自定义语言的标准方式，允许你定义自己的操作符和语法。

