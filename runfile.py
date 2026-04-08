import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="EDA Dashboard", layout="wide")

st.title("Exploratory Data Analysis Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Remove y column if present
    if 'y' in df.columns:
        df = df.drop(columns=['y'])

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Shape")
    st.write(df.shape)

    st.subheader("Summary Statistics")
    st.dataframe(df.describe())

    st.subheader("Missing Values")
    st.dataframe(df.isnull().sum())

    # Numeric columns only
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

    if len(numeric_cols) > 0:
        st.subheader("Bar Chart")

        col1 = st.selectbox("Select column for bar chart", numeric_cols)

        fig, ax = plt.subplots()
        df[col1].value_counts().head(20).plot(kind='bar', ax=ax)
        st.pyplot(fig)

        st.subheader("Histogram")

        col2 = st.selectbox("Select column for histogram", numeric_cols, key="hist")

        fig2, ax2 = plt.subplots()
        df[col2].hist(ax=ax2)
        st.pyplot(fig2)

        st.subheader("Line Graph")

        col3 = st.selectbox("Select column for line graph", numeric_cols, key="line")

        fig3, ax3 = plt.subplots()
        df[col3].plot(ax=ax3)
        st.pyplot(fig3)

    else:
        st.warning("No numeric columns available for plotting.")
