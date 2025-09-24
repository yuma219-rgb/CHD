import streamlit as st

st.title("有効硬化層深さ (CHD) 計算ツール")

# --- 入力欄 ---
limit_hardness = st.number_input("有効硬化層の限界硬さ", value=450)

# データ入力（例：2点）
d1 = st.number_input("測定深さ d1", value=0.7, format="%.3f")
h1 = st.number_input("硬さ H1", value=341.0, format="%.1f")
d2 = st.number_input("測定深さ d2", value=0.5, format="%.3f")
h2 = st.number_input("硬さ H2", value=518.0, format="%.1f")

# --- 計算 ---
chd = None
if (h1 - limit_hardness) * (h2 - limit_hardness) <= 0:
    # 線形補間で CHD を算出
    chd = d1 + (limit_hardness - h1) * (d2 - d1) / (h2 - h1)

# --- 出力 ---
st.subheader("計算結果")
if chd is not None:
    st.success(f"CHD = {chd:.4f}")
else:
    st.warning("限界硬さを超えるデータが見つかりませんでした。")
