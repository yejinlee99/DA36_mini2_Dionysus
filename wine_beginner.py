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

def wine_preprocessing(data):
    wine_beginner_df = pd.read_csv(data)

    # NaN 값 데이터(열) 삭제
    columns = ['country', 'variety']
    wine = wine_beginner_df.dropna(subset=columns)

    # 수치형 결측치 값은 각 컬럼의 평균을 집어넣는다.
    wine_price_mean = wine['price'].mean()
    wine['price'] = wine['price'].fillna(wine_price_mean)

    # 세부 지역 결측치는 나라이름을 집어넣는다.
    wine['region_1'] = wine['region_1'].fillna(wine['country'])
    wine['region_2'] = wine['region_2'].fillna(wine['country'])

    # 컬럼 삭제
    columns = ['Unnamed: 0', 'taster_name', 'taster_twitter_handle']
    wine = wine.drop(columns, axis=1)

    # 중복된 행 삭제
    wine = wine.drop_duplicates()

    return wine

def wine_beginner_recommendation(value):
    wine = wine_preprocessing('./data/archive/winemag-data-130k-v2.csv')

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
    result_df = wine.iloc[review_sorted_index][['title', 'cluster','points', 'country', 'price', 'variety', 'winery']]
    review_sim = review_sim.reshape(-1)
    result_df['similarity'] = review_sim[review_sorted_index]

    # 와인 추천 top15
    result_title = result_df['title'].tolist()
    result_country = result_df['country'].tolist()
    result_price = result_df['price'].tolist()
    result_variety = result_df['variety'].tolist()
    result_winery = result_df['winery'].tolist()
    result_points = result_df['points'].tolist()


    return result_title, result_country, result_price, result_variety, result_winery, result_points





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

