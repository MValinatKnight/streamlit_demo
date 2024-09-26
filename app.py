import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the App
st.title('Cool Streamlit Data App')

# Upload CSV Data
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the data into a dataframe
    df = pd.read_csv(uploaded_file)

    # Show raw data
    st.subheader('Raw Data')
    st.write(df.head(10))

    # Basic Stats
    st.subheader('Basic Statistics')
    st.write(df.describe(include="all"))

    # null percentage
    st.subheader('Missing Values %')
    st.write((df.isnull().sum() / len(df)) * 100)

    # Data visualization
    st.subheader('Data Visualization')

    # Choose plot type
    plot_type = st.selectbox("Select the type of plot:", ["Scatter Plot", "Line Plot"])

    # if plot_type == "Correlation Heatmap":
    #     st.subheader('Correlation Heatmap')
    #     fig, ax = plt.subplots(figsize=(10, 6))
    #     sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
    #     st.pyplot(fig)

    if plot_type == "Scatter Plot":
        st.subheader('Scatter Plot')
        x_axis = st.selectbox('X-Axis', df.columns)
        y_axis = st.selectbox('Y-Axis', df.columns)
        fig, ax = plt.subplots()
        ax = sns.regplot(x=df[x_axis], y=df[y_axis])
        st.pyplot(fig)

    elif plot_type == "Line Plot":
        st.subheader('Line Plot')
        column = st.selectbox("Select column to plot", df.columns)
        fig, ax = plt.subplots()
        ax.plot(df[column])
        st.pyplot(fig)
else:
    st.write("Upload a CSV file to get started!")

# Footer
st.markdown("""
    *Created with* **Streamlit**  
""")
