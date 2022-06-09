from audioop import mul
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
if 'multicount' not in st.session_state:
    st.session_state['multicount'] = 0
if 'multicode' not in st.session_state:
    st.session_state['multicode'] = ""

def sidebar(q_total):
    hash_fn = basehash.base36()
    with st.sidebar:
        st.header("Code Generator")
        gen_mode = st.radio(label="Generator Mode", options=("单个生成", "多个生成"), horizontal=True)
        
        if gen_mode == "单个生成":
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
        
        elif gen_mode == "多个生成":
            multi_col = st.columns((2,1))
            with multi_col[0]:
                gen_input = st.number_input("生成数：", min_value=2, max_value=15, step=1)
            with multi_col[1]:
                st.subheader("")
                st.write("")
                multi_btn = st.button("生成")
                
            multi_seq = st.session_state['multicount']
            if multi_btn:
                st.session_state['multicount'] += 1
            else:
                pass
                
            if gen_input is not None and multi_seq < st.session_state['multicount']:
                rand_list = random.sample(range(q_total), gen_input)
                encoded_list = []
                for randnum in rand_list:
                    hash_fn = basehash.base36()
                    hash_value = hash_fn.hash(randnum)
                    encoded_list.append(hash_value)
                    
                str_list = ", ".join(encoded_list)
                st.session_state['multicode'] = str_list
                st.markdown("Your code list: **{}**".format(st.session_state['multicode']), unsafe_allow_html=True)
                
            elif gen_input is not None and multi_seq == st.session_state['multicount'] and multi_seq > 0:
                st.markdown("Your code list: **{}**".format(st.session_state['multicode']), unsafe_allow_html=True)
                
            else:
                pass
        
        #-------------------Rules-------------------#
        st.subheader("游戏规则：")
        st.write("1、《海龟汤》是一款游戏，又叫“是否与此无关”，游戏方法非常简单，在任何地方都可以进行。")
        st.write("2、一开始由出题者给予一个不完整的故事，让猜题者提问各种可能性的问题。")
        st.write("3、出题者解答这些问题只能说「是」、「不是」或「与此无关」这些答案。")
        st.write("4、因此猜题者必须在有限的线索中推理出事件的始末，藉由限定性的问答拼凑出故事的全貌。")
        st.write(" ")
        foot_col = st.columns((0.5,1.2,0.5))
        with foot_col[1]:
            st.write("-------规则结束-------")
