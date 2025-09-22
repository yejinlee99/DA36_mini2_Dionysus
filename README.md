# DA36_mini2_Dionysus
# 🍷Wine Recommendation System🍷
<img width="1188" height="668" alt="스크린샷 2025-09-22 오후 12 24 17" src="https://github.com/user-attachments/assets/8b9c926a-c8db-453f-8533-5f608d2ca193" />

## 🍇 와인 추천의 필요성 🍇
  - 개인화된 추천 (Personalized Recommendation)
  - 새로운 와인 발견 (Discover New Wines)
  - 시간절약 (Time-Saving)

## 🍇 참고 사이트 🍇
[![image](https://github.com/user-attachments/assets/713b7b57-ba37-4e89-a7bb-f2ab2b2f5856)
](https://www.vivino.com/US/en/)

사진을 클릭하세요.

## 🍇 Team Crew 🍇
<div style="display: flex; align-items: center;">

  <img src="https://github.com/user-attachments/assets/843c1342-a6a6-415d-8fbe-6f5611f6e88c" style="width: 100px; margin-right: 20px;">
  <div>
    <strong>Haebin Kim</strong> <맛잘알, 와잘알 와인 추천 구현><br>
    [특징] 와인에 미쳐 사는 사람. 맛있는 음식과 함께라면 와인 주량 3병. 아이디어 제공자
  </div>

</div>

<div style="display: flex; align-items: center;">

  <img src="https://github.com/user-attachments/assets/adbecace-d98a-418a-9581-f570303ddbe9" style="width: 100px; margin-right: 20px;">
  <div>
    <strong>Yejin Lee</strong> <와린이 와인 추천 구현><br>
    [특징] 와인에 대해 아는 것이라고는 스파클링, 레드, 화이트 와인이 있다는 정도의 문외한이었어요. 하지만 이제 나도 와잘알?
  </div>

</div>

<div style="display: flex; align-items: center;">

  <img src="https://github.com/user-attachments/assets/324420a3-a674-4ee7-ac08-4285dbea6408" style="width: 100px; margin-right: 20px;">
  <div>
    <strong>Jeongseok Shim</strong> 팀원<br>
    [특징]  와인 입문자
  </div>

</div>

## 🍇 DATA Introduction 🍇
- [**와잘알/맛잘알 Data**](https://www.vivino.com/explore)
    - API 호출하여 JSON 파일 추출
    - **Columns**   총 22 columns x 3675 rows
        - *wine_ratings_count : 와인 평점 수*
        - *wine_ratings_average : 와인 평점*
        - *foods : 와인에 어울리는 음식*
        - vintage_price : 가격
        - vintage_wine_name : 와인 이름 (이름 + 년도)
        - vintage_wine_type : 와인 타입 (id mapping to type)
        - varietal_name : 포도 품종
        - variety : 와인 품종
        - winery : 와이너리 (양조장)
    - **Row Count**
        - 중복값 제거 후 df.shape = (2024, 22)

- [**와린이 Data**](https://www.kaggle.com/datasets/zynicide/wine-reviews?select=winemag-data_first150k.csv)
    - **Columns**
        - *description : 리뷰*
        - *title : 와인 이름*
        - country : 나라 이름
        - points : 와인 평점
        - price : 와인 가격
        - variety : 와인 품종
        - winery : 와이너리 (양조장)
    - **Row Count**
        - 중복된 행 제거 후 29,971 ⇨ 119,928
    - **Description words**
        - 68 words
        - 단어 벡터화 제외 5% 이하, 90% 이상 

## 🍇 Development Tools 🍇

![image](https://github.com/user-attachments/assets/0618206c-0b8f-46ca-b469-1670d4eee134)
![image](https://github.com/user-attachments/assets/b562dcd6-77ad-4869-ba33-fb8ff2f1ba32)
![image](https://github.com/user-attachments/assets/d8b91890-e764-458d-b4dc-1f413def55d1)
![image](https://github.com/user-attachments/assets/b26c66d7-251b-4e40-8c39-32cd627e45fd)

## 🍇 Our Recommendation System 🍇

- **와잘알ver.**<br>
![image](https://github.com/user-attachments/assets/5c5e3bb5-f02e-4874-bfb9-9af32b960446)

- **와린이ver.**<br>
와린이는 와인 + 어린이의 합성어로 와인에 대해 모르는 사람입니다. 와린이는 와인의 탄닌이 뭔지, 산도가 뭔지 잘 모르기 때문에 선택하기 보다 쉬운 질문을 해서 와인을 추천해 주는 시스템 입니다.

[예시] Step 1. 더 선호하시는 것을 고르세요.
1. 고기    2. 생선    3. 채소

예시로 Step 1을 보면, 각 선택지 마다 와인의 특징을 부여하였고 모델 데이터에서 미리 뽑은 68개의 단어들 중에서 특징들과 어울리는 단어들을 부여했습니다.

- 고기 : 진한 레드와인, 소고기, 양고기, 스테이크, 육즙이 풍부한, 풀바디 레드와인, 탄닌이 풍부, 강한 풍미
    => [dry, firm, tannins, red, flavor, dark, cabernet, sauvignon]

- 생선 : 화이트 와인, 산뜻하고  깔끔한 산미, 신선함, 해산물 요리
    => [fruit, white, crisp, fresh, bright, touch, sauvignon, light]

- 채소 : 화이트, 라이트레드, 구운 채소, 샐러드, 신선한, 상큼함, 섬세한
    => [fruit, white, crisp, fresh, bright, touch, sauvignon, light]

![image](https://github.com/user-attachments/assets/3c1bdc48-1e6b-4f80-a4dd-80c62f57e6ee)


- **맛잘알ver.**<br>
![image](https://github.com/user-attachments/assets/d031912b-4477-48aa-9401-2baff2d9f076)

  
- **와인 추천 결과**
  - **Best 3**<br>
  ![image](https://github.com/user-attachments/assets/a753feb3-9e13-471c-b603-1d4a54c1e3fa)

  - **Worst 3**<br>
  ![image](https://github.com/user-attachments/assets/4e005d8a-43ca-4a74-a2bd-9d86730f9e21)


## 🍇 Streamlit App 🍇

👇와인 추천 시스템을 이용하려면 이걸 눌러주세요.

[![image](https://github.com/user-attachments/assets/74016d81-546a-40ba-aaa6-6d9e63995d4b)
](https://da36mini2dionysus-29g5hzkbgzgnskeescxfnc.streamlit.app/)


## 🍇 구현 영상 🍇

👇와인 추천 시스템 구현영상을 보시려면 이걸 눌러주세요.

[![썸네일](https://github.com/user-attachments/assets/3c4ac3b1-5403-4942-ae89-35263034488f)](https://youtu.be/Fy1aycHWAVM)


<br><br><br><br><br>
## 🇺🇸 English
## 🍇 Why a Wine Recommendation System 🍇
- Personalized recommendations  
- Discover new wines  
- Save time

## 🍇 Reference Site 🍇
[![image](https://github.com/user-attachments/assets/713b7b57-ba37-4e89-a7bb-f2ab2b2f5856)
](https://www.vivino.com/US/en/)

Click the image.

## 🍇 Team Crew 🍇

<div style="display: flex; align-items: center;">
  <img src="https://github.com/user-attachments/assets/843c1342-a6a6-415d-8fbe-6f5611f6e88c" style="width: 100px; margin-right: 20px;">
  <div>
    <strong>Haebin Kim</strong> &lt;Implemented recommendations for wine-savvy users&gt;<br>
    [About] A true wine lover and foodie. Can enjoy up to three bottles with great food. Idea contributor.
  </div>
</div>

<div style="display: flex; align-items: center;">
  <img src="https://github.com/user-attachments/assets/adbecace-d98a-418a-9581-f570303ddbe9" style="width: 100px; margin-right: 20px;">
  <div>
    <strong>Yejin Lee</strong> &lt;Implemented recommendations for wine beginners (“Warin-i”)&gt;<br>
    [About] Used to know only “sparkling / red / white,” but now on the way to becoming a wine knower!
  </div>
</div>

<div style="display: flex; align-items: center;">
  <img src="https://github.com/user-attachments/assets/324420a3-a674-4ee7-ac08-4285dbea6408" style="width: 100px; margin-right: 20px;">
  <div>
    <strong>Jeongseok Shim</strong> Team member<br>
    [About] Wine beginner.
  </div>
</div>

## 🍇 DATA Introduction 🍇

- [**Wine-savvy / Food-savvy Data**](https://www.vivino.com/explore)  
  - Called the API and extracted JSON  
  - **Columns**: 22 columns × 3,675 rows  
    - *wine_ratings_count*: number of ratings  
    - *wine_ratings_average*: average rating  
    - *foods*: food pairings  
    - *vintage_price*: price  
    - *vintage_wine_name*: wine name (name + vintage year)  
    - *vintage_wine_type*: wine type (id mapped to type)  
    - *varietal_name*: grape varietal  
    - *variety*: wine variety  
    - *winery*: winery  
  - **Row Count**  
    - After removing duplicates: `df.shape = (2024, 22)`

- [**Beginner (“Warin-i”) Data**](https://www.kaggle.com/datasets/zynicide/wine-reviews?select=winemag-data_first150k.csv)  
  - **Columns**  
    - *description*: review text  
    - *title*: wine name  
    - *country*: country  
    - *points*: rating  
    - *price*: price  
    - *variety*: variety  
    - *winery*: winery  
  - **Row Count**  
    - After removing duplicates: 29,971 ⇨ 119,928  
  - **Description words**  
    - 68 words used  
    - Words below 5% or above 90% frequency were excluded from vectorization

## 🍇 Development Tools 🍇
(Images unchanged)

## 🍇 Our Recommendation System 🍇

- **Wine-savvy ver.**  
(see screenshot)

- **Beginner (“Warin-i”) ver.**  
“Warin-i” is a portmanteau of “wine + beginner.” Since beginners may not know terms like tannin or acidity, the system asks simple preference questions and recommends wines accordingly.

**[Example] Step 1. Choose what you prefer.**  
1) Meat &nbsp;&nbsp; 2) Fish &nbsp;&nbsp; 3) Vegetables

For each choice, we assign characteristic tags and map them to a subset of our 68 keywords extracted from the model data.

- **Meat**: rich red wines, beef/lamb/steak, juicy, full-bodied, tannic, bold flavors  
  ⇒ [dry, firm, tannins, red, flavor, dark, cabernet, sauvignon]

- **Fish**: white wines, crisp acidity, freshness, seafood  
  ⇒ [fruit, white, crisp, fresh, bright, touch, sauvignon, light]

- **Vegetables**: white / light red, roasted vegetables, salads, fresh, zesty, delicate  
  ⇒ [fruit, white, crisp, fresh, bright, touch, sauvignon, light]

(See screenshots)

- **Food-savvy (“Mat-jal-al”) ver.**  
(see screenshot)

- **Recommendation Results**  
  - **Best 3** (screenshot)  
  - **Worst 3** (screenshot)

## 🍇 Streamlit App 🍇
👇 Click to use the wine recommendation system.

[![image](https://github.com/user-attachments/assets/74016d81-546a-40ba-aaa6-6d9e63995d4b)
](https://da36mini2dionysus-29g5hzkbgzgnskeescxfnc.streamlit.app/)

## 🍇 Demo Video 🍇
👇 Click to watch the implementation demo.

[![Thumbnail](https://github.com/user-attachments/assets/3c4ac3b1-5403-4942-ae89-35263034488f)](https://youtu.be/Fy1aycHWAVM)



