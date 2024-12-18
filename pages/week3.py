import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 페이지 설정
st.set_page_config(layout="wide", page_title="3차시: 따릉이 이용 시간 분석")
# 네비게이션 버튼
col1, col2, col3 = st.columns([1,3,1])
with col1:
    if st.button('⬅️ 이전 차시로'):
        st.switch_page("pages/week2.py")  
with col3:
    if st.button('다음 차시 ➡️'):
        st.switch_page("pages/week4.py")  

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
        .highlight-box {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
            border-left: 5px solid #FF6B6B;
        }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv('bikeborrow.csv', encoding='cp949')
    df['시간'] = df['기준_시간대'].astype(str).str.zfill(4)
    df['시간대'] = pd.to_datetime(df['시간'], format='%H%M').dt.hour
    df['출발_구'] = df['시작_대여소명'].fillna('').astype(str).apply(
        lambda x: x.split('_')[0].replace('동', '').strip() if x else '알수없음'
    )
    return df

# 타이틀
st.markdown('<h1 class="title">🚲 3차시: 운행시간 데이터 분석 </h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">누가, 언제, 얼마나 오래 따릉이를 탈까요? 🤔</p>', unsafe_allow_html=True)

# 데이터 로드
df = load_data()

# 1. 가장 긴 이용 시간 분석
st.markdown("### 🏆 최장 시간 이용자 분석")

# Top 10 최장 시간 이용자
top_duration = df.nlargest(10, '전체_이용_분')
fig_top = px.bar(top_duration, 
                 x='전체_이용_분', 
                 y='시작_대여소명',
                 orientation='h',
                 title='최장 시간 이용 TOP 10',
                 labels={'전체_이용_분': '이용 시간(분)', '시작_대여소명': '출발 대여소'})
st.plotly_chart(fig_top, use_container_width=True)

# 2. 장거리 이용자 특징 분석
st.markdown("### 🔍 장시간 이용자들의 특징")

# 이용 시간 기준 설정
time_threshold = st.slider('장시간 이용 기준 설정 (분)', 
                          min_value=10, 
                          max_value=int(df['전체_이용_분'].max()),
                          value=30)

long_rides = df[df['전체_이용_분'] >= time_threshold]

col1, col2 = st.columns(2)

with col1:
    # 시간대별 장거리 이용 분포
    hourly_long = long_rides.groupby('시간대')['전체_건수'].sum().reset_index()
    fig_hourly = px.line(hourly_long, 
                        x='시간대', 
                        y='전체_건수',
                        title=f'{time_threshold}분 이상 이용 - 시간대별 분포',
                        labels={'시간대': '시간', '전체_건수': '이용 건수'})
    st.plotly_chart(fig_hourly)

with col2:
    # 출발 지역별 장거리 이용 분포
    region_long = long_rides.groupby('출발_구')['전체_건수'].sum().sort_values(ascending=True).tail(10)
    fig_region = px.bar(region_long, 
                       orientation='h',
                       title=f'{time_threshold}분 이상 이용 - 지역별 분포',
                       labels={'value': '이용 건수', 'index': '지역'})
    st.plotly_chart(fig_region)

# 3. 상세 통계
st.markdown("### 📊 상세 통계")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("평균 이용 시간", f"{df['전체_이용_분'].mean():.1f}분")
with col2:
    st.metric("최장 이용 시간", f"{df['전체_이용_분'].max():.0f}분")
with col3:
    long_ride_percent = (len(long_rides) / len(df)) * 100
    st.metric(f"{time_threshold}분 이상 이용 비율", f"{long_ride_percent:.1f}%")

# 4. 장거리 이용 패턴 분석
st.markdown("### 🎯 장거리 이용 패턴")

# 이용 시간과 이동 거리의 관계
fig_scatter = px.scatter(df, 
                        x='전체_이용_분', 
                        y='전체_이용_거리',
                        title='이용 시간과 이동 거리의 관계',
                        labels={'전체_이용_분': '이용 시간(분)', 
                               '전체_이용_거리': '이동 거리(m)'},
                        opacity=0.6)

st.plotly_chart(fig_scatter, use_container_width=True)

# 분석 인사이트
st.markdown("""
    <div class="highlight-box">
        <h4>💡 분석 결과로 알 수 있는 것</h4>
        <ul>
            <li>장시간 이용자들은 주로 어느 시간대에 많이 있나요?</li>
            <li>어떤 지역에서 장시간 이용이 많이 발생하나요?</li>
            <li>이용 시간과 이동 거리는 어떤 관계가 있나요?</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# 시간대별 평균 이용 시간
st.markdown("### ⏰ 시간대별 평균 이용 시간")
hourly_avg = df.groupby('시간대')['전체_이용_분'].mean().reset_index()
fig_hourly_avg = px.line(hourly_avg, 
                        x='시간대', 
                        y='전체_이용_분',
                        title='시간대별 평균 이용 시간',
                        labels={'시간대': '시간', '전체_이용_분': '평균 이용 시간(분)'})
st.plotly_chart(fig_hourly_avg, use_container_width=True)