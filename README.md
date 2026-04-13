# NexusFlow
專案管理、工具調度side project

## 後端啟動環境指令 (backend_server)

啟動前請確保 `.env` 檔案設定完成。

### 1. 啟動服務
平時開發或僅變動環境變數時使用：
```bash
cd backend_server
docker-compose up -d
```

### 2. 重新構建程式
```bash
docker-compose up -d --build
```

### 3. 停止所有容器
```bash
docker-compose down
```