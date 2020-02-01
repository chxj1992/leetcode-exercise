## 42. 接雨水

https://leetcode-cn.com/problems/trapping-rain-water/


#### 解法  

* [单调栈](_1.py) 
* [按列求和](_2.py)
* [按列求和 + 动态规划优化](_3.py)
* [按列求和 + 双指针优化](_4.py) 


#### 分析

本题详细的解析可以参考[此篇题解](https://leetcode-cn.com/problems/trapping-rain-water/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-8/)

1. 单调栈解法可以结合 [84. 柱状图中最大的矩形](../84_largest_rectangle_in_histogram) 一起练习
2. 每列能保存的水等于该列左右边界中的较小值减当列高度
3. 提前缓存每个位置的左右边界 


