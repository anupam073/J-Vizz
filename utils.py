import streamlit as st

def dev_details():
    for _ in range(18):
        st.sidebar.text("")
    st.sidebar.markdown(
        f"<div align = 'center'><h3 style='text-align: center;'>Conncet with me on <a href = 'https://github.com/anupam073'> GitHub </a> & <a href='http://kaggle.com/sagnik1511'> Kaggle </a></h3></div>",
        unsafe_allow_html=True)


description_text = "J-vizz  expects it becoming a basic data visualization tool to be used by every data wrangler " \
                    "To get to know the basic quality and the features summary of the data by a eagle's view."\
                    " It also expects to save time from the most boring phase of every data wrangler that is data visualization "\
                    "and EDA. Hope this helps you."



