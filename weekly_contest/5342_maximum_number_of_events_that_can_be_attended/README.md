## 5342. 最多可以参加的会议数目

https://leetcode-cn.com/problems/maximum-number-of-events-that-can-be-attended/


#### 解法  

[贪心算法](_1.py)


#### 分析

1. 贪心算法 

思路: 优先选择结束时间早的会议. 具体逻辑为: 将会议按结束时间升序排列后遍历会议, 如果当前会议可以参加就安排上.