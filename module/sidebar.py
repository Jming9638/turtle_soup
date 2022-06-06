import streamlit as st
from streamlit.components.v1 import html
import basehash
import time

def sidebar(q_total):
    hash_fn = basehash.base36()
    with st.sidebar:
        st.header("Code Generator")
        input_num = st.text_input("Please input an integer between 1 - {}.".format(q_total))
        if input_num != "":
            try:
                num = int(input_num)
                code_num = hash_fn.hash(num)
                st.write("Your code: {}".format(code_num))
                
            except:
                st.write("Please input a valid number.")
            