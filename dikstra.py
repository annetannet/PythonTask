import heapq

def Dijkstra(arr, start):
    q = []
    heapq.heappush(q, (0, start))
    coust = [0] * len(arr)
    while len(q) > 0:
        coustNow, pointNow = heapq.heappop(q)
        nextPoints = arr[pointNow]
        for i in range(len(nextPoints)):
            if coust[i] == 0 \
                or coust[i] > coustNow + nextPoints[i][1]:
                heapq.heappush(q, nextPoints[i])
                coust[i] = coustNow + nextPoints[i][1]
