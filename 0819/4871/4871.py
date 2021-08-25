import sys
sys.stdin = open('input.txt')


# 주어진 경로로부터 1과 0으로 이루어진 행렬 생성
def make_arr(course):
    global V
    global E
    arr = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        # 단방향 이동이기 때문에 아래와 같이 지정
        arr[course[i * 2]][course[i * 2 + 1]] = 1
    return arr


def solution(arr, final_course):
    global V
    visited = [0] * (V+1)
    i = final_course[0]
    visited[i] = 1
    stack = []
    # 동일한 방법으로 반복문 실행
    while i != 0:
        for w in range(len(arr[0])):
            if arr[i][w] == 1 and visited[w] == 0:
                stack.append(i)
                i = w
                # i값을 계속해서 최신화 시켜주면서 그 값이 도착점에 도착하면 1을 반환
                if i == final_course[1]:
                    return 1
                visited[i] = 1
                break

        else:
            if stack:
                i = stack.pop()
            else:
                i = 0
                return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    course = []
    
    # 경로를 한 줄로 생성
    for i in range(E):
        sub_s, sub_g = map(int, input().split())
        course.append(sub_s)
        course.append(sub_g)
    # print(course)
    # 최종 출발점과 도착점 생성
    final_course = list(map(int, input().split()))
    # print(final_course)
    # 함수를 사용해 원하는 배열 생성
    arr = make_arr(course)

    # 위의 배열과 최종 경로를 넣고 최종 결과 생성
    print('#{} {}'.format(tc, solution(arr, final_course)))

    

