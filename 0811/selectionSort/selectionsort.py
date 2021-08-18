# 선택 정렬
def select_sort(a):
    for i in range(0, len(a)-1):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


number = [123, 2398, 1, 48, 292, 22]
print(select_sort(number))


# k번째로 작은 원소 찾기
def select_k(list, k):
    for i in range(0, k):
        min_idx = i
        for j in range(i+1, len(list)):
            if list[min_idx] > list[j]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
    return list[k-1]
number = [123, 2398, 1, 48, 292, 22]
print(select_k(number, 4))