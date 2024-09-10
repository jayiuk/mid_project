# mid_project
# 야구선수 개인성적 기반 연봉 구간 예측(투수)

## 목차
- [mid\_project](#mid_project)
- [야구선수 개인성적 기반 연봉 구간 예측(투수)](#야구선수-개인성적-기반-연봉-구간-예측투수)
  - [목차](#목차)
  - [1. 개요](#1-개요)
  - [2. 데이터 크롤링](#2-데이터-크롤링)
  - [3. EDA1 get\_data](#3-eda1-get_data)
  - [4. EDA2 Derived Variable \& Data Visualization](#4-eda2-derived-variable--data-visualization)
  - [5. modeling](#5-modeling)


## 1. 개요
- 많은 사람들이 고연봉 운동선수에 대한 의문을 가짐
  - 과연 그 정도를 받을 실력인가에 대한 의문
- 또한 연봉협상 시 선수들은 제대로 비교할 대조군 부족
- 이런 문제를 해결하기 위해 야구선수 연봉 구간 예측 모델 개발



## 2. 데이터 크롤링
- 사용 프레임워크 : Selenium, beautifulSoup
- 크롤링 웹페이지 : [KBO 기록실](https://www.koreabaseball.com/Record/Player/PitcherBasic/Basic1.aspx), [스탯티즈](https://statiz.sporki.com/add/?m=salary)
- 크롤링 범위 : KBO 기록실 - 2019 ~ 2023, 스탯티즈 - 2020 ~ 2024
  - 2019, 데이터는 잘림(2019년은 현재 연봉이 없음)
  - 따라서 남은 데이터는 2020 ~ 2023년 4년치 데이터를 이용

## 3. EDA1 get_data
- 크롤링한 데이터는 연도별로 나뉘어져 있음
- 또한 특정 컬럼은 숫자형으로 되어있어야 할 값이 object로 되어있음
- 이를 해결하기 위해 데이터를 합치고(concat) object를 numeric으로 바꿔줌
  - 이닝에선 1/3, 2/3은 .333, .669로 바꿔준 후 to_numeric
  - 연봉에 ,는 정규표현식을 활용해 ,제거 후 numeric으로 바꿔줌
  - 그 외 모든 데이터도 이와 유사한 방식
- NaN값은 제거
  - NaN값이 있는 경우는 2군으로 내려간 경우, 부상으로 경기를 많이 뛰지 못한 경우가 있기 때문
- 31이닝 이하로 뛴 경우도 삭제
  - 이 이닝 이하로 뛴 선수 기록은 제대로 안쳐줌
  - 즉 이는 이상치가 됨

## 4. EDA2 Derived Variable & Data Visualization
- 원래는 통상적으로 중요하다고 여기는 주요 5개 지표를 토대로 모델링할 계획
  - 하지만 연봉과의 상관관계가 낮게 나옴
  - 또한 모델 성능도 기대 이하로 나옴
  - 파생변수를 만들어 해결하기로 계획
- 파생변수 생성
  - 실제로 사용한 파생변수
    - QS_G : QS성공률. QS/G. QS는 한경기당 하나 까지만 나오기 때문에 이렇게 계산
    - K_BB : K/BB. 볼삼비. 삼진 갯수 / 볼넷 개수. 이를 통해 투수의 제구력을 평가 가능
    - exp_QS : QS기댓값. QS성공률과 QS를 곱함. 이를 통해 QS기댓값 구할 수 있음
    - SO_G : 삼진/경기. 경기당 삼진 계산.
    - RA_9 : 9이닝 당 모든 실점. 모든 실점엔 투수가 관여되어있다는 이론을 수용해 만든 파생변수.
    - K-BB : 삼진률 - 볼넷율. 이를 통해 투수의 제구력 평가
    - NP/IP : 이닝 당 투구수. 효율적인 투수를 확인할 수 있음.
  - 이외에도 많은 파생변수(ex. pFIP)가 있지만 연봉 구간간의 상관계수가 낮아 사용하지 않음
- 후년연봉간의 산점도 그래프
![output10](https://github.com/user-attachments/assets/6c547bba-82a0-43dd-a560-a692bfb3d79a)
  - 이를 통해 선형의 관계인지 확인
- 후년연봉구간간의 상관계수 히트맵
![output11](https://github.com/user-attachments/assets/07861ec3-3ad8-4c78-aec3-7c55d82c797e)
  - 이를 통해 정확한 수치로 선형성을 띄는지 확인
- 상관계수가 0.4 이상인 지표를 사용
  - 후년연봉 자체가 이미 주관적인 지표가 끼어있어 더 높은 상관계수가 잘 나오지 않음
  - 또한 ERA같은 투수를 평가하는 보편적인 지표들이 탈락할 수 있음
    - ERA, WHIP는 MVP를 뽑는 데에도 쓰이는 지표

## 5. modeling
