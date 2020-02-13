## 45. 跳跃游戏 II

https://leetcode-cn.com/problems/jump-game-ii/


#### 解法  

* [递归 + 缓存](_1.py)
* [动态规划](_2.py)
* [贪心算法1](_3.py)
* [贪心算法2](_4.py)


#### 分析

贪心算法思路: 

贪心算法1: 找出能到达最后一个点的距离最远的点, 再找能到达这个点的最远的前一个点, 不断迭代直到到达起点

贪心算法2: 每次在可跳范围内选择可以使之跳得更远的位置
