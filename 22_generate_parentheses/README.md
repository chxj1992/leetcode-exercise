## 22. 括号生成

https://leetcode-cn.com/problems/generate-parentheses/


#### 解法  

* [动态规划](_1.py)
* [闭合数(递归)](_2.py)
* [回溯法](_3.py)


#### 分析 

关于本次的解析可以参考此篇[题解](https://leetcode-cn.com/problems/generate-parentheses/solution/hui-su-suan-fa-by-liweiwei1419/).

其中, 动态规划解法关键在于找到状态转移方程:
```
dp[i] = "(" + dp[j] + ")" + dp[i- j - 1] , j = 0, 1, ..., i - 1
```

另外, 关于闭合数的解法可以阅读[官方题解](https://leetcode-cn.com/problems/generate-parentheses/solution/gua-hao-sheng-cheng-by-leetcode/)中的解析,
究其根本还是利用了 `dp[i] = "(" + dp[j] + ")" + dp[i- j - 1]` 这一公式, 通过递归实现算法.
