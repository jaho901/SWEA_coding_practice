import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    number = input()
    # numbers라는 list 들고오기
    numbers = list(number)
    # numbers 정렬시키기
    numbers = sorted(numbers)

    # 최종 결과값
    result = []

    # 숫자 개수 구하는 용으로 새로운 list 만들기
    cot = [0] * 10
    # 반복문 사용하여 개수 채우기
    for i in numbers:
        cot[int(i)] += 1

    # 조건문을 통해 가장 큰 수가 존재하면 그 수 반환
    # maximum 저장

    count_idx = []


    # 최댓값이 한개인 경우 그 값의 인덱스와 개수를 반환
    if cot.count(max(cot)) == 1:

        # result 0번째는 최댓값의 인덱스와 1번째는 최댓값을 넣어줬다.
        result.append(cot.index(max(cot)))
        result.append(max(cot))

    # 최댓값이 한개 이상인 경우
    elif cot.count(max(cot)) > 1:
        # 반복문을 사용해 최댓값이 존재하는 위치에 해당 인덱스를 반환
        # 아닌 경우에 0을 반환하는 새로운 리스트 생성
        for i in range(len(cot)):
            if cot[i] == max(cot):
                count_idx.append(i)
            else:
                count_idx.append(0)

        # result 0번째는 최댓값의 인덱스와 1번째는 최댓값을 넣어줬다.
        result.append(max(count_idx))
        result.append(max(cot))

    '''
    for tc in range(1, T+1):
        n = int(input())
        cards = list(map(int, input()))
        card_list = [0]*10
        
        # 카드 수를 카운팅
        for card in cards:
            card_list[card] += 1
            
        # 제일 큰 숫자가 있는 위치를 idx로
        # 반복문을 사용하게 되면 정해진 범위를 알아서 순회하고 끝
        idx = 0
        max_idx = 0
        while idx != 10:
            # 카드 리스트에는 카드 장수가 요소로 들어있음.
            # 카드 장수 비교해서 더 많은 중복된 카드들 찾는게 목적
            # 같은 장수를 가지고 있더라도 idx가 더 높은 쪽이 더 높은 숫자
            if card_list[idx] >= card_list[max_idx]:
                max_idx = idx
            # 인덱스 조정
            idx += 1            
    
        print('#{0} {1} {2}'.format(tc, max_idx, card_list[max_idx])
    '''


    print('#{0} {1} {2}'.format(tc, result[0], result[1]))







