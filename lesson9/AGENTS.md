# Lesson 9: Flask 專案說明

這是一個使用 Python Flask 框架開發的簡易網頁應用程式。

## 環境與執行

本專案使用 `uv` 作為虛擬環境與套件管理工具。

執行應用程式（請在專案根目錄 `python_web_2025` 執行）：
```bash
uv run python ./lesson9/app.py
```

## 專案結構

```
/lesson9
├── app.py              # Flask 應用程式主檔案（啟動點）
├── requirements.txt    # 專案依賴（如 flask）
├── templates/          # HTML 樣板
│   └── ... 
├── static/             # 靜態資源（CSS / JS / images）
│   ├── css/
│   └── js/
└── README.md           # 本目錄的簡要說明
```

## 開發注意事項

- 所有 HTML 樣板請放在 `templates/`，靜態檔案放在 `static/`。
- 建議將 CSS 規則放入 `.css` 檔案，避免大量行內樣式（inline style）。
- 若新增後端或資料處理邏輯，請遵循「模組化」原則：將純邏輯放在模組中（例如 lesson9 下的 utils/module），I/O 與互動放在 app 或腳本中。
- 使用 UTF-8 編碼以確保中文顯示正確。
2.  **執行專案**: `uv run python ./lesson9/app.py`
>>>>>>> 3ec8829d9406606a570eb7bce9756ae249839fdb

### 開發規範

*   Flask 網頁樣版請放置於 `templates` 資料夾。
*   CSS, JavaScript, 圖片等靜態檔案請放置於 `static` 資料夾。
*   請避免在 HTML 中使用行內樣式(inline style)，應將 CSS 規則統一寫在對應的 `.css` 檔案中。
=======
# Lesson 9: Flask 專案說明

這是一個使用 Python Flask 框架開發的簡易網頁應用程式。

## 環境與執行

本專案使用 `uv` 作為虛擬環境與套件管理工具。

**執行應用程式：**
請在**專案根目錄** (`python_web_2025`) 執行以下指令來啟動伺服器：
```bash
uv run python ./lesson9/app.py
```

## 專案結構
- **`templates/`**: 存放所有 HTML 樣板檔案。
- **`static/`**: 存放所有 CSS、JavaScript 和圖片等靜態檔案。

## 開發注意事項
- 若有修改網頁樣式，建議將行內 CSS (inline CSS) 整理並更新到對應的 `.css` 檔案中，以利於程式碼的整潔與後續維護。
>>>>>>> bb1d9793f1518be19249ca92557bc5c2927f5b09
