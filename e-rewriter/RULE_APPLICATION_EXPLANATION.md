# Egg 规则应用机制说明

## 当前实现

在 `e-rewriter` 中，使用 egg 库的 `Runner` 进行重写：

```rust
let runner = Runner::default()
    .with_explanations_enabled()
    .with_expr(&expr)
    .with_time_limit(std::time::Duration::from_secs(100))
    .with_iter_limit(runner_iteration_limit)
    .with_node_limit(egraph_node_limit)
    .run(&make_rules_enhance());
```

## Egg Runner 的工作方式

### 1. **每个迭代中检查所有规则**

在每个迭代（iteration）中，egg 的 Runner 会：
- **遍历所有规则**：对 `make_rules_enhance()` 返回的每个规则进行检查
- **尝试匹配**：对每个规则，尝试在当前的 e-graph 中找到匹配的模式
- **应用匹配的规则**：如果规则匹配成功，应用重写并更新 e-graph

### 2. **规则匹配过程**

对于每个规则：
- 规则有左侧模式（pattern），例如 `"(* ?b 0)"`
- Runner 会在 e-graph 中搜索所有匹配该模式的子图
- 如果找到匹配，创建重写并添加到 e-graph

### 3. **迭代循环**

```
迭代 1:
  - 检查规则 1 (null-element1): 匹配？应用
  - 检查规则 2 (null-element2): 匹配？应用
  - ...
  - 检查规则 N (de-morgan2): 匹配？应用
  - 更新 e-graph

迭代 2:
  - 再次检查所有规则（因为 e-graph 可能已改变）
  - ...

直到达到停止条件：
  - 迭代次数限制 (runner_iteration_limit)
  - 时间限制 (time_limit)
  - 节点数量限制 (node_limit)
  - 或没有新的匹配
```

## 当前规则列表

`make_rules_enhance()` 定义了 **22 条规则**：

1. null-element1, null-element2
2. complements1, complements2
3. covering1, covering2
4. combining1, combining2
5. identity1, identity2'
6. idempotency1, idempotency2
7. involution1
8. commutativity1, commutativity2
9. associativity1, associativity2
10. distributivity1, distributivity2
11. consensus1, consensus2
12. de-morgan1, de-morgan2

## 性能考虑

### 优点：
- **完整性**：确保所有可能的优化都被考虑
- **正确性**：不会遗漏任何匹配的规则

### 缺点：
- **性能开销**：每个迭代都要检查所有规则
- **规则数量增加时**：检查时间线性增长

## 优化建议

如果需要优化性能，可以考虑：

1. **规则优先级**：egg 支持规则优先级，可以优先检查常用规则
2. **规则分组**：将规则分成多个阶段，不同阶段应用不同规则
3. **选择性应用**：根据电路特征，只应用相关的规则子集

## 统计信息

通过 `runner.report()` 可以获取：
- 每个规则的匹配次数
- 每个规则的应用次数
- 总迭代次数

这些信息可以帮助识别：
- 哪些规则最常用
- 哪些规则从未被使用
- 规则应用的效率



