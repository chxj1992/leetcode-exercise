## 53. 最大子序和

https://leetcode-cn.com/problems/maximum-subarray/


#### 解法  

* [Kadane算法](_1.py)
* [贪心算法](_2.py)


#### 分析 

1. Kadane算法

最大子数列问题最早于1977年提出, 直到1984年卡内基梅隆大学的 Jay Kadane 才提出了该问题的线性算法.
更多细节详见维基百科[最大子数列问题](https://zh.wikipedia.org/wiki/%E6%9C%80%E5%A4%A7%E5%AD%90%E6%95%B0%E5%88%97%E9%97%AE%E9%A2%98)

可以用动态规划的思路来理解Kadane算法. 结合代码:  

如果 max_here > 0，则说明 max_here 对截止当前元素的结果有增益效果，则 max_here 保留并加上当前遍历数字
如果 max_here <= 0，则说明 max_here 对截止当前元素的结果无增益效果，需要舍弃，则将 max_here 直接更新为当前遍历数字


2. 贪心算法

迭代求和, 将问题转化为求最大差问题. 可结合 [121. 买卖股票的最佳时机](../121_best_time_to_buy_and_sell_stock) 一起思考.