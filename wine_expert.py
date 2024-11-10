import pandas as pd
from catboost import CatBoostRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import euclidean_distances

# input = (1,3,4,4,4)

def wine_expert_recommendation(input):
    wine_expert_df = pd.read_csv('data/archive/data_cleansed.csv')
    wine_expert_df.fillna(value=0, inplace=True)

    features = ['acidity', 'fizziness', 'intensity', 'sweetness', 'tannin']
    X = wine_expert_df[features]
    y = wine_expert_df[features]  # 추천 시스템이므로 X와 y 모두 같은 특성 사용

    # 모델 훈련
    base_model = CatBoostRegressor(iterations=500, depth=6, learning_rate=0.1, loss_function='RMSE', verbose=0)
    model = MultiOutputRegressor(base_model)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)

    # 사용자 입력값
    input_acidity = input[0]
    input_fizziness = input[1]
    input_intensity = input[2]
    input_sweetness = input[3]
    input_tannin = input[4]

    input_features = [[input_acidity, input_fizziness, input_intensity, input_sweetness, input_tannin]]

    # 모델을 통해 예측된 특성
    predicted_features = model.predict(input_features)

    # 입력값과 데이터셋 간의 거리 계산
    distances = euclidean_distances(predicted_features.reshape(1, -1), X).flatten()
    closest_idx = distances.argsort()[:10]  # 가장 가까운 5개 와인 추천

    # 추천 결과 출력
    recommended_wines = wine_expert_df.iloc[closest_idx]
    selected_columns = ['vintage_wine_name', 'vintage_winery', 'vintage_country', 'vintage_wine_type', 'varietal_name',
                       'body_description', 'acidity_description']
    df_selected = recommended_wines[selected_columns].reset_index(drop=True)
    return df_selected

# print(wine_expert(input))