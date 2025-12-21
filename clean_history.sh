#!/bin/bash
# 从 git 历史中移除 xgboost_tmp 目录

cd /home/ice890425/E-Syn

echo "=== 步骤 1: 从所有分支和标签的历史中移除 xgboost_tmp ==="
git filter-branch --force --index-filter 'git rm -rf --cached --ignore-unmatch xgboost_tmp' --prune-empty --tag-name-filter cat -- --all

echo ""
echo "=== 步骤 2: 清理备份引用 ==="
rm -rf .git/refs/original/

echo ""
echo "=== 步骤 3: 清理 reflog ==="
git reflog expire --expire=now --all

echo ""
echo "=== 步骤 4: 垃圾回收 ==="
git gc --prune=now --aggressive

echo ""
echo "=== 步骤 5: 验证大文件是否已移除 ==="
COUNT=$(git rev-list --objects --all | grep "xgboost_tmp/aigfuzz_random/fuzz_circuit_7_processed.eqn" | wc -l)
echo "找到 $COUNT 个大文件引用（应该为 0）"

if [ "$COUNT" -eq 0 ]; then
    echo "✓ 成功！大文件已从历史中移除"
    echo ""
    echo "现在可以推送："
    echo "  git push origin main --force"
else
    echo "✗ 警告：仍有大文件在历史中"
fi

