#!/bin/bash
echo "get ready to started process!"
ps -ef | grep java
# 定义进程识别字符串
PROCESS="dbgpt start webserver --config configs/dbgpt-proxy-siliconflow.toml"

# 查找进程ID
PID=$(ps aux | grep -i "$PROCESS" | grep -v grep | awk '{print $2}')

# 如果进程存在，杀死它
if [ ! -z "$PID" ]; then
    echo "Found existing process with PID: $PID, killing it..."
    kill -9 $PID
    # 等待进程终止
    sleep 2
fi

# 后台启动进程
echo "Starting new process in background..."
nohup uv run $PROCESS > dbgpt-webserver.log 2>&1 &
ps -ef | grep java
echo "Process started successfully!"
