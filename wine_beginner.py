import streamlit as st
import pandas as pd
import nltk
import string
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')


def wine_beginner_recommendation_streamlit():
    # 와린이 추천 페이지
    st.title('🤔와린이 추천🤔')
    st.write("당신은 와린이 시군요!! 당신에게 알맞은 와인을 추천해 드리겠습니다.")
    col1, col2 = st.columns(2)
    with col1:
        # '홈으로 돌아가기' 버튼
        if st.button('홈으로 돌아가기', icon='🏠', use_container_width=True):
            st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동
    with col2:
        # '추천 시작' 버튼
        if st.button('추천 시작하기!', icon='🍷', use_container_width=True):
            st.session_state.page = 'wine_beginner_step1'  # 버튼 클릭 시 step1 페이지로 이동

    # '질문1' 페이지
    if st.session_state.page == 'wine_beginner_step1':
        st.session_state.selected_values = []
        st.title("Step 1. 더 선호하시는 것은 무엇입니까? ")
        if st.button('고기🥩', icon='🥩', use_container_width=True):
            answer1 = 'dry', 'firm', 'tannins', 'red', 'flavor', 'dark', 'cabernet', 'sauvignon'
            st.session_state.selected_values.append(answer1)
            st.session_state.page = 'wine_beginner_step2'  # 버튼 클릭 시 페이지 변경
        elif st.button('생선🐟', icon='🐟', use_container_width=True):
            answer1 = 'fruit', 'white', 'crisp', 'fresh', 'bright', 'touch', 'sauvignon', 'light'
            st.session_state.selected_values.append(answer1)
            st.session_state.page = 'wine_beginner_step2'
        elif st.button('채소🥬', icon='🥬', use_container_width=True):
            answer1 = 'fruit', 'white', 'crisp', 'fresh', 'bright', 'touch', 'sauvignon', 'light'
            st.session_state.selected_values.append(answer1)
            st.session_state.page = 'wine_beginner_step2'

        # '홈으로 돌아가기' 버튼
        elif st.button('홈으로 돌아가기', icon='🏠'):
            st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동

    # '질문2' 페이지
    elif st.session_state.page == 'wine_beginner_step2':
        st.title("Step 2. 더 선호하시는 것은 무엇입니까? ")
        if st.button('트로피칼🍍', icon='🍍', use_container_width=True):
            answer2 = 'fruit', 'apple', 'peach', 'pear', 'ripe', 'fruity', 'smooth', 'juicy', 'white', 'flavor', 'smooth', 'soft', 'sauvignon', 'rich', 'round', 'plum', 'sweet'
            st.session_state.selected_values.append(answer2)
            st.session_state.page = 'wine_beginner_step3'  # 버튼 클릭 시 페이지 변경
        elif st.button('시트러스🍊', icon='🍊', use_container_width=True):
            answer2 = 'fruit', 'citrus', 'lemon', 'acidity', 'fruity', 'juicy', 'white', 'flavor', 'crisp', 'green', 'fresh', 'bright', 'touch', 'sauvignon', 'light'
            st.session_state.selected_values.append(answer2)
            st.session_state.page = 'wine_beginner_step3'
        elif st.button('베리🍒', icon='🍒', use_container_width=True):
            answer2 = 'fruit', 'red', 'berry', 'blackberry', 'raspberry', 'black cherry', 'bright', 'cabernet', 'sauvignon'
            st.session_state.selected_values.append(answer2)
            st.session_state.page = 'wine_beginner_step3'
        elif st.button('향신료🫚', icon='🫚', use_container_width=True):
            answer2 = 'structure', 'firm', 'red', 'flavor', 'spicy', 'spice', 'dark', 'character', 'rich'
            st.session_state.selected_values.append(answer2)
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

        if st.button('장미꽃🌹', icon='🌹', use_container_width=True):
            answer3 = 'structure', 'firm', 'red', 'dark', 'rich'
            st.session_state.selected_values.append(answer3)
            st.session_state.page = 'wine_beginner_step4'  # 버튼 클릭 시 페이지 변경
        elif st.button('제비꽃🌸', icon='🌸', use_container_width=True):
            answer3 = 'smooth', 'red', 'flavor', 'finish', 'dark', 'soft', 'texture', 'cabernet', 'sauvignon', 'rich', 'nose'
            st.session_state.selected_values.append(answer3)
            st.session_state.page = 'wine_beginner_step4'
        elif st.button('백합🌼', icon='🌼', use_container_width=True):
            answer3 = 'white', 'crisp', 'fresh', 'bright', 'touch', 'light'
            st.session_state.selected_values.append(answer3)
            st.session_state.page = 'wine_beginner_step4'
        elif st.button('나무🌳', icon='🌳', use_container_width=True):
            answer3 = 'dry', 'structure', 'firm', 'red', 'dark', 'texture', 'cabernet', 'sauvignon', 'oak', 'vanilla', 'years', 'feel', 'toast', 'lead', 'age'
            st.session_state.selected_values.append(answer3)
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
        if st.button('달콤한 초콜릿❤️', icon='❤️', use_container_width=True):
            answer4 = 'juicy', 'crisp', 'bright', 'chocolate', 'sweet', 'light'
            st.session_state.selected_values.append(answer4)
            st.session_state.page = 'wine_beginner_step5'  # 버튼 클릭 시 페이지 변경
        elif st.button('카카오 50%🤎', icon='🤎', use_container_width=True):
            answer4 = 'smooth', 'soft', 'chocolate', 'hint', 'sweet'
            st.session_state.selected_values.append(answer4)
            st.session_state.page = 'wine_beginner_step5'
        elif st.button('카카오 100%🍫', icon='🍫', use_container_width=True):
            answer4 = 'dry', 'structure', 'firm', 'tannins', 'red', 'dark', 'chocolate', 'lead'
            st.session_state.selected_values.append(answer4)
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
        if st.button('묵은지🌶️', icon='🌶️', use_container_width=True):
            answer5 = 'dry', 'structure', 'firm', 'tannins', 'red', 'white', 'cabernet', 'sauvignon', 'oak', 'years', 'age'
            st.session_state.selected_values.append(answer5)
            st.session_state.page = 'wine_beginner_step6'  # 버튼 클릭 시 페이지 변경
        elif st.button('신김치🧄', icon='🧄', use_container_width=True):
            answer5 = 'acidity', 'fruit', 'lemon', 'white', 'green', 'crisp', 'fresh', 'bright', 'light', 'age'
            st.session_state.selected_values.append(answer5)
            st.session_state.page = 'wine_beginner_step6'
        elif st.button('조금 익은 김치🧅', icon='🧅', use_container_width=True):
            answer5 = 'smooth', 'plum', 'soft', 'round'
            st.session_state.selected_values.append(answer5)
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
        if st.button('라떼🥛', icon='🥛', use_container_width=True):
            answer6 = 'smooth', 'soft', 'light', 'round'
            st.session_state.selected_values.append(answer6)
            st.session_state.page = 'wine_beginner_step7'  # 버튼 클릭 시 페이지 변경
        elif st.button('에스프레소☕', icon='☕', use_container_width=True):
            answer6 = 'dry', 'structure', 'firm', 'tannins', 'red', 'dark', 'rich', 'character'
            st.session_state.selected_values.append(answer6)
            st.session_state.page = 'wine_beginner_step7'
        elif st.button('아메리카노🥤', icon='🥤', use_container_width=True):
            answer6 = 'dry', 'smooth', 'soft', 'rich', 'hint', 'round'
            st.session_state.selected_values.append(answer6)
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
        if st.button('진하게 우려낸🥇', icon='🥇', use_container_width=True):
            answer7 = 'dry', 'structure', 'firm', 'tannins', 'red', 'dark'
            st.session_state.selected_values.append(answer7)
            st.session_state.page = 'wine_beginner_final'  # 버튼 클릭 시 페이지 변경
        elif st.button('적당히 우려낸🥈', icon='🥈', use_container_width=True):
            answer7 = 'structure', 'red', 'dark', 'smooth', 'soft', 'hint'
            st.session_state.selected_values.append(answer7)
            st.session_state.page = 'wine_beginner_final'
        elif st.button('연하게 우려낸🥉', icon='🥉', use_container_width=True):
            answer7 = 'smooth', 'soft', 'touch', 'light'
            st.session_state.selected_values.append(answer7)
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

    # 결과 확인하러가기 페이지
    elif st.session_state.page == 'wine_beginner_final':
        st.title('모든 질문이 끝났습니다.')
        st.write('결과 확인까지 다소 시간이 걸릴 수 있습니다. 잠시만 기다려 주세요~')
        if st.button('결과 확인하러 가기🍇', icon='🍇', use_container_width=True):
            st.session_state.page = 'wine_beginner_final_result'

    # 와린이 파이널 페이지
    elif st.session_state.page == 'wine_beginner_final_result':
        st.title('🤔와린이 와인 추천 완료🤔')

        wine_beginner_recommendation_result = wine_beginner_recommendation(st.session_state.selected_values)

        st.write("🍷당신이 좋아할 것 같은 Top 3 와인🍷")
        st.write(f"🥇 Top 1. {wine_beginner_recommendation_result[0]}")
        st.write(f"🥈 Top 2. {wine_beginner_recommendation_result[1]}")
        st.write(f"🥉 Top 3. {wine_beginner_recommendation_result[2]}")

        st.write("😵당신이 좋아하지 않을 것 같은 Top 3 와인😵")
        st.write(f"🧨 Bottom 1. {wine_beginner_recommendation_result[-1]}")
        st.write(f"🧨 Bottom 2. {wine_beginner_recommendation_result[-2]}")
        st.write(f"🧨 Bottom 3. {wine_beginner_recommendation_result[-3]}")

        col1, col2 = st.columns(2)
        with col1:
            # '홈으로 돌아가기' 버튼
            if st.button('홈으로 돌아가기', icon='🏠', use_container_width=True):
                st.session_state.page = 'home'  # 버튼 클릭 시 홈 페이지로 이동
        with col2:
            # '다시 추천 받기' 버튼
            if st.button('다시 추천 받기!', icon='🔄', use_container_width=True):
                st.session_state.page = 'wine_beginner_step1'  # 버튼 클릭 시 다시 step1 페이지로 이동


