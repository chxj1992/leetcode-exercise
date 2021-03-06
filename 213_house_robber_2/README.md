## 213. 打家劫舍 II

https://leetcode-cn.com/problems/house-robber-ii/


#### 解法  

* [分治法](_1.py)
* [动态规划](_2.py)
* [动态规划2](_3.py)


#### 分析

解法3:

在 [198. 打家劫舍](../198_house_robber) 的基础上可以对本问题做如下分析: 

环状排列意味着第一个房子和最后一个房子中只能选择一个偷窃, 
因此可以把此环状排列房间问题约化为两个单排排列房间子问题: 

1. 在不偷窃第一个房子的情况下, 最优解为 p1
2. 在不偷窃最后一个房子的情况下, 最优解为 p2
​	
max(p1, p2) 即为本问题的解.
