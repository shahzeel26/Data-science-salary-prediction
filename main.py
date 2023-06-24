import streamlit as st
import pandas as pd
import numpy as np
from salary import prediction
from remove_outlier import remove_outlires
from encoder import Encoder

st.set_page_config(page_title='Data science salary prediction ', page_icon='📈', layout="centered", initial_sidebar_state="auto", menu_items=None)


def main_page():
   
    st.title('Data science salaru price prediction website ✅'    )
    st.sidebar.markdown("Data science salary prediction website ")
    st.write("Hello, Welcome to the Salary prediction website!")
    st.write("People can use this amazing website for predicting and analysing the salary price in different fields of data science for instance Machine learning, Data analyst, Data scientist, Artificial Intelligence....")
    st.write("Some can individiually predict salary on the bases of some perimeters.")

page_names_to_funcs = {
    "✅Main Page": main_page,
    "📈Delhi city's house price ": prediction,
    
    
}
selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()