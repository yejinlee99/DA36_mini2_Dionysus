# import pandas as pd
# from catboost import CatBoostRegressor
# from sklearn.multioutput import MultiOutputRegressor
# from sklearn.model_selection import train_test_split
# from sklearn.metrics.pairwise import euclidean_distances

# input = (1,3,4,4,4)

# def wine_expert_recommendation(input):
#     wine_expert_df = pd.read_csv('data/archive/data_cleansed.csv')
#     wine_expert_df.fillna(value=0, inplace=True)
#
#     features = ['acidity', 'fizziness', 'intensity', 'sweetness', 'tannin']
#     X = wine_expert_df[features]
#     y = wine_expert_df[features]  # 추천 시스템이므로 X와 y 모두 같은 특성 사용
#
#     # 모델 훈련
#     base_model = CatBoostRegressor(iterations=500, depth=6, learning_rate=0.1, loss_function='RMSE', verbose=0)
#     model = MultiOutputRegressor(base_model)
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#     model.fit(X_train, y_train)
#
#     # 사용자 입력값
#     input_acidity = input[0]
#     input_fizziness = input[1]
#     input_intensity = input[2]
#     input_sweetness = input[3]
#     input_tannin = input[4]
#
#     input_features = [[input_acidity, input_fizziness, input_intensity, input_sweetness, input_tannin]]
#
#     # 모델을 통해 예측된 특성
#     predicted_features = model.predict(input_features)
#
#     # 입력값과 데이터셋 간의 거리 계산
#     distances = euclidean_distances(predicted_features.reshape(1, -1), X).flatten()
#     closest_idx = distances.argsort()[:10]  # 가장 가까운 5개 와인 추천
#
#     # 추천 결과 출력
#     recommended_wines = wine_expert_df.iloc[closest_idx]
#     selected_columns = ['vintage_wine_name', 'vintage_winery', 'vintage_country', 'vintage_wine_type', 'varietal_name',
#                        'body_description', 'acidity_description']
#     df_selected = recommended_wines[selected_columns].reset_index(drop=True)
#     return df_selected


import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import streamlit as st


# Streamlit 앱의 메인 함수
def wine_expert_recommendation(input):
    # 데이터 불러오기
    wine_expert_df = pd.read_csv('data/archive/data_cleansed.csv')
    wine_expert_df.fillna(value=0, inplace=True)

    # 특징 설정
    features = ['acidity', 'fizziness', 'intensity', 'sweetness', 'tannin']
    X = wine_expert_df[features]

    # K-Means 클러스터링 모델 훈련
    kmeans = KMeans(n_clusters=5, random_state=42)
    kmeans.fit(X)
    labels = kmeans.labels_

    # K-Means 클러스터링 모델 훈련
    kmeans = KMeans(n_clusters=5, random_state=42)
    kmeans.fit(X)
    labels = kmeans.labels_

    # 입력값
    input_acidity = input[0]
    input_fizziness = input[1]
    input_intensity = input[2]
    input_sweetness = input[3]
    input_tannin = input[4]
    input_features = [[input_acidity, input_fizziness, input_intensity, input_sweetness, input_tannin]]

    # 입력값이 속한 클러스터 예측
    cluster_label = kmeans.predict(input_features)[0]

    # 같은 클러스터에 속하는 데이터 필터링
    similar_wines = wine_expert_df[labels == cluster_label]

    # 클러스터 레이블을 추가
    similar_wines['cluster'] = labels[labels == cluster_label]

    # 추천 결과 출력 (최대 10개)
    selected_columns = ['vintage_wine_name', 'vintage_winery', 'vintage_country', 'vintage_wine_type', 'varietal_name',
                        'body_description', 'acidity_description', 'cluster']
    df_selected = similar_wines[selected_columns].head(10).reset_index(drop=True)

    return df_selected

def show_cluster(input):
    # 데이터 불러오기
    wine_expert_df = pd.read_csv('data/archive/data_cleansed.csv')
    wine_expert_df.fillna(value=0, inplace=True)

    # 특징 설정
    features = ['acidity', 'fizziness', 'intensity', 'sweetness', 'tannin']
    X = wine_expert_df[features]

    # K-Means 클러스터링 모델 훈련
    kmeans = KMeans(n_clusters=5, random_state=42)
    kmeans.fit(X)
    labels = kmeans.labels_

    # K-Means 클러스터링 모델 훈련
    kmeans = KMeans(n_clusters=5, random_state=42)
    kmeans.fit(X)
    labels = kmeans.labels_

    # PCA를 사용하여 시각화 데이터 생성 (2D)
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    # PCA 결과와 클러스터 레이블을 데이터프레임으로 변환
    chart_data = pd.DataFrame({
        'PCA1': X_pca[:, 0],
        'PCA2': X_pca[:, 1],
        'Cluster': labels
    })

    # 입력값 PCA 변환 후 추가
    input_acidity = input[0]
    input_fizziness = input[1]
    input_intensity = input[2]
    input_sweetness = input[3]
    input_tannin = input[4]
    input_features = [[input_acidity, input_fizziness, input_intensity, input_sweetness, input_tannin]]
    input_pca = pca.transform(input_features)

    # 입력값을 데이터프레임에 추가하여 시각화
    input_df = pd.DataFrame({
        'PCA1': [input_pca[0, 0]],
        'PCA2': [input_pca[0, 1]],
        'Cluster': [-1]  # 입력값은 별도의 클러스터로 표시
    })

    # pd.concat()을 사용하여 입력값 추가
    chart_data = pd.concat([chart_data, input_df], ignore_index=True)

    return chart_data



# # 예시 입력값
# example_input = [3.5, 2.5, 4.0, 2.0, 3.0]
# wine_expert_recommendation(example_input)
