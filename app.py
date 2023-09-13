import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from io import StringIO
from pandasai.llm import OpenAI

llm = OpenAI(api_token="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", enable_cache=False)

uploaded_file = st.file_uploader("Upload a CSV for Natural Language Data Analysis and Visualization", type='csv')
if uploaded_file is not None:

    dataframe = pd.read_csv(uploaded_file, index_col=0)
    st.write(dataframe)
    dataframe = SmartDataframe(dataframe, config={"llm": llm, "enable_cache":False})

    prompt = st.chat_input("Ask question about the dataset or prompt instructions to make graphs.")
    if prompt:
        with st.chat_message("user"):
            st.write(f"{prompt}")

    with st.chat_message("assistant"):
        ans = dataframe.chat(prompt)
        if ans == None:
            # Change path according to local directory
            st.image("/Users/shubham/Documents/Slidey/slidey_demo/exports/charts/temp_chart.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        else:
            st.write(ans)
    # dataframe.chat(prompt)

    