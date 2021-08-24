import sys
sys.stdin = open('input.txt')

def match(data, left, right):
    # 왼쪽 오른쪽이 같아 질때까지 반복
    if left == right:
        # 왼쪽 오른쪽 상관 X
        return left

    # 문제 상에 중간 값을 나누기 위한 조건
    mid = (left + right) // 2

    # 앞 그룹 (시작점부터 중간값 까지)
    first_group = match(data, left, mid)
    # 뒷 그룹 (중간값+1 부터 끝까지)
    second_group = match(data, mid+1, right)
    
    # 위에 작성한 if문을 통해 반환될 두 그룹으로 가위바위보
    # 1은 가위, 2는 바위, 3은 보

    # 두 값이 같을 경우 왼쪽을 승자로 친다.
    if data[first_group] == data[second_group]:
        return first_group

    # 앞 사람이 가위를 냈다.
    if data[first_group] == 1:
        if data[second_group] == 2:
            return second_group
        else:
            return first_group

    # 앞 사람이 바위를 냈다.
    if data[first_group] == 2:
        if data[second_group] == 3:
            return second_group
        else:
            return first_group

    # 앞 사람이 가위를 냈다.
    if data[first_group] == 3:
        if data[second_group] == 1:
            return second_group
        else:
            return first_group


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    # 데이터, 시작 idx, 끝 idx
    result = match(data, 0, N-1)


    print('#{} {}'.format(tc, result+1))




