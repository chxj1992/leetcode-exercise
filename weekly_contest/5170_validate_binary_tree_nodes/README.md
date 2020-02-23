## 5180. 验证二叉树

https://leetcode-cn.com/problems/validate-binary-tree-nodes/


#### 解法  

[图论](_1.py)
[层次遍历](_2.py)


#### 分析 

1. 图论知识

结点个数等于-1的个数减1时为树 (edge = vertices - 1)


2. 广度优先遍历

满足无环连通图，即为树。
- 若要满足无环图，遍历过程中不能出现重复结点。
- 若要满足连通图，遍历完成后经过的顶点数需为n个

