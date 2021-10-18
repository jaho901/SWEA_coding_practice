arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def part(cur, total, cnt):
    if total > 10:
        return
    if total == 10:
        print(*ans)
        return

    for i in range(cnt, len(arr)):
        if not visited[i]:
            ans.append(arr[i])
            visited[i] = True
            part(cur+1, total+arr[i], i+1)
            ans.pop(-1)
            visited[i] = False


ans = []
p = []
print(len(arr))
visited = [False] * len(arr)
part(0, 0, 0)
