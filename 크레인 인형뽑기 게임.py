def solution(board, moves):
    stack = []
    count = 0
    # 크레인 구현
    for x in moves:
        # 크레인 내리기
        y = 0
        while board[y][x-1] == 0:
            if y+1 == len(board):
                break
            y += 1
        # 스택에 추가
        if board[y][x-1] != 0:
            if stack and stack[-1] == board[y][x-1]:
                stack.pop()
                count += 2
            else:
                stack.append(board[y][x-1])
        board[y][x-1] = 0
    return count



board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves))
