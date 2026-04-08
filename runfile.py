import streamlit as st
import pandas as pd
import sweetviz as sv

st.set_page_config(page_title="EDA Dashboard", layout="wide")

st.title("EDA Workshop - Streamlit Dashboard")

# Upload (replacement for files.upload())
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # remove y column
    if "y" in df.columns:
        df = df.drop(columns=["y"])

    # -----------------------
    # Tables
    # -----------------------
    st.header("Dataset Preview")
    st.dataframe(df.head())

    st.header("Dataset Shape")
    st.write(df.shape)

    st.header("Summary Statistics")
    st.dataframe(df.describe())

    st.header("Missing Values")
    st.dataframe(df.isnull().sum())

    # -----------------------
    # Sweetviz Visualization
    # -----------------------
    st.header("Sweetviz Report")

    report = sv.analyze(df)
    report_path = "sweetviz_report.html"
    report.show_html(report_path)

    with open(report_path, "r", encoding="utf-8") as f:
        html = f.read()

    st.components.v1.html(html, height=900, scrolling=True)
