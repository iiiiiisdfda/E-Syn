# `&` (Concat) 操作符说明

## `&` 操作符的来源

### 1. **在 EQN 文件中**
在 `simple_circuit_0.eqn` 文件中，**没有 `&` 操作符**。EQN 格式只使用：
- `*` - AND 操作符
- `+` - OR 操作符  
- `!` - NOT 操作符

### 2. **在 S-expression 文件中**
在 `simple_circuit_0.sexpr` 文件中，有 **22 个 `&` 操作符**。

### 3. **`&` 是如何产生的？**

`&` 是由 `circuitparser` 工具在**处理多输出电路**时自动添加的。

**代码位置：** `alpha_utils/circuitparser/src/main.rs` 第 149-150 行

```rust
while equations.len() > 1 {
    equations[0] = format!("({} & {})", equations[0], equations[1]);
    num_concat += 1;
    equations.remove(1);
}
```

**工作原理：**
1. 当电路有多个输出时（例如：po00, po01, po02, ..., po22）
2. `circuitparser` 会将所有输出用 `&` 连接起来
3. 形成一个大的 S-expression

**示例：**
如果有 3 个输出：
```
po00 = expr1
po01 = expr2  
po02 = expr3
```

会被转换为：
```
(& (& expr1 expr2) expr3)
```

### 4. **`&` 的含义**

在 Prop 语言中，`&` 被定义为 **`Concat`（连接）操作符**：

```rust
define_language! {
    enum Prop {
        "&" = Concat([Id; 2]),  // 连接操作符
        "*" = And([Id; 2]),     // AND 操作符
        "+" = Or([Id; 2]),      // OR 操作符
        "!" = Not(Id),          // NOT 操作符
    }
}
```

**作用：**
- `&` 用于**连接多个输出信号**
- 它不是逻辑操作符（不是 AND）
- 它只是将多个输出组合成一个表达式

### 5. **为什么有 22 个 `&`？**

`simple_circuit_0.eqn` 有 **23 个输出**（po00 到 po22）：
- 23 个输出需要 **22 个连接符**（n 个输出需要 n-1 个连接符）
- 所以 `&` 的数量 = 23 - 1 = 22

### 6. **在统计中的意义**

在 `analyzer` 工具统计操作符时：
- `&` 被统计为"其他操作符"
- 它代表**多输出电路的连接结构**
- 不是逻辑门，而是**结构信息**

### 7. **总结**

| 操作符 | 在 EQN 中 | 在 S-expression 中 | 含义 |
|--------|-----------|-------------------|------|
| `*` | ✅ | ✅ | AND（逻辑与） |
| `+` | ✅ | ✅ | OR（逻辑或） |
| `!` | ✅ | ✅ | NOT（逻辑非） |
| `&` | ❌ | ✅ | Concat（连接，仅用于多输出） |

**关键点：**
- `&` **不是** EQN 格式中的操作符
- `&` **是** `circuitparser` 在处理多输出电路时添加的
- `&` 用于将多个输出连接成一个 S-expression
- 在统计中，`&` 的数量 = 输出数量 - 1



