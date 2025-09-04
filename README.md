# Streamlit TIL
이 저장소는 Streamlit을 체계적으로 학습할 수 있도록 구성된 예제 모음입니다. 기본 기능부터 실전 대시보드와 챗봇 애플리케이션까지 단계별로 학습한 내용을 정리하였습니다. 
각 예제를 실행하려면 터미널에서 다음 명령어를 사용하세요:
```
streamlit run 0_streamlit_demo.py
```

### requirements.txt
```
koreanize-matplotlib==0.1.1
matplotlib==3.10.6
numpy==2.3.2
openai==1.105.0
pandas==2.3.2
plotly==6.3.0
scikit-learn==1.7.1
scipy==1.16.1
seaborn==0.13.2
streamlit==1.49.1
```

## 0_streamlit_demo.py (기본 함수)
이 파일은 Streamlit의 다양한 핵심 기능을 실습하는 예제입니다.  
텍스트 표시부터 사용자 입력 위젯, 데이터 처리까지 Streamlit 앱을 구성하는 데 필요한 기본 요소들을 폭넓게 다룹니다. 

1. 텍스트 표시   
    - `st.tltle`, `st.header`, `st.subheader`: 제목, 헤더, 서브헤더 등 다양한 크기의 텍스트 표시   
    - `st.markdown`: Markdown을 사용하여 볼드체, 기울임, 링크, 이모지, 테이블 등 디양한 스타일 적용   
    - `st.caption`, `st.text`, `st.write`: 기타 텍스트 표시 함수   
    - `st.code`: 코드 블록   
    - `st.latex`: 수학 공식   
 
2. 텍스트 입력   
    - `st.text_input`: 짧은 텍스트 입력  
    - `st.text_area`: 긴 텍스트 입력   
    - `st.number_input`: 숫자 입력 (-, +)   
    - `st.date_input`: 날짜 입력 (달력 형식)   

3. 선택형 위젯   
    - `st.selectbox`: 단일 항목 선택 드롭다운   
    - `st.multiselect`: 여러 항목 선택 드롭다운    
    - `st.radio`: 단일 항목 선택 라디오 버튼   
  
4. 버튼 및 슬라이더:    
    - `st.button`: 클릭 이벤트 처리   
    - `st.slider`: 값을 직관적으로 조절    

5. 파일 및 데이터 처리:    
    - `st.file_uploader`: CSV 또는 Excel 파일 업로드   


## 1_streamlit_graph.py (차트 시각화)
이 파일은 Streamlit에서 다양한 차트 라이브러리를 활용하여 데이터를 시각화하는 방법을 보여줍니다.
 
- `st.line_chart`, `st.bar_chart`, `st.area_chart`: pandas DataFrame을 기반으로 빠르게 차트 생성  
- `st.pyplot`: Matplotlib 및 Seaborn으로 만든 정적인 그래프를 Streamlit 앱에 표시   
- `st.plotly_chart`: Plotly로 만든 동적인 대화형 차트 생성  

## 2_streamlit_mbti.py (웹사이트 제작 실습) 
이 파일은 Streamlit을 활용하여 간단한 MBTI 성격 테스트 웹 애플리케이션을 만드는 예제입니다.  
사용자 상호작용과 세션 상태 관리를 통해 동적인 테스트 기능을 구현합니다.

- 질문 및 답변: E/I, S/N, T/F, J/P의 4가지 유형을 결정하는 질문과 답변  
- 커스텀 CSS: 배경색과 카드 스타일의 질문 UI, 그리고 버튼 애니메이션 등 커스텀 CSS 적용  
- 진행 상황: `st.progress`를 사용해 테스트 진행률을 시각적으로 표시   
- 레이아웃: `st.columns`를 활용하여 질문 옵션 버튼을 두 개의 열로 배치   
- 세션 상태 관리: `st.session_state`를 사용하여 사용자의 답변을 저장하고, 테스트가 끝난 후 결과 계산   
- 결과 출력: 사용자의 MBTI 유형에 대한 설명과 약점 정보 표시   
- 테스트 초기화: '테스트 다시 시작' 버튼을 누르면 모든 질문과 답변 초기화   

