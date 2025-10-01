## AI 協作說明 — python_web_2025

本倉庫是 Python/資料處理與基礎 Web 教學範例集合（含 notebooks 與腳本）。目標是讓代理能快速定位檔案、用正確方式執行/擴充，並遵循既有模式寫出可維護的課程範例。

### 專案結構與重點
- 根目錄：`pyproject.toml`（Python>=3.10；deps: flask, notebook, requests），`uv.lock`（建議用 uv 管理環境）。
- 課程資料：
  - `lesson1/`、`lesson2/`：Python 基礎與函式（參見 `lesson2/README.md`、`lesson2/AGENTS.md`）。
  - `lesson3/`：資料抓取與資料處理模式（關鍵：`lesson3/tools.py`、`lesson3_3.py`）。
  - `lesson4/`：練習/演算法小題。
- 風格：以 CLI/print 與 `input()` 互動為主；教學文字多為繁體中文。

### 執行與環境（Windows/cmd）
- 建議使用 uv（因有 `uv.lock`）
  - 建置依賴：`uv sync`
  - 執行腳本：`uv run python lesson3\lesson3_3.py`
- 若用 pip（無 requirements.txt）：`py -m venv .venv && .venv\Scripts\activate && pip install flask notebook requests`
- 執行含輸入的腳本（範例將「板橋區」餵給程式）：`echo 板橋區 | uv run python lesson3\lesson3_3.py`

### 既有程式設計模式（請延續）
- 分層：
  - 資料/網路層在模組（例如 `lesson3/tools.py`）中提供「小而純」的函式。
  - I/O 與互動在可執行腳本（例如 `lesson3_3.py`）中進行。
- 例：`download_youbike_data() -> list` 以 requests 取回外部 JSON；`get_area(data) -> list` 從項目萃取 `sarea`；`get_sites_of_area(data, area) -> list` 依區域過濾。
- 命名：snake_case，函式簽章簡潔清楚；輸出以可列印資料結構為主（list/dict）。

### 外部整合與資料流
- 對外資料：新北市 YouBike 開放資料（JSON）。呼叫在 `lesson3/tools.py`，下游函式只處理 Python 物件，不直接發網路請求。
- 請保持「網路 I/O 與資料轉換分離」：新增功能時，先在 tools 模組寫純函式，再在執行腳本組裝流程與互動。

### 常見陷阱與修正建議（維持可用範例為主）
- `tools.download_youbike_data()` 中 `response.raise_for_status` 需呼叫成 `response.raise_for_status()`，且避免重複 `requests.get()`；若你改動此區，保留既有的例外處理訊息格式（繁中）。
- 以 `UTF-8` 讀寫檔案/字串，確保中文正常顯示。
- Notebook 用於探索；可重用的邏輯請放 `.py` 模組並從 notebook 匯入。

### 新增功能的建議落點（依既有模式）
- 新資料來源或轉換：加到 `lesson3/tools.py` 或新增相近模組，提供純函式 API（輸入/輸出為 Python 內建型別）。
- 新互動腳本或示範：新增到對應 `lessonX/` 目錄（例如 `lesson3/your_demo.py`），在 `if __name__ == "__main__":` 中組裝流程與輸入提示。

### 小範例（延續專案風格）
```python
# 讀取資料 → 列區域 → 依選擇過濾
import tools
data = tools.download_youbike_data()
areas = tools.get_area(data)
print("可查詢區域:", " ".join(areas))
sites = tools.get_sites_of_area(data, area="板橋區")
print(f"板橋區站點數: {len(sites)}")
```

若有你常用但文件未涵蓋的工作流程（例如 VS Code 偵錯設定、Flask 實作路徑等），請回饋，我們會補充到本檔使代理能即時上手。
