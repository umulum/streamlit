##### 기본 정보 불러오기 #####
import streamlit as st
import openai
import os
import base64
API_KEY= "API_KEY"

#### 기능 구현 함수 정리 #####
def askGpt(question):
    client = openai.OpenAI(api_key=API_KEY)
    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=question)
    return response.choices[0].message.content


# STT
def STT(audio_value):
    client = openai.OpenAI(api_key=OPENAI_API)
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_value,
        response_format="text"
    )
    return transcript

# TTS
def TTS(response):
    client = openai.OpenAI(api_key=OPENAI_API)
    # TTS를 활용하여 만든 음성을 파일로 저장
    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="onyx",
        input=response
    ) as audio_response:
        filename = "output.mp3"
        audio_response.stream_to_file(filename)

    # 저장한 음성 파일을 자동 재생
    with open(filename, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay="True">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

    # 폴더에 남지 않도록 파일을 삭제
    os.remove(filename)

##### 메인 함수 #####
def main():
    st.set_page_config(page_title="AI 음성 비서", layout="wide")
    st.title('AI 음성 비서')
    st.markdown('---')

    if "messages" not in st.session_state:
        st.session_state.messages = []

    col1, col2 = st.columns(2)
    with col1:
        audio_value = st.audio_input("음성 메시지를 녹음하세요")

    with col2:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if audio_value:
            with st.chat_message("user"):
                user_ask_text = STT(audio_value)
                st.markdown(user_ask_text)
                st.session_state.messages.append({"role": "user", "content": user_ask_text})
            with st.chat_message("assistant"):
                response = askGpt(st.session_state.messages)
                TTS(response)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

if __name__=="__main__":
    main()
