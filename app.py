import streamlit as st
import pandas as pd
import basehash

def run():
    st.title("海龟汤")
    df = pd.read_excel("海龟汤.xlsx")
    q_total = df.shape[0]
    st.write("总题库：", str(q_total))
    
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
        st.subheader("汤底：")
        st.write(ans)
        
    
if __name__ == "__main__":
    run()