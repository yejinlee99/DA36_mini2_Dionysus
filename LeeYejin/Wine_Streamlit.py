import streamlit as st

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
    st.title('🤔와린이 추천🤔')
    st.write("당신은 와린이 시군요!! 당신에게 알맞은 와인을 추천해 드리겠습니다.")
    col1, col2 = st.columns(2)
    with col1:
        # '홈으로 돌아가기' 버튼
        if st.button('홈으로 돌아가기', icon = '🏠', use_container_width=True):
            st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동
    with col2:
        # '추천 시작' 버튼
        if st.button('추천 시작하기!', icon = '🍷', use_container_width=True):
            st.session_state.page = 'wine_beginner_step1'  # 버튼 클릭 시 step1 페이지로 이동

# '질문1' 페이지
elif st.session_state.page == 'wine_beginner_step1':
    st.title("Step 1. 더 선호하시는 것은 무엇입니까? ")
    if st.button('고기🥩', icon = '🥩', use_container_width=True):
        st.session_state.page = 'wine_beginner_step2'  # 버튼 클릭 시 페이지 변경
    if st.button('생선🐟', icon = '🐟', use_container_width=True):
        st.session_state.page = 'wine_beginner_step2'
    if st.button('채소🥬', icon = '🥬', use_container_width=True):
        st.session_state.page = 'wine_beginner_step2'

    # '홈으로 돌아가기' 버튼
    if st.button('홈으로 돌아가기', icon = '🏠'):
        st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동

# '질문2' 페이지
elif st.session_state.page == 'wine_beginner_step2':
    st.title("Step 2. 더 선호하시는 것은 무엇입니까? ")
    if st.button('트로피칼🍍', icon = '🍍', use_container_width=True):
        st.session_state.page = 'wine_beginner_step3'  # 버튼 클릭 시 페이지 변경
    if st.button('시트러스🍊', icon = '🍊', use_container_width=True):
        st.session_state.page = 'wine_beginner_step3'
    if st.button('베리🍒', icon = '🍒', use_container_width=True):
        st.session_state.page = 'wine_beginner_step3'
    if st.button('향신료🫚', icon = '🫚', use_container_width=True):
        st.session_state.page = 'wine_beginner_step3'

    col1, col2 = st.columns(2)
    with col1:
        # '홈으로 돌아가기' 버튼
        if st.button('홈으로 돌아가기', icon='🏠', use_container_width=True):
            st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동
    with col2:
        # '이전으로 돌아가기' 버튼
        if st.button('이전 페이지로 돌아가기', icon='⬅️', use_container_width=True):
            st.session_state.page = 'wine_beginner_step1'

# '질문3' 페이지
elif st.session_state.page == 'wine_beginner_step3':
    st.title("Step 3. 더 선호하시는 것은 무엇입니까? ")
    if st.button('장미꽃🌹', icon = '🌹', use_container_width=True):
        st.session_state.page = 'wine_beginner_step4'  # 버튼 클릭 시 페이지 변경
    if st.button('제비꽃🌸', icon = '🌸', use_container_width=True):
        st.session_state.page = 'wine_beginner_step4'
    if st.button('백합🌼', icon = '🌼', use_container_width=True):
        st.session_state.page = 'wine_beginner_step4'
    if st.button('나무🌳', icon = '🌳', use_container_width=True):
        st.session_state.page = 'wine_beginner_step4'

    col1, col2 = st.columns(2)
    with col1:
        # '홈으로 돌아가기' 버튼
        if st.button('홈으로 돌아가기', icon='🏠', use_container_width=True):
            st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동
    with col2:
        # '이전으로 돌아가기' 버튼
        if st.button('이전 페이지로 돌아가기', icon='⬅️', use_container_width=True):
            st.session_state.page = 'wine_beginner_step2'

# '질문4' 페이지
elif st.session_state.page == 'wine_beginner_step4':
    st.title("Step 4. 더 선호하시는 것은 무엇입니까? ")
    if st.button('달콤한 초콜릿❤️', icon = '❤️', use_container_width=True):
        st.session_state.page = 'wine_beginner_step5'  # 버튼 클릭 시 페이지 변경
    if st.button('카카오 50%🤎', icon = '🤎', use_container_width=True):
        st.session_state.page = 'wine_beginner_step5'
    if st.button('카카오 100%🍫', icon = '🍫', use_container_width=True):
        st.session_state.page = 'wine_beginner_step5'

    col1, col2 = st.columns(2)
    with col1:
        # '홈으로 돌아가기' 버튼
        if st.button('홈으로 돌아가기', icon='🏠', use_container_width=True):
            st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동
    with col2:
        # '이전으로 돌아가기' 버튼
        if st.button('이전 페이지로 돌아가기', icon='⬅️', use_container_width=True):
            st.session_state.page = 'wine_beginner_step3'

