graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def dfs_error(graph: dict, root: str) -> None:   # 已修正错误
    # visited = set([root, ])
    visited = set([])
    stack = [root, ]
    while stack:
        print("stack: ", stack)
        curr = stack.pop()
        print("pop: ", curr)
        visited.add(curr)
        print("visited: ", visited)
        for neighbor in graph[curr]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)   # 之前出错的原因在于落下的这句话，一旦入栈，说明已经将要被访问
    # print('')

'''
这段代码的输出结果：
stack:  ['A']
pop:  A
visited:  {'A'}
stack:  ['B', 'C']
pop:  C
visited:  {'A', 'C'}
stack:  ['B', 'F']
pop:  F
visited:  {'A', 'F', 'C'}
stack:  ['B', 'E']
pop:  E
visited:  {'A', 'F', 'E', 'C'}
stack:  ['B', 'B']
pop:  B
visited:  {'F', 'E', 'A', 'C', 'B'}
stack:  ['B', 'D']
pop:  D
visited:  {'F', 'E', 'D', 'A', 'C', 'B'}
stack:  ['B']
pop:  B
visited:  {'F', 'E', 'D', 'A', 'C', 'B'}

这段代码的问题在于，没有判断节点是否visited就把它输出了，也就是当B被重复访问时，两次都输出了
所以print节点的步骤也应该判断是否visited（这是下边def dfs()的写法）
或者，在每次遍历neighbor的时候就要标记visited（这是上边error写法的修正）

或者说，stack里边是有可能存在重复节点的，这时候需要判断visited在输出（访问），不能直接从stack里边直接输出
'''

def dfs(graph: dict, root: str) -> None:
    # visited = set([root, ])
    visited = set([])
    stack = [root, ]
    while stack:
        curr = stack.pop()
        if curr not in visited:
            print(curr)
            visited.add(curr)
            for neighbor in graph[curr]:
                stack.append(neighbor)

'''
更改后的输出：
A
C
F
E
B
D
'''

def dfs_by_ChatGPT(graph, start):
    stack = [start]
    visited = set()

    while stack:
        current = stack.pop()
        print(current)
        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
    
    return visited

# Call the DFS function
# dfs(graph, 'A')
dfs_error(graph, 'A')