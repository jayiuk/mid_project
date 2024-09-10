# mid_project
# 야구선수 개인성적 기반 연봉 구간 예측(투수)

## 목차
1. [개요](#1.-개요)
2. [데이터 크롤링](#2.-데이터-크롤링)
3. [EDA1 get_data](#3.-EDA1-get_data)
4. [EDA2 Derived Variable & Data Visualization](#4.-EDA2-Derived-Variable-&-Data-Visualization)
5. [modeling](#5.-modeling)
6. [결론](#6.-결론)


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