# '질문5' 페이지
elif st.session_state.page == 'wine_beginner_step5':
    st.title("Step 5. 어떤 김치를 더 좋아하세요?")
    if st.button('묵은지🌶️', icon = '🌶️', use_container_width=True):
        st.session_state.page = 'wine_beginner_step6'  # 버튼 클릭 시 페이지 변경
    if st.button('신김치🧄', icon = '🧄', use_container_width=True):
        st.session_state.page = 'wine_beginner_step6'
    if st.button('조금 익은 김치🧅', icon = '🧅', use_container_width=True):
        st.session_state.page = 'wine_beginner_step6'

    col1, col2 = st.columns(2)
    with col1:
        # '홈으로 돌아가기' 버튼
        if st.button('홈으로 돌아가기', icon='🏠', use_container_width=True):
            st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동
    with col2:
        # '이전으로 돌아가기' 버튼
        if st.button('이전 페이지로 돌아가기', icon='⬅️', use_container_width=True):
            st.session_state.page = 'wine_beginner_step4'

# '질문6' 페이지
elif st.session_state.page == 'wine_beginner_step6':
    st.title("Step 6. 좋아하는 커피 종류를 알려주세요.")
    if st.button('라떼🥛', icon = '🥛', use_container_width=True):
        st.session_state.page = 'wine_beginner_step7'  # 버튼 클릭 시 페이지 변경
    if st.button('에스프레소☕', icon = '☕', use_container_width=True):
        st.session_state.page = 'wine_beginner_step7'
    if st.button('아메리카노🥤', icon = '🥤', use_container_width=True):
        st.session_state.page = 'wine_beginner_step7'

    col1, col2 = st.columns(2)
    with col1:
        # '홈으로 돌아가기' 버튼
        if st.button('홈으로 돌아가기', icon='🏠', use_container_width=True):
            st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동
    with col2:
        # '이전으로 돌아가기' 버튼
        if st.button('이전 페이지로 돌아가기', icon='⬅️', use_container_width=True):
            st.session_state.page = 'wine_beginner_step5'

# '질문7' 페이지
elif st.session_state.page == 'wine_beginner_step7':
    st.title("Step 7. 홍차의 떫은 맛에 더 익숙한가요?")
    if st.button('진하게 우려낸🥇', icon = '🥇', use_container_width=True):
        st.session_state.page = 'wine_beginner_final'  # 버튼 클릭 시 페이지 변경
    if st.button('적당히 우려낸🥈', icon = '🥈', use_container_width=True):
        st.session_state.page = 'wine_beginner_final'
    if st.button('연하게 우려낸🥉', icon = '🥉', use_container_width=True):
        st.session_state.page = 'wine_beginner_final'

    col1, col2 = st.columns(2)
    with col1:
        # '홈으로 돌아가기' 버튼
        if st.button('홈으로 돌아가기', icon='🏠', use_container_width=True):
            st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동
    with col2:
        # '이전으로 돌아가기' 버튼
        if st.button('이전 페이지로 돌아가기', icon='⬅️', use_container_width=True):
            st.session_state.page = 'wine_beginner_step6'

# 와린이 파이널 페이지
elif st.session_state.page == 'wine_beginner_final':
    st.title('🤔와린이 와인 추천 완료🤔')
    st.write("당신이 좋아할 것 같은 와인은...")

    st.write("당신이 좋아하지 않을 것 같은 와인은...")
    col1, col2 = st.columns(2)
    with col1:
        # '홈으로 돌아가기' 버튼
        if st.button('홈으로 돌아가기', icon = '🏠', use_container_width=True):
            st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동
    with col2:
        # '다시 추천 받기' 버튼
        if st.button('다시 추천 받기!', icon = '🔄', use_container_width=True):
            st.session_state.page = 'wine_beginner_step1'  # 버튼 클릭 시 다시 step1 페이지로 이동






# 음식에 어울리는 와인 추천 페이지
elif st.session_state.page == 'wine_food':
    st.title('🍽️음식에 어울리는 와인추천🍽️')
    st.write("당신은 음식에 어울리는 와인을 찾고 있으시군요!!")
    st.write("당신에게 알맞은 와인을 추천해 드리겠습니다.")

    # '홈으로 돌아가기' 버튼
    if st.button('홈으로 돌아가기'):
        st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동




























