import streamlit as st
import pandas as pd
import joblib

# Load model
@st.cache_resource
def load_model():
    return joblib.load("D:\\House_predict\\bengaluru_price_model.pkl")

model = load_model()

# ---------------- UI ----------------
st.set_page_config(
    page_title="Bengaluru House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 Bengaluru House Price Prediction")
st.write("Nhập thông tin căn nhà để dự đoán giá (đơn vị **Lakh INR**)")

# -------- Input form --------
with st.form("prediction_form"):
    location = st.text_input("📍 Location", value="Whitefield")
    total_sqft = st.number_input("📐 Total Square Feet", min_value=300.0, max_value=10000.0, value=1200.0)
    bath = st.number_input("🛁 Number of Bathrooms", min_value=1.0, max_value=10.0, value=2.0)
    bhk = st.number_input("🛏️ Number of BHK", min_value=1.0, max_value=10.0, value=2.0)

    submitted = st.form_submit_button("🔮 Predict Price")

# -------- Prediction --------
if submitted:
    input_df = pd.DataFrame([{
        "location": location,
        "total_sqft": total_sqft,
        "bath": bath,
        "bhk": bhk
    }])

    try:
        prediction = model.predict(input_df)[0]

        st.success(f"💰 Giá nhà dự đoán: **{prediction:.2f} Lakh INR**")

        st.markdown("### 📊 Thông tin đầu vào")
        st.dataframe(input_df)

    except Exception as e:
        st.error("❌ Lỗi khi dự đoán")
        st.exception(e)
