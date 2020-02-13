## 152. 乘积最大子序列

https://leetcode-cn.com/problems/maximum-product-subarray/


#### 解法  

* [动态规划](_1.py)
* [符号判别法](_2.py)


#### 分析

1. 动态规划

保存截止当前元素子序列乘积的最大值和最小值, 因为当遇到负数时, 其与最小值的乘积可能变为最大值.

更详细的思路可以参考[这篇题解](https://leetcode-cn.com/problems/maximum-product-subarray/solution/hua-jie-suan-fa-152-cheng-ji-zui-da-zi-xu-lie-by-g/)


2. 符号判别法 

* 当数组里有偶数个负数时, 全部相乘结果最大;
* 当数组里有奇数个负数时, 取除去两侧的某一个负数后乘积较大的一个
* 当遇到 0 则重置
