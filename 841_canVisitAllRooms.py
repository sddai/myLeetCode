def canVisitAllRooms(rooms: [[int]]) -> bool:
    # graph = [[] for _ in range(n)]
    visited = set([0])
    queue = [rooms[0]]
    # print(queue)
    while queue:
        curr = queue.pop(0)
        # print("curr", curr)
        for neighbor in curr:
            if neighbor not in visited:  # 注意不要忘了这句判断
                queue.append(rooms[neighbor])
                visited.add(neighbor)
    if len(visited) == len(rooms): 
        return True 
    else: 
        return False
    
print(canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))