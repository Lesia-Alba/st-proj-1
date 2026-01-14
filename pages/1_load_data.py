import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


uploaded_file = st.file_uploader(
        "Загрузите файл в формате CSV", 
        type=['csv']
)

if uploaded_file:
    df = pd.read_scv(uploaded_file)
    dfs ={ "male": df[df['customer_gender'] == 'male'],
          "female": df[df['customer_gender'] == 'female']
    }

    for title, data in dfs.items():
        data.drop(columns=['customer_gender'], inplace = True)
        st.subheader("Данные")
        st.dataframe(df)

    st.subheader("Распределение по возрасту у мужчин")    
    fig, ax = plt.subplots()
    ax.hist(dfs["male"]["customer_age"])
    ax.set_title("Распределение по возрасту у мужчин")
    st.pyplot(fig)

    st.bar_chart(data=dfs["male"], x=["country"], y=["customer_age"])

    f_df = dfs["female"]
    st.line_chart(data=f_df[f_df["revenue"] > 1000], x=["customer_age"], y=["revenue"])








