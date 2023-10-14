import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title='Dashboard📊')
st.title('Dashboard📊')

uploaded_file = st.file_uploader('Choose CSV or XLSX File', type=['xlsx', 'csv'])
if uploaded_file:
    st.markdown('---')
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.dataframe(df)

    groupby_column = st.selectbox(
        'What would you like to analyze?',
        df.columns
    )

    # Bar Chart
    st.subheader('Bar Chart')
    df_grouped = df.groupby(groupby_column).size().reset_index(name='Count')
    fig_bar = px.bar(
        df_grouped,
        x=groupby_column,
        y='Count',
        template='plotly_white'
    )
    st.plotly_chart(fig_bar)

    # Pie Chart
    df_grouped['Count'] = df.groupby(groupby_column)[groupby_column].transform('size')
    df_grouped['Label'] = df_grouped[groupby_column].astype(str) + ' (' + df_grouped['Count'].astype(str) + ')'
    st.subheader('Pie Chart')
    fig_pie = px.pie(
        df_grouped,
        names='Label',
        values='Count',
        template='plotly_white'
    )
    st.plotly_chart(fig_pie)
    
    # Box Plot
    st.subheader('Box Plot')
    x_variable_boxplot = st.selectbox('Select X Variable:', df.columns, key='x_variable_boxplot')
    y_variable_boxplot = st.selectbox('Select Y Variable:', df.columns, key='y_variable_boxplot')
    fig_boxplot = px.box(
        df,
        x=x_variable_boxplot,
        y=y_variable_boxplot,
        color=df[groupby_column],
        template='plotly_white',
        height=600,
        width=800 
    )
    st.plotly_chart(fig_boxplot)

    # Scatter Plot 
    st.subheader('Scatter Plot')
    x_variable_scatter = st.selectbox('Select X Variable:', df.columns)
    y_variable_scatter = st.selectbox('Select Y Variable:', df.columns)
    fig_scatter = px.scatter(
        df,
        x=x_variable_scatter,
        y=y_variable_scatter,
        color=df[groupby_column],
        template='plotly_white',
        height=600,
        width=800
    )
    st.plotly_chart(fig_scatter)
