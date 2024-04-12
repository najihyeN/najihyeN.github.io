---
title: 알고리즘1
date: 2024-04-11 00:00:00 +09:00
categories: [py,알고리즘]
---
```python
# 입력으로 첫 번째 줄에 수열의 길이 N을 받습니다.
N = int(input())
# A라는 이름의 수열의 리스트를 만들어, 0으로 N개 만큼 초기화합니다.
A = [0]*N

# 입력으로 받은 수열의 각 원소를 A 리스트에 저장합니다. (N만큼 돌림)
for i in range(N):
    A[i] = int(input())

# 스택을 사용하기 위한 빈 리스트를 만듭니다.
stack = []
# 스택에 차례대로 넣을 자연수를 나타내기 위한 변수를 1로 시작합니다.
num = 1
# 결과를 저장할 변수입니다. 처음에는 True로 설정합니다.
result = True
# 스택의 push와 pop 연산을 문자열로 저장할 변수입니다.
answer = ""

# 수열의 각 원소에 대해 반복문을 실행합니다.
for i in range(N): #변수의 길이
    su = A[i]
    # 현재 수열의 값이 num보다 크거나 같으면 스택에 push 연산을 수행합니다.
    if su >= num:
        # su가 num 이상이 될 때까지 반복하여 스택에 push합니다.
        while su >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        # 수열의 값을 만족시키기 위해 마지막에 push한 값을 pop합니다.
        stack.pop()
        answer += "-\n"
    else: # 현재 수열의 값이 num보다 작으면 스택에서 pop 연산을 수행합니다.
        n = stack.pop()
        # 스택의 가장 위의 값이 현재 수열의 값보다 크면 수열을 만들 수 없습니다.
        if n > su:
            print("NO")
            result = False
            break
        else: # 수열을 만들 수 있으면 계속해서 pop 연산을 기록합니다.
            answer += "-\n"

# 모든 과정이 끝나고 수열을 만들 수 있다면, 수행한 연산을 출력합니다.
if result:
    print(answer)
```
03-5 스택과 큐 예제