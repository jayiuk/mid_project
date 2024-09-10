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
- 



## 2. 데이터 크롤링
- 사용 프레임워크 : Selenium, beautifulSoup
- 크롤링 웹페이지 : [KBO 기록실](https://www.koreabaseball.com/Record/Player/PitcherBasic/Basic1.aspx), [스탯티즈](https://statiz.sporki.com/add/?m=salary)
- 크롤링 범위 : KBO 기록실 - 2019 ~ 2023, 스탯티즈 - 2020 ~ 2024
- 