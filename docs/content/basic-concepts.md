# 基本概念

阅读本教程前，请先确认，你已经完成开发环境搭建（Python 和 `VS Code`的安装），并且可以使用 Python 的 `print` 函数输出 `Hello world` 了。


## 解释器
我们安装了 Python，但这玩意儿到底是啥？  
<br>

先讲答案：Python 是一个`解释器（interpreter）`。这又是啥呢？  
<br>

我们从计算机的底层讲起。  
<br>

计算机本质上不过是一堆用电器堆在一起（用电器嘛，就是灯啊、马达啊这些，通电就工作，不通电就不工作，电流不同，用电器不同，产生的效果不同）。所以，只有改变电流，才能直接控制计算机。  
<br>

我们把有电流称为 `1`，没有电流称为 `0`。  
<br>

我们最终给计算机下的一条条命令，其实长成这样：  
`0010 0000 0010 0010 0000 0001 0101 1110`  
（这句话 32 位长的命令执行了一个加法操作）  
<br>

我们常说的 32 位的系统，意思就是计算机的每条命令有 32 位。64 位的系统，每条命令就是 64 位。就这么简单。  
<br>

但是，这样给计算机下命令太反人类了，如果不查表的话，谁能看懂一串 `0` 和 `1` 到底是啥。所以，我们想用人类能看懂的**英语**写程序，然后把它翻译过去，这样就简单多了。  
<br>

谁来做这个翻译的工作呢？翻译也很麻烦。于是我们打算写一个程序来自动翻译。这个自动翻译的玩意儿就是 `解释器（interpreter）`。  
（P.S. 其实更专业来讲，这个翻译过程还牵扯到`编译器（compiler）`，`链接器（linker）`等一众工具，但入门的话，知道`解释器`就足够啦！）  
<br>

我们下载的 `Python` 就是这样一个 `解释器`。我们通过运行它，把我们的 `.py` 文件翻译成 `0` 和 `1` 的组成的命令，交给计算机。  
<br>

## 编程语言
除了 Python，还有很多不同的编程语言。它们最终都会被自动翻译软件翻译成一堆 `0` 和 `1`。所以本质上，语言之间并没有什么区别。能被一种语言实现的，一定也能被另一种语言实现，只要语言是[图灵完备](https://www.zhihu.com/question/20115374)的。  
<br>

不过，不同语言有不同的特性。比如 Python，它的简洁让它可以胜任数据分析、测试 AI 算法等任务，但它低下的解释效率让它面对密集的信息处理时稍显疲惫。总之，语言之间没有能与不能的区分，只有适合与不适合的差异。


## 编辑器
我们为什么下载 `VS Code` 呢？  
<br>

其实，这不是必须的。你甚至可以直接用记事本写一个 `.py` 文件，然后拿去给 Python 解释、运行。  
<br>

使用 `VS Code`，不过是让它帮你检查你的 Python 语法错误、给你一些提示和帮助，以及把你的代码变得五颜六色而已。


