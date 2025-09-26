import streamlit as st

st.set_page_config(page_title="焼入深さ計算ツール", layout="centered")

# --- CSS ---
st.markdown("""
<style>
    input[type="text"] {
        font-size: 18px !important;
        padding: 10px !important;
    }
    div.stButton > button {
        width: 100%;
        height: 3em;
        font-size: 18px;
        border-radius: 8px;
    }
    .stAlert {
        font-size: 18px !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("📱 焼入深さ計算ツール")

# --- 初期化 ---
for key in ["limit_hardness", "d1", "h1", "d2", "h2"]:
    st.session_state.setdefault(key, "")

# --- リセットボタン ---
if st.button("🔄 リセット"):
    for key in ["limit_hardness", "d1", "h1", "d2", "h2"]:
        st.session_state[key] = ""   # 値を空に上書き
    st.rerun()                       # 再描画

# --- 入力欄 ---
limit_hardness = st.text_input("有効硬化層の限界硬さ", key="limit_hardness")
d1 = st.text_input("測定深さ d1", key="d1")
h1 = st.text_input("硬さ H1", key="h1")
d2 = st.text_input("測定深さ d2", key="d2")
h2 = st.text_input("硬さ H2", key="h2")

# --- 数値変換 ---
def to_float(x):
    try:
        return float(x)
    except:
        return None

limit_hardness_val = to_float(limit_hardness)
d1_val = to_float(d1)
h1_val = to_float(h1)
d2_val = to_float(d2)
h2_val = to_float(h2)

# --- 計算 ---
chd = None
if None not in [limit_hardness_val, d1_val, h1_val, d2_val, h2_val]:
    if (h1_val - limit_hardness_val) * (h2_val - limit_hardness_val) <= 0:
        chd = d1_val + (limit_hardness_val - h1_val) * (d2_val - d1_val) / (h2_val - h1_val)

# --- 出力 ---
st.subheader("📊 計算結果")
if chd is not None:
    st.success(f"焼入深さ = {chd:.2f}")  # ← 小数点2桁
elif all(st.session_state.get(k, "") == "" for k in ["limit_hardness","d1","h1","d2","h2"]):
    st.info("値を入力してください。")
else:
    st.warning("限界硬さを超えるデータが見つかりませんでした。")

