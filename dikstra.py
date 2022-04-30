import heapq

def Dijkstra(arr, start):
    q = []
    heapq.heappush(q, arr[start])
    coust = [] * len(arr)
    while q.size() > 0:
        coustNow, pointNow = heapq.heappop(q)
        for i in range(arr[pointNow]):
            if coust[i] is not None \
                or coust[i] > coustNow + arr[i][1]:
                heapq.heappush(q, arr[start])
                coust[i] = coustNow + arr[i][1]
