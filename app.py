import streamlit as st
import pandas as pd
import basehash

def run():
    st.set_page_config(page_title="海龟汤", page_icon="🎮")
    col = st.columns((0.5,0.5,0.5,0.5))
    with col[0]:
        st.title("海龟汤")
    df = pd.read_excel("海龟汤.xlsx")
    q_total = df.shape[0]
    with col[1]:
        st.header("")
        st.write("")
        st.write("总题库：", str(q_total))
    st.caption("⚠️以下内容纯属虚构，如有不适，请立即停止游戏。")
    
    hash_fn = basehash.base36()
    input_code = st.text_input("Input your code:")
    
    if input_code != "":
        idx = hash_fn.unhash(input_code)
        title = df['title'][idx]
        ques = df['question'][idx]
        ans = df['answer'][idx]
        st.header("题目：{}".format(title))
        st.subheader("汤面：")
        st.write(ques)
        st.write("")
        
        ans_btn = st.button("解答")
        if ans_btn:
            st.subheader("汤底：")
            st.write(ans)
        
    
if __name__ == "__main__":
    run()