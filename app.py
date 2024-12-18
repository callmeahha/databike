import streamlit as st 
import pandas as pd  

# 페이지 설정
st.set_page_config(layout="wide", page_title="따릉이 데이터 분석 수업")

# CSS 스타일 추가
st.markdown("""
    <style>
        .title {
            color: #FF6B6B;
            text-align: center;
            padding: 20px;
            font-size: 2.8em;
            font-weight: bold;
            background: linear-gradient(120deg, #FFE5E5 0%, #FFF0F0 100%);
            border-radius: 15px;
            margin-bottom: 20px;
        }
        .subtitle {
            text-align: center;
            color: #666;
            font-size: 1.2em;
            margin-bottom: 30px;
        }
        .login-box {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin: 20px auto;
            max-width: 500px;
        }
        .welcome-text {
            text-align: center;
            color: #4A90E2;
            font-size: 1.5em;
            margin-bottom: 20px;
        }
        .stButton>button {
            background-color: #FF6B6B;
            color: white;
            width: 100%;
            padding: 10px 0;
            border: none;
            border-radius: 5px;
            margin-top: 20px;
        }
        .stButton>button:hover {
            background-color: #FF8585;
        }
    </style>
""", unsafe_allow_html=True)

# 타이틀
st.markdown('<h1 class="title">🚲 정보 교과 데이터 분석 수업</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">따릉이 데이터로 배우는 데이터 분석의 세계</p>', unsafe_allow_html=True)

# 이미지 중앙 정렬
# 이미지 중앙 정렬
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image('image.png', use_container_width=True)  

# 데이터 로드
data = pd.read_csv('id.csv')
data["PW"] = data["PW"].astype(str)

# 로그인 폼
st.markdown('<div class="login-box">', unsafe_allow_html=True)
st.markdown('<p class="welcome-text">로그인하고 시작하기</p>', unsafe_allow_html=True)

with st.form("login_form"):
    ID = st.text_input("아이디", placeholder="아이디를 입력하세요")
    PW = st.text_input("비밀번호", placeholder="비밀번호를 입력하세요", type="password")
    submit_button = st.form_submit_button("로그인")

if submit_button:
    if not ID or not PW:
        st.warning("🔔 아이디와 비밀번호를 모두 입력해주세요.")
    else:
        user = data[(data["ID"]==ID)&(data["PW"]==PW)]
        
        if not user.empty:
            st.success(f"🎉 환영합니다, {ID}님!")
            st.balloons()
            st.switch_page("pages/week1.py")
        else:
            st.error('❌ 사용자 정보가 일치하지 않습니다.')

st.markdown('</div>', unsafe_allow_html=True)

# 추가 정보 (선택사항)
st.markdown("""
    <div style='text-align: center; color: #666; margin-top: 30px; font-size: 0.9em;'>
        중학교 정보 교과 데이터 분석 수업에 오신 것을 환영합니다! 🎈
    </div>
""", unsafe_allow_html=True)