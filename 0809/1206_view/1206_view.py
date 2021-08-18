import sys
sys.stdin = open('input.txt')
# 아래에 코드 작성
# 총 10개의 케이스가 존재함으로 T를 10으로 잡아준다.
T = 10
for tc in range(1, T+1):
    width = input()
    height = list(map(int, input().split()))

    # 최종 결과값
    result = 0

    length = len(height)
    # 양쪽 길이 2씩은 전부 0의 값을 가지므로 범위 조정하자!
    for i in range(2, length-2):
        #  왼쪽 2개의 max값과 오른쪽 2개의 max값보다 현재 위치 건물의 높이가 더 크면
        #  양쪽 2개씩의 총 4개의 건물 중 max값과의 차이를 result에 더한다.
        if height[i] > max(height[i-1], height[i-2]) and height[i] > max(height[i+1], height[i+2]):
            result += height[i] - max(height[i-1], height[i-2], height[i+1], height[i+2])

    print('#{0} {1}'.format(tc, result))