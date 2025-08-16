<ol><li><a href="http://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-03a72/tu-lun-ji--d55b2/" class="" xt-marked="ok">图论算法基础</a></li><li><a href="http://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-03a72/er-fen-tu--73400/" class="" xt-marked="ok">二分图判定算法及应用</a></li><li><a href="http://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-03a72/huan-jian--e36de/" class="" xt-marked="ok">环检测/拓扑排序算法及应用</a></li><li xt-marked="ok"><a href="https://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-03a72/bing-cha-j-323f3/" class="" xt-marked="ok">并查集算法及应用</a></li><li><a href="http://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-03a72/kruskal-zu-e6b5b/" class="" xt-marked="ok">Kruskal 最小生成树算法及应用</a></li><li><a href="http://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-03a72/prim-zui-x-0ef51/" class="" xt-marked="ok">Prim 最小生成树算法及应用</a></li><li><a href="http://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-03a72/dijkstra-s-6d0b2/" class="" xt-marked="ok">Dijkstra 算法模板及应用</a></li></ol>

# 图的遍历框架
```python
# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码不保证正确性，仅供参考。如有疑惑，可以参照我写的 java 代码对比查看。

# 记录被遍历过的节点
visited = []
# 记录从起点到当前节点的路径
onPath = []

""" 图遍历框架 """
def traverse(graph, s):
    if visited[s]:
        return
    # 经过节点 s，标记为已遍历
    visited[s] = True
    # 做选择：标记节点 s 在路径上
    onPath[s] = True
    for neighbor in graph.neighbors(s):
        traverse(graph, neighbor)
    # 撤销选择：节点 s 离开路径
    onPath[s] = False
```

# 拓扑排序
拓扑排序相当于把一张图“拉平”，按照顺序输出。而且这个「拉平」的图里面，所有箭头方向都是一致的。
**将后序遍历的结果进行反转，就是拓扑排序的结果。**——注意，这跟前序遍历不一样。

那么为什么后序遍历的反转结果就是拓扑排序呢？

# 环检测的dfs算法

# 环检测的bfs算法
每次循环找到入度为0的点向下做bfs，他的邻居节点入度减一，直到找不到入度为零的节点。
此时，如果还有节点没有被遍历，说明有环：想象三个节点首尾相连，此时，任何一个节点的入度都不等于0，则这三个节点都不能被遍历到。