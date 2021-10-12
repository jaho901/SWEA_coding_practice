import sys
sys.stdin = open('input.txt')

# def check_babygin(numbers):
#     counter = [0 for _ in range(10)]
#     is_babygin = 0
#
#     for number in numbers:
#         counter[number] += 1
#
#     idx = 0
#     while idx < len(counter):
#         # print(idx)
#         if counter[idx] >= 3:
#             counter[idx] -= 3
#             is_babygin += 1
#             continue
#
#         if idx < len(counter) - 2:
#             if counter[idx] and counter[idx+1] and counter[idx+2]:
#                 counter[idx] -= 1
#                 counter[idx+1] -= 1
#                 counter[idx+2] -= 1
#                 is_babygin += 1
#                 continue
#
#         if is_babygin == 2:
#             return True
#         idx += 1
#     return False

def baby_gin():
    global flag
    check = 0

    # 1. 연속하는 숫자 3개가 모두 같은경우
    if arr[0] == arr[1] and arr[1] == arr[2]:
        check += 1
    if arr[3] == arr[4] and arr[4] == arr[5]:
        check += 1

    # 2. 연속하는 세 자리수
    if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]:
        check += 1
    if arr[3] + 1 == arr[4] and arr[4] + 1 == arr[5]:
        check += 1

    if check == 2:
        flag = 1
        return

def perm(start, end):
    # 종료 조건
    if start == end:
        baby_gin()
    else:
        for i in range(start, end):
            arr[end], arr[i] = arr[i], arr[end]
            perm(start+1, end)
            arr[end], arr[i] = arr[i], arr[end]

for _ in range(int(input())):
    arr = list(map(int, input()))
    # print(check_babygin(arr))
    flag = 0
    perm(0, 5)
    if flag:
        print(True)
    else:
        print(False)