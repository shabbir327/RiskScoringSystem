import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#To run this app, use the command:
# streamlit run app.py

# ======================================================
# PAGE SETUP
# ======================================================
st.set_page_config(page_title="Supplier Risk Dashboard", layout="wide")
st.title("📊 Supplier Risk Scoring Dashboard")


# ======================================================
# LOAD DATA
# ======================================================
uploaded_file = st.file_uploader("Upload Supplier_KPI_Normalized_Final.csv", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    st.success("File loaded successfully!")

    required_cols = [
        "Supplier",
        "LDR_norm", "NRR_norm", "AD_norm",
        "LTR_norm", "FE_norm", "VSL_Risk_norm",
        "Supplier_Engagement_Level"
    ]

    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        st.error(f"Missing required columns: {missing}")
        st.stop()

    # ======================================================
    # KPI WEIGHTS INPUT (must total 1.0)
    # ======================================================
    st.header("⚙️ KPI Weights")

    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)

    w_LDR = col1.number_input("LDR Weight", 0.0, 1.0, 0.30)
    w_NRR = col2.number_input("NRR Weight", 0.0, 1.0, 0.25)
    w_AD  = col3.number_input("AD Weight", 0.0, 1.0, 0.15)

    w_LTR = col4.number_input("Lead Time Weight", 0.0, 1.0, 0.10)
    w_FE  = col5.number_input("Financial Exposure Weight", 0.0, 1.0, 0.10)
    w_VSL = col6.number_input("VSL Risk Weight", 0.0, 1.0, 0.10)

    weight_sum = w_LDR + w_NRR + w_AD + w_LTR + w_FE + w_VSL

    st.write(f"**Total Weight = {weight_sum:.2f}**")
    if abs(weight_sum - 1.0) > 0.0001:
        st.warning("⚠️ Weights must sum to 1.0")
        st.stop()

    # ======================================================
    # COMPUTE RISK SCORE
    # ======================================================
    df["Risk_Score"] = (
        df["LDR_norm"] * w_LDR +
        df["NRR_norm"] * w_NRR +
        df["AD_norm"]  * w_AD  +
        df["LTR_norm"] * w_LTR +
        df["FE_norm"]  * w_FE  +
        df["VSL_Risk_norm"] * w_VSL
    )

    # ======================================================
    # RISK COMMENT
    # ======================================================
    def risk_label(score):
        if score < 0.33:
            return "Low Risk"
        elif score < 0.66:
            return "Moderate Risk"
        else:
            return "High Risk"

    df["Risk_Comment"] = df["Risk_Score"].apply(risk_label)

    # ======================================================
    # FINAL OUTPUT TABLE
    # ======================================================
    st.header("📄 Supplier Risk Table")

    output_df = df[[
        "Supplier",
        "Supplier_Engagement_Level",
        "Risk_Score",
        "Risk_Comment"
    ]].sort_values(by="Risk_Score", ascending=False)

    st.dataframe(output_df, use_container_width=True)

else:
    st.info("👆 Upload your Supplier_KPI_Normalized_Final.csv to begin.")
