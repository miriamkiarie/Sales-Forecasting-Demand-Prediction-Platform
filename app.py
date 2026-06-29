import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    layout="wide"
)

st.title("📈 Sales Forecasting Dashboard")
st.markdown("Upload a dataset to explore and analyze sales data.")

# -------------------------
# FILE UPLOAD
# -------------------------
uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

# -------------------------
# LOAD DATA
# -------------------------
if uploaded_file is not None:

    try:

        if uploaded_file.name.endswith(".csv"):

            encodings = ["utf-8", "latin1", "cp1252"]

            df = None

            for enc in encodings:
                try:
                    uploaded_file.seek(0)
                    df = pd.read_csv(uploaded_file, encoding=enc)
                    st.success(f"Dataset loaded using {enc}")
                    break
                except:
                    continue

            if df is None:
                st.error("Could not read CSV file.")
                st.stop()

        else:
            df = pd.read_excel(uploaded_file)
            st.success("Excel file loaded successfully")

        # -------------------------
        # DATA OVERVIEW
        # -------------------------
        st.header("Dataset Overview")

        col1, col2, col3 = st.columns(3)

        col1.metric("Rows", len(df))
        col2.metric("Columns", len(df.columns))
        col3.metric("Missing Values", int(df.isnull().sum().sum()))

        st.subheader("Preview")
        st.dataframe(df.head())

        # -------------------------
        # COLUMN INFO
        # -------------------------
        st.header("Column Information")

        info_df = pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str),
            "Missing Values": df.isnull().sum().values
        })

        st.dataframe(info_df)

        # -------------------------
        # SUMMARY STATS
        # -------------------------
        st.header("Summary Statistics")

        st.dataframe(df.describe(include="all"))

        # -------------------------
        # VISUALIZATION
        # -------------------------
        numeric_cols = df.select_dtypes(include="number").columns

        if len(numeric_cols) > 0:

            st.header("Visualization")

            selected_col = st.selectbox(
                "Select Numeric Column",
                numeric_cols
            )

            fig, ax = plt.subplots(figsize=(8, 4))

            df[selected_col].hist(ax=ax)

            ax.set_title(f"Distribution of {selected_col}")

            st.pyplot(fig)

        else:
            st.warning("No numeric columns available for visualization.")

    except Exception as e:
        st.error(f"Error loading file: {e}")

else:
    st.info("Upload a dataset to begin.")