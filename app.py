import streamlit as st
import pandas as pd
import basehash
import os

from module.sidebar import sidebar

os.environ['STREAMLIT_THEME_BASE'] = 'light'

def run():
    st.set_page_config(page_title="海龟汤", page_icon="🎮", initial_sidebar_state="expanded") # collapsed, expanded
    col = st.columns((0.5,0.5,0.5,0.5))
    with col[0]:
        st.title("海龟汤")
    df = pd.read_excel("海龟汤_2.xlsx")
    q_total = df.shape[0]
    sidebar(q_total)
    
    with col[1]:
        st.header("")
        st.write("")
        st.write("总题库：", str(q_total))
    st.caption("⚠️以下内容纯属虚构，如有不适，请立即停止游戏。")
    
    col2 = st.columns([1,3])
    with col2[0]:
        input_code = st.text_input("Input your code:")
    with col2[1]:
        st.subheader("")
        st.write("")
        q_btn = st.button("提取")
        
    if input_code != "" or q_btn:
        hash_fn = basehash.base36()
        idx = hash_fn.unhash(input_code)
        
        try:
            title = df['title'][idx]
            ques = df['ques'][idx]
            ans = df['ans'][idx]
            st.header("题目：{}".format(title))
            st.subheader("汤面：")
            st.write(ques)
            st.write("")
            
            btn_col = st.columns((0.6,0.6,3))
            with btn_col[0]:
                ans_btn = st.button("解答")
            if ans_btn:
                with btn_col[1]:
                    undo_btn = st.button("收起")
                st.subheader("汤底：")
                st.write(ans)
                if undo_btn:
                    st.experimental_rerun()
        except:
            st.write("⚠️Error code. Please find your administrator to get the code.")
        
    
if __name__ == "__main__":
    run()
