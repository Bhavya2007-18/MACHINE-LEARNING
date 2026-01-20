import streamlit as st
import sys
import os

# Add the prakhar folder to Python path so we can import from it
sys.path.append(os.path.join(os.path.dirname(__file__), 'prakhar/converted_scripts/dataVisualization'))

# Now import your friend's EDA functions
try:
    from eda import *  # Import all functions from eda.py
    # OR import specific functions if you know them:
    # from eda import plot_distribution, plot_correlation, generate_summary
except ImportError as e:
    st.error(f"Import error: {e}. Check the file path.")
    st.stop()

# App title
st.title("📊 EDA Dashboard")
st.markdown("Interactive interface for exploratory data analysis")

# 1. FILE UPLOADER
uploaded_file = st.file_uploader("Upload your dataset (CSV or Excel)", type=['csv', 'xlsx'])

if uploaded_file is not None:
    # Load data based on file type
    import pandas as pd
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
    st.success(f"✅ Loaded {uploaded_file.name} with {df.shape[0]} rows and {df.shape[1]} columns")
    
    # 2. DATA PREVIEW
    st.subheader("Data Preview")
    show_preview = st.checkbox("Show first 10 rows", value=True)
    if show_preview:
        st.dataframe(df.head(10))
    
    # 3. COLUMN SELECTOR FOR ANALYSIS
    st.subheader("Column Selection")
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    
    col1, col2 = st.columns(2)
    with col1:
        if numeric_cols:
            selected_num = st.multiselect("Numeric columns for analysis:", numeric_cols, default=numeric_cols[:2])
    with col2:
        if categorical_cols:
            selected_cat = st.selectbox("Categorical column (for grouping):", ['None'] + categorical_cols)
    
    # 4. ANALYSIS CONTROLS
    st.subheader("Analysis Controls")
    
    # You'll need to know what functions are available in eda.py
    # Example: if eda.py has a function plot_histogram(data, column)
    if st.button("Run Basic EDA", type="primary"):
        st.info("Running analysis...")
        
        # Call functions from eda.py
        try:
            # Example 1: Show basic statistics
            st.write("### Basic Statistics")
            st.write(df[selected_num].describe() if selected_num else df.describe())
            
            # Example 2: Create visualizations
            # If eda.py has a plot_distribution function:
            # fig = plot_distribution(df, selected_num[0])
            # st.pyplot(fig)
            
            # For now, show a sample plot using Streamlit
            if selected_num:
                st.write("### Distribution Plot")
                st.bar_chart(df[selected_num[:2]])  # Simple placeholder
                
        except Exception as e:
            st.error(f"Analysis error: {e}")
    
    # 5. DOWNLOAD OPTIONS
    st.subheader("Export Results")
    if st.button("Generate Report"):
        # You can create a summary report here
        st.download_button(
            label="Download Summary",
            data=df.describe().to_csv(),
            file_name="eda_summary.csv",
            mime="text/csv"
        )

else:
    st.info("👆 Please upload a dataset to begin analysis")
    # Show sample option
    if st.button("Use sample data for testing"):
        # Load sample data
        import pandas as pd
        df = pd.DataFrame({
            'A': range(100),
            'B': range(100, 200),
            'category': ['X', 'Y'] * 50
        })
        st.session_state['df'] = df
        st.rerun()
