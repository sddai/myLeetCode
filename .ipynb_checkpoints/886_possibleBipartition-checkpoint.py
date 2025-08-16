def possibleBipartition( n: int, dislikes: [[int]]) -> bool:
    # graph = [ [0] for _ in n+1]  
    #这里要先构建出来一个图数据结构，即：新建一个graph     
    graph = [ [] for _ in range(n)] 
    # 然后把dislike数组改写成graph的格式：
    for a, b in dislikes:
        graph[a-1].append(b-1) 
        graph[b-1].append(a-1)  
    colors = [0] * n
    queue = []
    for i in range(n):
        if colors[i] == 0:     # 避免有孤立点的存在（不连通的其他点）
            queue.append(i)
            colors[i] = 1
            while len(queue) > 0:
                currNode = queue.pop(0)
                for neighbor in graph[currNode]:
                    if colors[neighbor] == colors[currNode]:
                        return False
                    if colors[neighbor] == 0:
                        colors[neighbor] = -colors[currNode]
                        queue.append(neighbor)
    return True

print(possibleBipartition(4,[[1,2],[1,3],[2,4]]))