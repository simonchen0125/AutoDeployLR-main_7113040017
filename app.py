import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt # 引入 altair 套件
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# --- 中文字體設定 ---
# 為了在 Matplotlib 中正確顯示中文，需要設定支援中文的字體。
# 'Microsoft JhengHei' 是 Windows 上的「微軟正黑體」。
# Altair 不需要此設定，但為了離群值分析的表格樣式保留 Matplotlib。
try:
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
except Exception as e:
    st.warning(f"Matplotlib 中文字體設定失敗，部分樣式可能無法正常顯示。錯誤訊息：{e}")


# --- 頁面設定 ---
st.set_page_config(
    page_title="互動式線性迴歸分析儀 (CRISP-DM)",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CRISP-DM 階段 1: 商業理解 (Business Understanding) ---
st.title("互動式線性迴歸分析儀")
st.markdown("""
### 專案目標 (商業理解)
本專案遵循 **CRISP-DM (跨產業資料探勘標準流程)** 的框架，旨在建立一個互動式工具，讓使用者可以直觀地理解簡單線性迴歸。

您可以透過左側的控制面板調整參數，觀察資料分佈、迴歸線擬合以及模型評估指標的即時變化，從而深入了解各項參數對模型的影響。
""")

# --- 側邊欄：參數控制 ---
st.sidebar.header("⚙️ 參數控制面板")

# 使用者可調整的參數
st.sidebar.markdown("### 1. 資料生成參數")

# 修正 #3：定義一個回呼函式來重設參數
def reset_parameters():
    st.session_state.n_points_slider = 300
    st.session_state.coefficient_a_slider = -5.0
    st.session_state.noise_variance_slider = 50.0

# 透過 key 來讓滑桿記住自己的狀態
n_points = st.sidebar.slider("資料點數量 (n)", min_value=100, max_value=2000, value=300, step=100, key='n_points_slider')
coefficient_a = st.sidebar.slider("真實斜率 (a)", min_value=-20.0, max_value=20.0, value=-5.0, step=0.1, key='coefficient_a_slider')
coefficient_b = 5.0
st.sidebar.info(f"註：真實截距 (b) 固定為 {coefficient_b}。")
noise_variance = st.sidebar.slider("雜訊變異數 (Noise Variance)", min_value=0.0, max_value=500.0, value=50.0, step=5.0, key='noise_variance_slider')

# 修正 #3：將回呼函式綁定到按鈕的 on_click 事件
st.sidebar.button("🔄 恢復預設值", on_click=reset_parameters)


# --- CRISP-DM 階段 2 & 3: 資料理解與準備 (Data Understanding & Preparation) ---
st.markdown("---")
st.header("📊 資料理解與準備")
st.write(f"我們將根據公式 `y = {coefficient_a:.1f} * x + {coefficient_b:.1f} + noise` 來生成資料。")

# 生成資料
np.random.seed(42)
x = np.random.rand(n_points) * 10
y_true = coefficient_a * x + coefficient_b
noise = np.random.normal(0, np.sqrt(noise_variance), n_points)
y = y_true + noise

df = pd.DataFrame({'x': x, 'y': y, 'y_true': y_true})

if st.checkbox("顯示生成的資料預覽 (前 5 筆)"):
    st.dataframe(df.head())

@st.cache_data
def convert_df_to_csv(df_to_convert):
    return df_to_convert.to_csv(index=False).encode('utf-8')

csv = convert_df_to_csv(df)

st.download_button(
   label="📥 下載生成的資料 (CSV)",
   data=csv,
   file_name='generated_regression_data.csv',
   mime='text/csv',
)


# --- CRISP-DM 階段 4: 模型建立 (Modeling) ---
st.markdown("---")
st.header("🤖 模型建立")
st.write("我們選用 **簡單線性迴歸 (Simple Linear Regression)** 模型，來學習 `x` 與 `y` 之間的關係。")

model = LinearRegression()
X = x.reshape(-1, 1)
model.fit(X, y)
y_pred = model.predict(X)

df['predicted_y'] = y_pred
df['residuals'] = np.abs(y - y_pred)

col1, col2 = st.columns(2)
with col1:
    st.metric(label="模型學到的斜率 (Coefficient)", value=f"{model.coef_[0]:.2f}",
              delta=f"{model.coef_[0] - coefficient_a:.2f} (與真實值差異)")
with col2:
    st.metric(label="模型學到的截距 (Intercept)", value=f"{model.intercept_:.2f}",
              delta=f"{model.intercept_ - coefficient_b:.2f} (與真實值差異)")


# --- CRISP-DM 階段 5: 評估 (Evaluation) ---
st.markdown("---")
st.header("📈 評估")

# 使用分頁 (Tabs) 來組織評估內容
tab1, tab2, tab3 = st.tabs(["📊 視覺化評估 (互動圖表)", "🔢 量化指標", "🧐 離群值分析"])

with tab1:
    st.subheader("互動式圖表")
    
    # 將 DataFrame 轉換為適合 Altair 的格式
    source = df.copy()
    
    # 建立散佈圖
    scatter_plot = alt.Chart(source).mark_circle(size=60, opacity=0.6).encode(
        x=alt.X('x', title='X 變數'),
        y=alt.Y('y', title='Y 變數'),
        tooltip=['x', 'y', 'residuals']
    ).interactive() # 啟用互動功能

    # 建立迴歸線
    regression_line = alt.Chart(source).mark_line(color='red', size=3).encode(
        x='x',
        y='predicted_y'
    )

    # 建立真實關係線
    true_line = alt.Chart(source).mark_line(color='green', strokeDash=[5,5], size=2).encode(
        x='x',
        y='y_true'
    )
    
    # 組合圖表
    chart = (scatter_plot + regression_line + true_line).properties(
        title='線性迴歸模型擬合結果'
    )
    
    st.altair_chart(chart, use_container_width=True)

with tab2:
    st.subheader("量化指標評估")
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    st.metric(label="均方誤差 (MSE)", value=f"{mse:.2f}")
    st.markdown("MSE 衡量預測值與真實值的平均平方差異，越小越好。")
    st.metric(label="R 平方 (R-squared)", value=f"{r2:.3f}")
    st.markdown("R² 表示模型能解釋 y 變異的百分比，越接近 1 越好。")

with tab3:
    st.subheader("離群值分析")
    st.write("離群值是距離迴歸線最遠的資料點，它們可能會對模型的準確性產生較大影響。")
    outliers = df.nlargest(5, 'residuals')
    st.dataframe(outliers[['x', 'y', 'predicted_y', 'residuals']].style.background_gradient(cmap='Reds', subset=['residuals']))


# --- CRISP-DM 階段 6: 部署 (Deployment) ---
st.markdown("---")
st.header("🚀 部署")
st.success("""
這個 Streamlit 應用程式本身就是 **部署 (Deployment)** 階段的成果。

我們已將一個資料分析流程打包成一個互動式的 Web 應用，讓使用者可以輕鬆地進行操作與探索。
""")