## 3_streamlit_layout.py  (레이아웃 구성)
이 파일은 Streamlit의 다양한 레이아웃 기능을 활용하여 웹 앱의 시각적 구조를 구성하는 방법을 보여줍니다. 

- `st.columns`: 페이지를 여러 개의 세로 열로 나누어 콘텐츠를 나란히 배치
- `st.expander`: 클릭하면 내용을 펼치거나 접을 수 있는 섹션 생성
- `st.tabs`: 클릭으로 전환할 수 있는 여러 개의 탭 생성 
- `st.sidebar`: 웹 앱의 왼쪽에 별도의 사이드바를 만들어 사용자가 메인 콘텐츠에 영향을 주지 않고 옵션을 조작할 수 있도록 함

## 4_streamlit_page (페이지 구성) 
이 폴더는 Streamlit의 새로운 멀티 페이지 기능을 활용하여 여러 페이지로 구성된 웹 애플리케이션을 만드는 방법을 보여줍니다.     
`entrypoint.py` 파일을 실행하면 앱의 시작점이 되며, 다른 페이지 파일로 쉽게 이동할 수 있는 내비게이션 기능을 제공합니다.   

1. `entrypoint.py`: 앱의 시작점, `st.Page()`를 사용해 페이지 정의, `st.navigation()`을 통해 페이지 선택 내비게이션 바 제공     
2. `home.py`: 앱의 메인 화면, 앱에 대한 전반적인 소개와 환영 메시지 표시    
3. `production.py`: 생산 데이터 분석 페이지, 생산량, 가동 시간 등의 예시 데이터를 `st.dataframe`과 `st.bar_chart`로 시각화     
4. `quality.py`: 품질 관리 페이지, Matplotlib을 사용하여 불량률 데이터의 분포를 히스토그램으로 시각화  
5. `maintenance.py`: 유지 보수 페이지, 설비 데이터 분석을 통한 고장 예측 모델의 개념 설명
6. `.streamlit/config.toml`: 테마와 서버 설정을 커스텀하는 파일로, 배경색, 폰트, 포트 번호 등을 변경하여 앱의 디자인 변경


## 5_streamlit_session.py (세션 상태 관리) 
이 파일은 Streamlit의 세션 상태를 사용하여 사용자의 상호작용 결과를 유지하는 방법을 보여줍니다.   
Streamlit은 사용자가 위젯을 조작할 때마다 스크립트 전체를 다시 실행(rerun)하는 방식으로 동작하므로, 세션 상태를 사용하지 않으면 변수 값이 매번 초기화됩니다. 

- `st.session_state`: 브라우저(사용자)마다 서로 다른 상태를 유지할 수 있게 해주는 저장 공간으로, 사용자가 입력한 값이나 버튼을 몇 번 눌렀는지 같은 정보를 계속 기억함

버튼 클릭 횟수를 표시하고 싶을 때, `st.session_state`를 사용하지 않고 변수를 선언하면, 버튼을 클릭할 때마다 값이 0으로 초기화됩니다.   
`st.session_state.count`와 같이 세션 상태에 변수를 저장하면, 버튼을 클릭해 앱이 다시 실행되어도 값이 유지됩니다.

사용자 입력, 클릭 횟수, 게임 점수 등 사용자의 상태를 기억해야 하는 앱을 만들 때 필수적인 기능입니다.


## 6_streamlit_caching.py (캐싱을 통한 성능 최적화)
이 파일은 Streamlit의 캐싱(Caching) 기능을 사용하여 앱의 성능을 최적화하는 방법을 보여줍니다.      
계산 비용이 큰 함수를 실행할 때 st.cache_data 데코레이터를 사용하면, 동일한 입력 값에 대해 함수를 다시 호출하지 않고 캐시된 결과를 즉시 반환하여 앱의 실행 속도를 크게 개선할 수 있습니다.

