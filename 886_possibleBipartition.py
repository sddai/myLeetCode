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

"""
        graph = [[ ] for _ in range(n)]   # 要注意这里的初始化：不能初始化为0，而应该初始化为空，因为0也代表一个节点
        for i in range(len(dislikes)):
            graph[dislikes[i][0]-1].append(dislikes[i][1]-1)
            graph[dislikes[i][1]-1].append(dislikes[i][0]-1)  # 无向图，双向边一致
        color_map = [0 for _ in range(n)]
        queue = []
        for i in range(len(color_map)):
            if color_map[i] == 0:
                color_map[i] = 1     # 这个点是遍历二分图的起点
                # color_map[i] = color # 染色为+1
                queue.append(i)
                # for i in range(len(graph)):
                while queue:
                    curr = queue.pop(0)
                    for neighbor in graph[curr]:
                        if color_map[curr] == color_map[neighbor]:
                            return False
                        if color_map[neighbor] == 0:
                            # color = -color   
                            # 不要用一个变量保存当前的color，因为新的染色与上一个染的颜色无关，而与一条边关联的节点颜色有关
                            color_map[neighbor] = -color_map[curr]
                            queue.append(neighbor)
        return True
"""