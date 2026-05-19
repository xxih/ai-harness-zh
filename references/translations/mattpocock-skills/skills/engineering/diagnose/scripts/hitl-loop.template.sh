#!/usr/bin/env bash
# Human-in-the-loop 复现循环。
# 复制本文件,编辑下方步骤后执行。
# Agent 跑脚本,用户在终端按提示操作。
#
# 用法:
#   bash hitl-loop.template.sh
#
# 两个 helper:
#   step "<指令>"            → 显示指令,等待回车
#   capture VAR "<问题>"     → 显示问题,把回答读到 VAR
#
# 结尾会把抓到的值以 KEY=VALUE 形式打印,供 agent 解析。

set -euo pipefail

step() {
  printf '\n>>> %s\n' "$1"
  read -r -p "    [做完按回车] " _
}

capture() {
  local var="$1" question="$2" answer
  printf '\n>>> %s\n' "$question"
  read -r -p "    > " answer
  printf -v "$var" '%s' "$answer"
}

# --- 编辑下方 ---------------------------------------------------------

step "打开 http://localhost:3000 并登录。"

capture ERRORED "点击 'Export' 按钮。报错了吗?(y/n)"

capture ERROR_MSG "粘贴报错信息(或填 'none'):"

# --- 编辑上方 ---------------------------------------------------------

printf '\n--- 已抓取 ---\n'
printf 'ERRORED=%s\n' "$ERRORED"
printf 'ERROR_MSG=%s\n' "$ERROR_MSG"
