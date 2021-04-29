# 递归

> 递归就是包子馅的包子，它的极限是馒头 (Yang, 2016)
> https://www.zhihu.com/people/burea

当一个函数在内部调用了自己，那么可以把这个函数叫做**递归函数**。我们先来看一个例子：  

```python
# 用来计算 1 + 2 + ... + n 的和
def calc_sum(n):
    # 如果 n 是 1 的话，和就是 1
    if n == 1:
        return 1

    # 不然的话，返回的值是当前的 n 加上以 n-1 作为参数调用自己的返回值
    return n + calc_sum(n - 1)
```

这有一点点像我们接触的数学归纳法。`n == 1` 的时候`return 1`， 这是 `base case`，就像是第一个多米诺骨牌，而 `n + calc_sum(n - 1) ` 就是让多米诺骨牌接连倒地的 `recursive step`。  
<br>

当我们运行 `calc_sum(10)` 的时候，其实是在进行如下的推演：
$$
\begin{align}
    \text{calc_sum(10)} &= 10 + \text{calc_sum(9)}  \\
    &= 10 + 9 + \text{calc_sum(8)}  \\
    &= 10 + 9 + 8 + \text{calc_sum(7)}  \\
    &= ... \\
    &= 10 + 9 + 8 + ... + 2 + 1 \\
    &= 55
\end{align}
$$
但是，如果输入一个很大的 `n`，`calc_sum` 就会超出 `max recursion depth`，从而停止运行（可以试试看）。  
<br>

因为每次函数调用，程序都要创建一个新的变量空间，这是相当消耗内存的。这一点是在使用递归的时候必须要注意的。不理解的话，可以把这段代码放到第一周的[在线 Python 运行器](http://pythontutor.com/composingprograms.html)里跑一下。  
<br>

由于任何递归的函数，必然都能用非递归的函数代替，所以很多时候，为了提升性能，我们会避免使用递归。  
<br>

但是，使用递归，的确可以简化代码，让我们更容易实现一些功能。在本周的练习中，大家就可以感受到这一点。  
<br>

