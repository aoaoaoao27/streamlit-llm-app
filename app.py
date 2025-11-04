###
# Load environment variables from a .env file
###
import re
from dotenv import load_dotenv
load_dotenv()

###
# llm
###
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def invoke_question(role, user_query):
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "あなたは{role}です。質問に対して初心者にも分かりやすく簡潔に答えてください。専門外の質問には答えないでください。"),
        ("human", "{user_query}")
    ])

    chain = prompt | llm | StrOutputParser()
    result = chain.invoke({"role": role, "user_query": user_query})

    return result

###
# Streamlit
###
import streamlit as st

st.title("LLMなWebアプリ")

st.write("このアプリは、異なる専門分野のLLM（大規模言語モデル）を利用して、ユーザーの質問に答えることができます。")
st.write("##### 動作モード1: 医療の専門家")
st.write("LLMは、医療の専門家として振る舞い舞ます。患者の症状に基づいて、適切な診断と治療法を提案します。")
st.write("##### 動作モード2: 法律の専門家")
st.write("LLMは、法律の専門家として振る舞い舞ます。クライアントの法的な質問に対して、適切なアドバイスを提供します。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["医療の専門家", "法律の専門家"]
)

st.divider()

input_message = st.text_input(label="質問を入力してください。")

if st.button("Submit"):
    st.divider()

    if input_message:
        if selected_item == "医療の専門家":
            result = invoke_question(selected_item, input_message)
            st.write("医学の専門家としての応答:")
            st.write(f"{result}")

        else:
            result = invoke_question(selected_item, input_message)
            st.write("法律の専門家としての応答:")
            st.write(f"{result}")

    else:
        st.error("質問を入力してから「Submit」ボタンを押してください。")
