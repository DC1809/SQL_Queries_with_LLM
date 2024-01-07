import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.title("Aura_Merchandise: Database Q&A 👕")

# Main layout
question = st.text_input("Question:", placeholder="E.g., How many Adidas products are in stock?")
if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)

 