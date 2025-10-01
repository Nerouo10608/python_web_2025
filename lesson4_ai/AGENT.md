## 這是一個flask的專案
## 工作目錄
- __python_web_2025__\lesson4_ai

## 使用uv進入虛擬環境
- source .venv\Scripts\activate

### 啟動 Flask 專案
- 建置依賴：uv sync
- 啟動開發伺服器：uv run python lesson4_ai\app.py
- 瀏覽器開啟：http://127.0.0.1:8000/
- 或使用 Flask CLI：uv run flask --app lesson4_ai/app run --debug

### 目錄結構
```
lesson4_ai/
  app.py
  templates/
    index.html
  static/
    css/
      style.css
```

### 備註
- 頁面採 RWD（手機優先，768px 以上雙欄）。
- 檔案編碼為 UTF-8。