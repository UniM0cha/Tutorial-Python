# 등수 구하기

tot = [60, 0, 70, 60, 70, 80, 100, 60, 80, 100]
rank = [0]*101

for i in range(0, len(tot), 1):
    [tot[i]] += 1
