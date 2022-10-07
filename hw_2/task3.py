def network_delay(times, n, k):
    delay = [float('inf')] * n
    delay[k - 1] = 0
    for i in range(n):
        for u, v, w in times:
            if delay[u - 1] + w < delay[v - 1]:
                delay[v - 1] = delay[u - 1] + w
    return max(delay) if max(delay) < float('inf') else -1
