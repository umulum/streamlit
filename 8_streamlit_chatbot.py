##### 기본 정보 불러오기 #####
import streamlit as st
import openai
API_KEY = "" # API 키 입력

#### 기능 구현 함수 정리 #####
def askGpt(question):
    client = openai.OpenAI(api_key = API_KEY)
    response = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=question)
    return response.choices[0].message.content

##### 메인 함수 #####
def main():
    st.title('AI 챗봇 만들기')
    st.markdown('---')

    if "messages" not in st.session_state:
        st.session_state.messages =[]
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("채팅을 입력하세요")
    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("assistant"):
            response = askGpt(st.session_state.messages)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
    print(st.session_state.messages)

if __name__=="__main__":
    main()