def wine_beginner_recommendation(value):
    wine = pd.read_csv('./data/archive/winemag-data-130k-v2.csv')

    # NaN 값 데이터(열) 삭제
    columns = ['country', 'variety']
    wine = wine.dropna(subset=columns)

    # 수치형 결측치 값은 각 컬럼의 평균을 집어넣는다.
    wine_price_mean = wine['price'].mean()
    wine['price'] = wine['price'].fillna(wine_price_mean)

    # 세부 지역 결측치는 나라이름을 집어넣는다.
    wine['region_1'] = wine['region_1'].fillna(wine['country'])
    wine['region_2'] = wine['region_2'].fillna(wine['country'])

    # 컬럼 삭제
    columns = ['Unnamed: 0', 'taster_name', 'taster_twitter_handle']
    wine = wine.drop(columns, axis=1)

    result = [", ".join(item) for item in value]
    final_result = "\n".join(result)
    user_input = [None, final_result, None, None, None, None, None, None, None, None, None]
    wine.loc[129971] = user_input

    tfidf_vectorizer = TfidfVectorizer(
        tokenizer=lemmatize,
        stop_words='english',
        ngram_range=(1, 2),
        max_df=0.9,
        min_df=0.05
    )
    review_vecs = tfidf_vectorizer.fit_transform(wine['description'])

    kmeans = KMeans(
        n_clusters=10,
        max_iter=10000,
        random_state=0
    )
    # 중심점 게산
    reviews_label = kmeans.fit_predict(review_vecs)
    wine['cluster'] = reviews_label

    # 군집화 중심점
    centers = kmeans.cluster_centers_

    # tf-idf값이 높은 순으로 정렬
    centroid_arg_ind = centers.argsort()[:, ::-1]
    top20 = centroid_arg_ind[:, :30]
    feature_names = tfidf_vectorizer.get_feature_names_out()
    top20_df = pd.DataFrame(feature_names[top20])

    # 와인 이름 관련 리뷰를 기준 리뷰로 선정
    # 마지막 리뷰(사용자 지정 데이터)를 기준 리뷰로 선정
    base_index = 129971

    # 기준 리뷰와 모든 리뷰의 유사도 계산
    review_sim = cosine_similarity(review_vecs[-1], review_vecs)

    # 유사도가 높은 순으로 정렬
    review_sorted_index = review_sim.argsort()[:, ::-1]  # 내림차순 정렬
    review_sorted_index = review_sorted_index[:, 1:]
    review_sorted_index = review_sorted_index.reshape(-1)  # 자기자신 제외

    # 유사도가 높은 순으로 정렬된 와인 이름 조회
    result_df = wine.iloc[review_sorted_index][['title', 'cluster']]
    review_sim = review_sim.reshape(-1)
    result_df['similarity'] = review_sim[review_sorted_index]

    # 와인 추천 top15
    result_title = result_df['title'].tolist()
    return result_title




def lemmatize(text):
    """
    소문자변환, 특수문자제거, 토큰화, 어근분리
    """
    # 1. 소문자 변환
    text = text.lower()

    # 2. 특수문자 변환표 dict
    punc_rem_dict = dict((ord(ch), None) for ch in string.punctuation)
    text = text.translate(punc_rem_dict)  # 특수문자 제거

    # 3. 토큰화
    tokens = nltk.word_tokenize(text)

    # 4. 어근분리
    lemmatizer = WordNetLemmatizer()

    return [lemmatizer.lemmatize(token, pos='v') for token in tokens]

