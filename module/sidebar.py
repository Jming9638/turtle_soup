import streamlit as st
from streamlit.components.v1 import html
import basehash
import random

if 'num' not in st.session_state:
    st.session_state['num'] = ""
if 'button' not in st.session_state:
    st.session_state['button'] = ""
if 'rancount' not in st.session_state:
    st.session_state['rancount'] = 0

def sidebar(q_total):
    hash_fn = basehash.base36()
    with st.sidebar:
        st.header("Code Generator")
        input_num = st.text_input("Please input an integer between 1 - {}.".format(q_total))
        st.session_state['num'] = input_num
        gen_col = st.columns((0.8,1.2,1))
        with gen_col[0]:
            gen_btn = st.button("生成")
        with gen_col[1]:
            ran_btn = st.button("随机生成")
            
        if gen_btn:
            st.session_state['button'] = "gen"
        else:
            pass
        
        ran_seq = st.session_state['rancount']
        if ran_btn:
            st.session_state['rancount'] += 1
            st.session_state['button'] = "ran"
        else:
            pass
            
        if st.session_state['button'] == "ran" and ran_seq < st.session_state['rancount']:
            num = random.randint(0, q_total)
            code_num = hash_fn.hash(num)
            st.markdown("Random code: **{}**".format(code_num), unsafe_allow_html=True)

        elif st.session_state['num'] != "" or st.session_state['button'] == "gen":
            try:
                num = int(st.session_state['num'])
                if num <= q_total and num > 0:
                    code_num = hash_fn.hash(num-1)
                    st.markdown("Your code: **{}**".format(code_num), unsafe_allow_html=True)
                else:
                    st.write("Your input number is out of the range.")
            except:
                st.write("Please input a valid number.")
        
        else:
            pass
        
        
        #-------------------Rules-------------------#
        st.subheader("游戏规则：")
        st.write("1、《海龟汤》是一款游戏，又叫“是否与此无关”，游戏方法非常简单，在任何地方都可以进行。")
        st.write("2、一开始由出题者给予一个不完整的故事，让猜题者提问各种可能性的问题。")
        st.write("3、出题者解答这些问题只能说「是」、「不是」或「与此无关」这些答案。")
        st.write("4、因此猜题者必须在有限的线索中推理出事件的始末，藉由限定性的问答拼凑出故事的全貌。")
            