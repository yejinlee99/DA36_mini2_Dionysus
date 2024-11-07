import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# 데이터 불러오기 및 컬럼 설정
wine_data_df = pd.read_csv('./data/cleansingWine.csv', low_memory=False)
print(f"Data shape: {wine_data_df.shape}")
wine_data_df.describe()

# 사용할 컬럼 선택
wine_favor_df = wine_data_df[['name', 'nation', 'local1', 'varieties1', 'varieties2', 'varieties3',
                              'type', 'use', 'abv', 'sweet', 'acidity', 'body', 'tannin',
                              'price', 'year', 'ml']]

# 결측치 대체 (abv는 가장 많은 값 13으로 대체)
wine_data_df['abv'] = wine_data_df['abv'].fillna(13)
wine_data_df = wine_data_df.fillna('None')  # 모든 결측치를 'None' 문자열로 대체

# 필요한 컬럼 추출 및 숫자 변환
wine_data_df['sweet_level'] = wine_data_df['sweet'].str.extract(r'(\d+)').astype(float)
wine_data_df['acidity_level'] = wine_data_df['acidity'].str.extract(r'(\d+)').astype(float)
wine_data_df['body_level'] = wine_data_df['body'].str.extract(r'(\d+)').astype(float)
wine_data_df['tannin_level'] = wine_data_df['tannin'].str.extract(r'(\d+)').astype(float)

# NaN 값을 각 컬럼의 평균값으로 대체
wine_data_df = wine_data_df.assign(
    sweet_level=wine_data_df['sweet_level'].fillna(wine_data_df['sweet_level'].mean()),
    acidity_level=wine_data_df['acidity_level'].fillna(wine_data_df['acidity_level'].mean()),
    body_level=wine_data_df['body_level'].fillna(wine_data_df['body_level'].mean()),
    tannin_level=wine_data_df['tannin_level'].fillna(wine_data_df['tannin_level'].mean())
)


# 추천 시스템 함수 정의
def recommend_wines(user_preferences, wine_data_df, top_n=5):
    """
    사용자의 선호도에 따라 유사한 와인을 추천하는 함수

    Parameters:
    - user_preferences: dict - 사용자가 선호하는 속성 (sweet, acidity, body, tannin)
    - wine_data_df: DataFrame - 와인 데이터
    - top_n: int - 추천할 와인 개수

    Returns:
    - 추천된 와인의 DataFrame
    """
    # 사용자 선호도를 numpy array로 변환
    user_vector = np.array([
        user_preferences['sweet'],
        user_preferences['acidity'],
        user_preferences['body'],
        user_preferences['tannin']
    ]).reshape(1, -1)

    # 와인 속성 벡터 추출
    wine_vectors = wine_data_df[['sweet_level', 'acidity_level', 'body_level', 'tannin_level']].values

    # 코사인 유사도 계산
    similarities = cosine_similarity(user_vector, wine_vectors).flatten()

    # 유사도 기준으로 정렬하여 상위 top_n 추천
    top_indices = similarities.argsort()[-top_n:][::-1]
    recommended_wines = wine_data_df.iloc[top_indices]

    return recommended_wines[['name', 'nation', 'local1', 'varieties1', 'price', 'year', 'ml',
                              'sweet_level', 'acidity_level', 'body_level', 'tannin_level']]

# 사용자 선호도 입력서 1 ~ 5 사이만 입력하게 설정
def get_preference(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 5:
                return value
            else:
                print("1에서 5 사이의 숫자를 입력하세요.")
        except ValueError:
            print("유효한 숫자를 입력하세요.")

# 사용자 선호도 입력 받기
user_preferences = {
    'sweet': int(input("당도 선택 (1-5): ")),
    'acidity': int(input("산도 선택 (1-5): ")),
    'body': int(input("바디 선택 (1-5): ")),
    'tannin': int(input("타닌 선택 (1-5): "))
}

# 추천 결과 확인
recommended_wines = recommend_wines(user_preferences, wine_data_df)
print(recommended_wines)
