import streamlit as st
from wine_beginner import *



# 세션 상태를 사용하여 페이지를 추적
if 'page' not in st.session_state:
    st.session_state.page = 'home'  # 기본 페이지는 'home'

# 홈 페이지
if st.session_state.page == 'home':
    st.title('🍷와인 추천 시스템🍷')
    st.write("안녕하세요. 당신이 좋아할 만한 와인을 추천해 드립니다!!")

    # '와잘알 와인추천' 버튼
    if st.button('와잘알 추천🤓', icon="🤓", use_container_width=True):
        st.session_state.page = 'wine_expert'  # 버튼 클릭 시 페이지 변경
    st.write("☝️ 와인에 대해 잘 아시는 당신! 이걸 이용해 보세요!")

    # '와린이 와인추천' 버튼
    if st.button('와린이 추천🤔', icon="🤔", use_container_width=True):
        st.session_state.page = 'wine_beginner'  # 버튼 클릭 시 페이지 변경
    st.write("☝️ 와인에 대해 잘 모르는 당신! 이걸 이용해 보세요!")

    # '음식에 어울리는  와인추천' 버튼
    if st.button('음식에 어울리는 와인추천🍽️', icon="🍽️", use_container_width=True):
        st.session_state.page = 'wine_food'  # 버튼 클릭 시 페이지 변경
    st.write("☝️ 음식에 어울리는 와인을 찾고 있는 당신! 이걸 이용해 보세요!")


# 와잘알 추천 페이지
elif st.session_state.page == 'wine_expert':
    st.title('🤓와잘알 추천 시스템🤓')
    st.write("당신은 와잘알이시군요!! 당신에게 알맞은 와인을 추천해 드리겠습니다.")

    # '홈으로 돌아가기' 버튼
    if st.button('홈으로 돌아가기'):
        st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동



# 와린이 추천 페이지
elif st.session_state.page == 'wine_beginner':
    wine_beginner_recommendation_streamlit()

# 음식에 어울리는 와인 추천 페이지
elif st.session_state.page == 'wine_food':
    st.title('🍽️음식에 어울리는 와인추천🍽️')
    st.write("당신은 음식에 어울리는 와인을 찾고 있으시군요!!")
    st.write("당신에게 알맞은 와인을 추천해 드리겠습니다.")

    # '홈으로 돌아가기' 버튼
    if st.button('홈으로 돌아가기'):
        st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동




























