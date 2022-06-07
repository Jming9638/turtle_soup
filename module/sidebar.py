import streamlit as st
from streamlit.components.v1 import html
import basehash
import time

def sidebar(q_total):
    hash_fn = basehash.base36()
    with st.sidebar:
        st.header("Code Generator")
        input_num = st.text_input("Please input an integer between 1 - {}.".format(q_total))
        gen_col = st.columns((0.8,2))
        with gen_col[0]:
            gen_btn = st.button("生成")
            
        if input_num != "" or gen_btn:
            try:
                num = int(input_num)
                if num <= q_total and num > 0:
                    code_num = hash_fn.hash(num-1)
                    with gen_col[1]:
                        st.markdown("Your code: **{}**".format(code_num), unsafe_allow_html=True)
                else:
                    with gen_col[1]:
                        st.write("Your input number is out of the range.")
            except:
                with gen_col[1]:
                    st.write("Please input a valid number.")
                
        st.subheader("游戏规则：")
        st.write("1、《海龟汤》是一款游戏，又叫“是否与此无关”，游戏方法非常简单，在任何地方都可以进行。")
        st.write("2、一开始由出题者给予一个不完整的故事，让猜题者提问各种可能性的问题。")
        st.write("3、出题者解答这些问题只能说「是」、「不是」或「与此无关」这些答案。")
        st.write("4、因此猜题者必须在有限的线索中推理出事件的始末，藉由限定性的问答拼凑出故事的全貌。")
            