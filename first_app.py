import streamlit as st
import pandas as pd

def main():
    st.title("First_APP")
    df=pd.Dataframe({
        "first_col":[1,2,3,4],
        "second_col":[100,20,30,40]
        
    })
    st.write(df)

if __name__=="__main__":
    main()    