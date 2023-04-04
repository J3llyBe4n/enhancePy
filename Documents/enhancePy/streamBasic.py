import streamlit as st
#title
st.title("Hello, 빅데이터 AI")
#입력
user_input = st.text_input("어떤 커피 드실래요?","Type Here")
user_input2 = st.text_input("당도 비율을 알려주세요","0%,30%,50%,70% 중 골라주세요.")
if st.button("Submit"):
    st.write(f"{user_input}를 {user_input2} 으로 먹을게요")
#실행 : 터미널 창에 streamlit run 파일명