#!/bin/sh
#在sym_reg目錄下執行
set -eu

TARGET="./aigfuzz"
EMPTY="/tmp/empty_rs"

# 保證目標存在且是目錄
[ -d "$TARGET" ] || {
    echo "ERROR: ./aigfuzz not found or not a directory"
    exit 1
}

# 準備空目錄
[ -d "$EMPTY" ] || mkdir "$EMPTY"

echo "Clearing $TARGET"

# rsync 清空內容（受控刪除）
rsync -a --delete "$EMPTY"/ "$TARGET"/

# 確認是否為空（最低負擔）
if find "$TARGET" -mindepth 1 -print -quit | grep -q .; then
    echo "ERROR: directory not empty, abort rmdir"
    exit 2
fi

# 移除目錄本身
rmdir "$TARGET"
echo "Removed ./aigfuzz"
