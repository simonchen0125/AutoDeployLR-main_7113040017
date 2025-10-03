# 互動式線性迴歸分析儀 (CRISP-DM)

這是一個基於 Streamlit 開發的互動式網頁應用，旨在透過視覺化的方式，幫助使用者深入理解簡單線性迴歸模型。

整個專案的開發流程與應用程式的介面結構，皆遵循 **CRISP-DM (跨產業資料探勘標準流程)** 框架，從商業理解到最終部署，提供一個完整的範例。

## 🚀 線上展示 (Demo Site)

您可以透過以下連結，直接在線上操作此應用程式：

[https://hw1-7113040017.streamlit.app/](https://hw1-7113040017.streamlit.app/)

## ✨ 主要功能

-   **互動式參數調整**: 使用者可以透過側邊欄的滑桿，即時調整以下參數來生成資料：
    -   資料點數量 (n)
    -   真實斜率 (a)
    -   雜訊變異數 (Noise Variance)
-   **即時視覺化**: 所有參數的變更都會立即反映在圖表上，包含：
    -   資料散佈圖
    -   模型擬合的迴歸線 (紅色)
    -   真實資料的關係線 (綠色虛線)
-   **模型評估**: 即時計算並顯示模型的關鍵評估指標：
    -   **量化指標**: 均方誤差 (MSE) 和 R 平方 (R-squared)。
    -   **視覺化指標**: 透過圖表直觀感受擬合效果。
-   **離群值分析**: 自動標示出對模型影響最大的前 5 個離群值。
-   **資料下載**: 提供按鈕讓使用者可以下載當前參數下生成的 CSV 資料檔。

## 🛠️ 技術棧 (Technology Stack)

-   **Python 3.8+**
-   **Streamlit**: 用於快速建構互動式網頁應用。
-   **Scikit-learn**: 用於建立與訓練線性迴歸模型。
-   **Pandas**: 資料處理與管理。
-   **Numpy**: 數值運算。
-   **Altair**: 互動式資料視覺化圖表。

## 💻 本地安裝與執行

請依照以下步驟來設定並在您的電腦上執行本專案。

**1. 前置要求**

-   確認您的電腦已安裝 Python 3.8 或更高版本。

**2. 複製專案**

```bash
git clone https://github.com/simonchen0125/AutoDeployLR-main_7113040017.git
cd AutoDeployLR-main_7113040017
```

**3.建立虛擬環境**

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

**4.安裝相依套件**

```bash
pip install -r requirements.txt
```

**5.執行 Streamlit 應用**

```bash
streamlit run app.py
```
