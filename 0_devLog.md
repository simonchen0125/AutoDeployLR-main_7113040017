# 1.0 專案啟動與規劃 (Project Initiation & Planning)

1.1 **建立開發日誌**: 建立 `0_devLog.md` 開始記錄專案開發歷程。/n
1.2 **需求分析 (CRISP-DM: 商業理解)**: 根據 HW1 要求，確立專案目標為建立一個互動式線性迴歸分析工具。
1.3 **功能規劃**: - 必須遵循 CRISP-DM 框架。 - 需允許使用者調整斜率 (a)、噪聲 (noise) 和資料點數量。 - 最終成果需部署為 Streamlit 或 Flask 網頁應用。
1.4 **建立任務清單**: 建立 `Todo.md`，將主要開發任務條列化。

# 2.0 開發環境設定 (Environment Setup)

2.1 **建立專案結構**: 建立初始資料夾結構與 `.gitignore` 檔案以排除不必要的檔案。
2.2 **定義相依套件**: 建立 `requirements.txt` 並列出所需套件：`streamlit`, `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `altair`。
2.3 **建立虛擬環境**: 執行 `python -m venv venv` 建立獨立的 Python 環境。
2.4 **安裝套件**: 啟動虛擬環境，並執行 `pip install -r requirements.txt` 安裝所有相依套件。
2.5 **驗證安裝**: 確認套件均已成功安裝。

# 3.0 Streamlit 應用程式核心開發 (Core App Development)

3.1 **建立主檔案**: 建立 `app.py` 作為 Streamlit 應用的進入點。
3.2 **Phase 1: 商業理解**: 在 app 中加入專案標題與目標說明。
3.3 **Phase 2 & 3: 資料理解與準備**: - 使用 `st.sidebar` 建立參數控制面板。 - 加入滑桿 (sliders) 讓使用者能調整資料點數量、斜率 `a` 與噪聲變異數。 - 撰寫資料生成函式，根據公式 `y = ax + b + noise` 產生 DataFrame。
3.4 **Phase 4: 模型建立**: - 引入 `sklearn.linear_model.LinearRegression`。 - 根據生成的資料訓練模型，並取得預測斜率與截距。 - 使用 `st.metric` 顯示模型學到的參數，並與真實值進行比較。
3.5 **Phase 5: 模型評估**: - 計算並顯示 MSE (均方誤差) 和 R-squared (R 平方) 指標。 - 使用 Altair 套件繪製互動式圖表，包含散佈圖、迴歸線與真實關係線。 - 增加離群值分析功能，找出並顯示殘差最大的幾個點。
3.6 **Phase 6: 部署**: - 在 app 結尾加入說明，闡述此 Streamlit 應用本身即為部署成果。

# 4.0 測試與驗證 (Testing & Validation)

4.1 **首次執行**: 在終端機中執行 `streamlit run app.py`。
4.2 **功能驗證**: - 測試所有側邊欄滑桿是否能正常運作並即時更新圖表。 - 確認模型評估指標是否會隨參數變動而刷新。 - 檢查資料下載按鈕功能是否正常。
4.3 **使用者體驗優化**: 加入「恢復預設值」按鈕，並美化介面排版。

# 5.0 文件撰寫 (Documentation)

5.1 **撰寫 README**: 建立 `README.md`，詳細說明專案功能、技術棧、安裝與執行步驟。
5.2 **建立 README**: 建立 `README.en.md` 以利協作。
5.3 **完成部署說明**: 建立 `ReplDeployment.md` (若有需要，用於說明更詳細的部署步驟)。
5.4 **專案完成**: 所有功能開發與文件撰寫完畢，建立 `AllDone.md` 標示專案完成。

# 6.0 專案完成

6.1 最終程式碼審查與確認。
6.2 專案交付。
