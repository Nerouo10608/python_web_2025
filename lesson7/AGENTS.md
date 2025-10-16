# Lesson 6: Flask 專案說明

這是一個使用 Python Flask 框架開發的簡易網頁應用程式。

## 環境與執行

本專案使用 `uv` 作為虛擬環境與套件管理工具。

**執行應用程式：**
請在**專案根目錄** (`python_web_2025`) 執行以下指令來啟動伺服器：
```bash
uv run python ./lesson6/app.py
```

## 專案結構
- **`templates/`**: 存放所有 HTML 樣板檔案。
- **`static/`**: 存放所有 CSS、JavaScript 和圖片等靜態檔案。

## 開發注意事項
- 若有修改網頁樣式，建議將行內 CSS (inline CSS) 整理並更新到對應的 `.css` 檔案中，以利於程式碼的整潔與後續維護。