# 1 부터 100 까지의 합

tot = 0
count = 1
n = int(input("숫자입력:"))

while (count < 4) and (n > 0):
    tot += n
    n = int(input("숫자입력:"))
    count += 1

print(f"총합은 {tot}이고 개수는 {count}개")
