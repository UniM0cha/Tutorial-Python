import matplotlib.pyplot as plt

# 동아리 회장에 4명이 출마해서 1번~4번까지 번호 투표를 하였다. 후보별 투표 인원을 출력해서 회장을 선출하라.

box = [1, 2, 3, 2, 3, 1, 2, 2, 4, 3, 5, 0, 3, 2, 1]
captain = [0, 0, 0, 0]
invalid = 0

for i in box:
    if 1 <= i <= 4:
        captain[i-1] += 1
    else:
        invalid += 1

print(
    f"1번 후보: {captain[0]}, 2번 후보: {captain[1]}, 3번 후보: {captain[2]}, 4번 후보: {captain[3]}")
print(invalid)

plt.bar(range(0, 4), captain)
plt.show()
