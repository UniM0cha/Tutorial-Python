def solution(numbers):
    array = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            a = numbers[i]+numbers[j]
            if (j != i) & (a not in array):
                array.append(numbers[i]+numbers[j])
    array.sort()
    return array


numbers = [2, 1, 3, 4, 1]
print(solution(numbers))
