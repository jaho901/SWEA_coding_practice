import sys
sys.stdin = open('5204.txt')

# 반씩 나누면서 가장 적게 나눠졌을 때 그때부터 합치며 정렬하는 함수로 전달
def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    # 재귀로 계속해서 나눈다.
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)


def merge(left, right):
    global cnt
    # 왼쪽과 오른족의 개수를 저장
    left_N, right_N = len(left), len(right)
    # 정렬된 값을 넣을 result값
    result = [0] * (left_N + right_N)
    # 왼쪽과 오른쪽의 인덱스
    left_i, right_i = 0, 0
    # i는 result에 넣기위한 인덱스
    i = 0
    # 오른쪽 원소가 먼저 복사되는 경우의 수를 cnt로 전달
    if left[-1] > right[-1]:
        cnt += 1
    # 왼쪽과 오른쪽 둘중 하나라도 끝까지 가지 않았을때만 반복
    while left_i != left_N and right_i != right_N:
        # 오른쪽 값이 더 큰 경우
        if left[left_i] <= right[right_i]:
            # 왼쪽 값을 result에 넣고 인덱스는 1씩 추가
            result[i] += left[left_i]
            i += 1
            left_i += 1
        # 왼쪽 값이 더 큰 경우
        else:
            # 오른쪽 값을 result에 넣고 인덱스는 1씩 추가
            result[i] += right[right_i]
            i += 1
            right_i += 1
    
    # 왼쪽이나 오른쪽 한쪽에서 미리 다 result에 넣어진 경우
    # 왼쪽값이 남은 경우
    if left_i != left_N:
        # 왼쪽이 끝까지 다 넣어질때까지 반복
        while left_i != left_N:
            # result에 남은 왼쪽값을 순서대로 넣음
            result[i] += left[left_i]
            i += 1
            left_i += 1
    # 오른쪽 값이 남은 경우
    if right_i != right_N:
        # 오른쪽이 끝까지 다 넣어질때까지 반복
        while right_i != right_N:
            # result에 남은 오른쪽값을 순서대로 넣음
            result[i] += right[right_i]
            i += 1
            right_i += 1
    return result


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    data = list(map(int, input().split()))
    cnt = 0
    data = merge_sort(data)

    # data[N//2]를 통해 N//2번째 원소를 보여주며 cnt를 통해 우측원소가 먼저 복사된 경우의 수를 보여줌
    print('#%d %d %d'%(tc, data[N//2], cnt))