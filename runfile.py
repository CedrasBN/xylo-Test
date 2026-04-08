import streamlit as st
import pandas as pd
import sweetviz as sv

st.set_page_config(page_title="EDA App", layout="wide")

st.title("📊 Exploratory Data Analysis (EDA) App")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📌 Dataset Preview")
    st.dataframe(df.head())

    st.subheader("📊 Dataset Description")
    st.write(df.describe())

    st.subheader("ℹ️ Dataset Info")
    buffer = []
    df.info(buf=buffer)
    s = "\n".join(buffer)
    st.text(s)

    st.subheader("❌ Missing Values")
    st.write(df.isnull().sum())

    # YData Profiling Report
    st.subheader("📑 YData Profiling Report")


    with open("profile_report.html", "r", encoding="utf-8") as f:
        st.download_button("Download Profiling Report", f, file_name="EDA_report.html")

    # Sweetviz Report
    st.subheader("📈 Sweetviz Report")
    report = sv.analyze(df)
    report.show_html("sweetviz_report.html")

    with open("sweetviz_report.html", "r", encoding="utf-8") as f:
        st.download_button("Download Sweetviz Report", f, file_name="sweetviz_report.html")

else:
    st.info("👆 Please upload a CSV file to begin.")
