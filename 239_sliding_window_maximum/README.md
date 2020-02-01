## 239. 滑动窗口最大值

https://leetcode-cn.com/problems/sliding-window-maximum/


#### 解法  

* [暴力解法](_1.py) 
* [双向队列法](_2.py)


#### 分析

关于本题的双向队列解法, 可以参考 leetcode 官方题解中的这两篇:

[【视频解析】 双端队列滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/solution/shi-pin-jie-xi-shuang-duan-dui-lie-hua-dong-chuang/)
[滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/solution/hua-dong-chuang-kou-zui-da-zhi-by-leetcode-3/)

观看视频对理解算法原理很有帮助. 

Tip: 双向队列始终保持有序, 从队首获取最大元素的索引, 从队尾通过栈的方式维护新增元素

