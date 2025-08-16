class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [dict() for _ in range(n + 1)]
        for u, v, time in times:
            graph[u][v] = time
        dist_to = [float("inf")] * (n + 1)
        dist_to[k] = 0
        pq = [(0, k)]
        while pq:
            curr_dist, curr_node = heapq.heappop(pq)
            # dist_to[curr_node] = 
            for neighbor in graph[curr_node].keys():
                next_dist = dist_to[curr_node] + graph[curr_node][neighbor]
                if next_dist < dist_to[neighbor]:
                    dist_to[neighbor] = next_dist
                    heapq.heappush(pq, (graph[curr_node][neighbor], neighbor))  # 【出错位置】只有当当前总路径和满足条件可以更新的时候，才需要heappush，所以heappush在if里边
        res = max(dist_to[1:])
        return res if res != float("inf") else -1
