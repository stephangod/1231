import matplotlib.pyplot as plt

# ⭐ 한글 폰트 설정 (Windows)
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False  # 마이너스 깨짐 방지

# 예시 데이터
hours = [9, 12, 15, 18, 21]
views = [120, 340, 560, 430, 290]

# 그래프 생성
plt.plot(hours, views)

# 제목과 축 설정
plt.title("시간대별 기사 조회 수")
plt.xlabel("시간")
plt.ylabel("조회 수")

# 그래프 출력
plt.show()