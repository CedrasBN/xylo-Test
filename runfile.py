import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# profiling libraries
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import sweetviz as sv

st.set_page_config(page_title="EDA Workshop Dashboard", layout="wide")

st.title("EDA Workshop - Streamlit Version")

# equivalent to files.upload()
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # exclude y column
    if "y" in df.columns:
        df = df.drop(columns=["y"])

    st.header("Dataset Preview")
    st.dataframe(df.head())

    st.header("Dataset Info")
    st.write(df.shape)

    st.header("Summary Statistics")
    st.dataframe(df.describe())

    st.header("Missing Values")
    st.dataframe(df.isnull().sum())

    # -------------------------
    # Charts
    # -------------------------
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    if len(numeric_cols) > 0:

        st.subheader("Bar Chart")
        bar_col = st.selectbox("Select column for bar chart", numeric_cols)

        fig1, ax1 = plt.subplots()
        df[bar_col].value_counts().head(20).plot(kind="bar", ax=ax1)
        st.pyplot(fig1)

        st.subheader("Histogram")
        hist_col = st.selectbox("Select column for histogram", numeric_cols)

        fig2, ax2 = plt.subplots()
        df[hist_col].hist(ax=ax2)
        st.pyplot(fig2)

        st.subheader("Line Graph")
        line_col = st.selectbox("Select column for line graph", numeric_cols)

        fig3, ax3 = plt.subplots()
        df[line_col].plot(ax=ax3)
        st.pyplot(fig3)

    # -------------------------
    # YData Profiling
    # -------------------------
    st.header("YData Profiling Report")

    profile = ProfileReport(df, explorative=True)
    st_profile_report(profile)

    # -------------------------
    # Sweetviz Report
    # -------------------------
    st.header("Sweetviz Report")

    report = sv.analyze(df)
    report_html = "sweetviz_report.html"
    report.show_html(report_html)

    with open(report_html, "r", encoding="utf-8") as f:
        html = f.read()

    st.components.v1.html(html, height=800, scrolling=True)