- `@st.cache_data` / `st.cache`: 연산 결과를 저장해두었다가, 같은 입력으로 다시 함수를 부르면 이미 계산해 둔 결과를 바로 가져오는 기능

`expensive_computation1` 함수는 매번 실행될 때마다 3초의 지연 시간을 가집니다. 동일한 값을 선택하고 Compute 버튼을 눌러도 매번 다시 계산하여 같은 지연 시간이 발생합니다.      
`st.cache_data` 데코레이터가 적용된 `expensive_computation2` 함수는 한 번 계산된 결과를 캐시 메모리에 저장합니다. 따라서 동일한 값을 다시 선택하면, 실제 연산 없이 캐시된 결과를 즉시 불러와 실행 시간을 단축합니다.

캐싱 기능은 데이터 로딩, 복잡한 통계 계산, 머신러닝 모델 예측 등 반복적으로 동일한 결과가 필요한 고비용 연산에 매우 유용합니다.


## 7_streamlit_dashboard (대시보드 제작)
이 폴더는 지금까지 배운 Streamlit의 다양한 기능을 총정리하여 제조업 데이터 분석 대시보드를 구현한 예제입니다.  

1. `dashboard_page.py`:
    - 결함률, 생산량, 품질 점수, 작업자 생산성 등 핵심 성과 지표 계산
    - `st.metric`을 사용해 전월 대비 증감을 계산, `st.info`와 `st.error`를 사용해 전체 평균 대비 현재 상태 설명
    - Plotly를 이용한 게이지 차트, 라인 차트, 히스토그램, 박스 플롯 등 여러 종류의 차트 시각화

2. `prediction_page.py`:
    - 미리 학습된 .pkl 모델을 불러와 사용자의 입력값에 따라 결함 발생 여부 예측
    - `st.slider`와 `st.number_input` 위젯을 사용하여 사용자가 예측 모델에 값 입력
    - 히스토그램을 통해 사용자가 입력한 값이 전체 데이터셋 분포에서 어느 위치에 있는지 예측 분포 시각화


## 8_streamlit_chatbot.py (챗봇 앱)
이 파일은 Streamlit을 사용하여 AI 챗봇 애플리케이션을 만드는 방법을 보여주는 예제입니다. 

- API 연동: OpenAI 라이브러리를 통해 외부 API를 호출하여 답변 생성
- `st.session_state`: `st.session_state.messages`를 사용하여 사용자와 챗봇 간의 대화 기록을 저장하고 유지
- `st.chat_message`: 챗봇과 사용자의 메시지를 명확하게 구분하여 대화창에 표시
- `st.chat_input`: 사용자가 메시지를 입력할 수 있는 입력창을 제공하여 상호작용


## 8_streamlit_voicechat.py (음성 챗봇 앱)
이 파일은 AI 음성 비서 애플리케이션을 만드는 방법을 보여주는 예제입니다.       
OpenAI의 Whisper API를 활용한 음성 인식(STT)과 TTS API를 활용한 음성 합성을 결합하여 사용자와 음성으로 대화할 수 있는 챗봇 기능을 구현했습니다.

- 음성 인식(STT): 사용자가 녹음한 음성 메시지를 텍스트로 변환, `st.audio_input` 위젯으로 음성 파일을 받아 OpenAI의 Whisper 모델로 전사(Transcribe)
- 음성 합성(TTS): 챗봇의 텍스트 답변을 음성 파일로 변환, OpenAI의 TTS 모델로 음성을 생성하고, 이를 자동 재생하도록 설정하여 자연스러운 대화 흐름 제공
- 대화 기록 관리: `st.session_state`를 사용하여 사용자와 챗봇의 음성 및 텍스트 대화 기록 유지


