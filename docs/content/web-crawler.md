# Project 3: Web Crawler 网络爬虫

## 引言
时光飞逝。转眼间，小王已经大三了。这么多年来，他一直怀有出国读研的梦想。而现在，正是申请研究生的大好时机。只是，他对申研毫无头绪，不知道从什么地方入手：这么多学校，我怎么知道谁家的研究生更适合我呢？我该上哪去搜索相关的信息呢？  
<br>

他去某度搜索“牛津大学数学系研究生申请”，得到的只有铺天盖地的野鸡中介的广告，这让他更加绝望。  
<br>

五一假期聚会的时候，小王听小明说，你是一位会用 `Python` 写程序大佬，上次帮他解决过工作上遇到的难题。于是，经小明的推荐，小王找到了你，希望你能帮帮他。  
<br>

你回想起最近在学习的爬虫，眉头一皱，发现事情可以很简单。一次简单的开发，可以满足很多人的需求。于是，你欣然接下了这个请求<strike>，并且要求小王请自己吃饭</strike>。

## 准备工作
请下载初始代码。（尚未准备好）
[下载链接]()


## Section 1: 页面下载
以牛津的[硕士项目列表](https://www.ox.ac.uk/admissions/graduate/courses/courses-a-z-listing)为例。  
<br>

这个页面上，每一个硕士/博士项目名，都是一个可以点击的超链接。点击进入后，可以看到项目的具体介绍，而这正是我们想要的东西。  
<br>

在这个部分，我们需要把每个**硕士项目**的具体介绍页面的 `html` 文件下载下来，命名为这个项目的名称，保存在本地。  
<br>

提示：  
1. 你可以新创建一个文件夹，叫 `oxford`，运行脚本后，里面有 `advanced-computer-science.html`，`african-studies.html`, `ancient-philosophy.html` 等等几十个文件（注意命名格式，是小写字母 + 短横线）。
2. 我们只关心硕士项目（M 开头的学位）。比如，`Msc`，`MSt`, `MTh`, `MPhil` 等都是我们要下载的，而 `D` 打头的博士学位项目，以及 `PG` 打头的继续教育项目，需要直接跳过。


## Section 2: 微调
我们在以上程序的基础上，进行微调，爬取以下学校的项目介绍，并且每一个大学是一个单独的文件夹。  
- [UIUC](http://catalog.illinois.edu/graduate/)  
- [帝国理工](https://www.imperial.ac.uk/study/pg/courses/)  
- [剑桥大学](https://www.postgraduate.study.cam.ac.uk/courses)  
- [Manchester](https://www.manchester.ac.uk/study/masters/courses/list/)


比较热门的学校可能有一百来所，你打算先拿上面几所学校的网站做个实验，之后找几个同样懂爬虫的朋友，分一下工，大概一两天时间就能把全部热门大学的项目都爬下来。  
<br>

## Section 3: 建立索引
我们已经把数据都下载到本地了。可是，光有数据，其实用处不大；从数据中提取的信息，才有价值。为了让提取信息的过程更加高效，我们要对数据进行**预处理**。  
<br>

正常情况下，我们需要建立一个**关系型数据库**来高效地存储预处理之后的信息，不过这有点点超纲。我们先用普通的文件来存储。  
<br>

想象一下：现在我们手里有大量学校的项目介绍页面。我希望从中搜索所有标题带有 `math` 的项目（这些可能都是我感兴趣的）。为了方便搜索，我该怎么做呢？  
<br>

首先，我们遍历所有文件夹里的所有 `html` 文件。对于其中的每一个文件，我们提取以下信息（JSON 格式，以帝国理工 `Advanced Computer Science 为例`）：  
```json
{
    "document_id": "1",
    "school_name": "Oxford",
    "program_name": "Advanced Computer Science",
    "file_path": "./oxford/advanced-computer-science.html",
    "program_description": "....."
}
```
每一个 `html` 文件都对应这样一个 `json` 格式的数据。  
<br>

之后，请把所有的 `json` 对象放在字典 `program_dict` 变量里，每个对象对应一个唯一的 `document_id`，这会作为字典的 `key`，而 `value` 则是剩下的信息。换句话说，这个字典大概长这样：
```python
{
    1: {
        "document_id": "1",
        "school_name": "Oxford",
        "program_name": "Advanced Computer Science",
        "file_path": "./oxford/advanced-computer-science.html",
        "program_description": "....."
    }, 
    2: {
        "document_id": "2",
        "school_name": "Cambridge",
        "program_name": "Computer Science",
        "file_path": "./cambridge/computer-science.html",
        "program_description": "....."
    }
    # ... 其它的
}

```
<br>


最后，请使用 `python` 自带的 `pickle` 这个库，将 `program_dict` 这个字典变量保存在一个名为 `programs.pkl` 的文件。这就是我们的 `索引`。它的本质，就是以一定格式存放的数据，可以方便我们进行查询。它其实等价于一下这张表：  
<br>

| document_id |school_name| program_name| file_path | program_description |
|-----|-----|-----|----|----|
| 1|Oxford| Advanced Computer Science| ./oxford/advanced-computer-science.html| ... |
| 2|Cambridge| Computer Science| ./cambridge/computer-science.html| ... |
| 3|...|...|...|... |
<br>

注意：`program_description` 字段，即是 `html` 页面的内容。但是，请对它进行处理以下处理：  
- 消除所有 `<script></script>` 标签中间的全部内容。  
- 消除所有 `html` 标签，以及特殊符号。   
- 其它可能的操作（总之，越干净越好，最好只保留文字信息）。  
<br>

如果忘记了怎么用 `python` 管理文件，可以回顾一下[文件管理](../file-management)这一章的内容。如果忘记怎么使用`正则表达式`，可以参考 Week 2 四月一号的内容。
<br>

## Section 4: 项目名查询
索引建立好之后，我们需要另外写一个脚本 `search.py`，方便用户搜索信息。  
<br>

这个脚本的需求如下：  
1. 需要读取 `programs.pkl` 保存的字典。  
2. 需要用 `input` 函数监听用户的输入。  
3. 在字典里面搜索**所有`program_name`包含用户输入**的项目并打印。  
<br>

比如，我想申请数学系的研究生，于是我输入 `math` 这个关键词，程序就会输出所有我可能感兴趣的项目。  
<br>

## Section 5: 内容关键字查询
现在，我想知道，哪些项目可能需要考 `GRE`，哪些需要 `GMAT`，哪些两者都不要。于是，你可能需要列出包含这些关键字的项目信息。  
<br>

稍微思考过后，你觉得可能可以这样做：
```python
1. 读取 programs.pkl，保存在名为 my_dict 的字典变量中（这就是所有 program 的信息）。
2. 对于 my_dict 中的每一个 item （每一个 item 就是每一个 program 的信息）：
    2.1 搜索 item 的 program_description 这一字段，看其中是否包含某些关键词。如果包含，则记录。
3. 返回所有的记录
```

请写一个 `search_key_word.py`，实现以上的查询功能。具体需求如下：  
1. 需要读取 `programs.pkl` （会得到一个`字典`）。  
2. 需要用 `input` 函数监听用户的输入。  
3. 在字典里面搜索**所有`program_description`包含用户输入**的项目并打印。  
<br>

完成之后，请尝试运行，并留意程序运行所耗费的时间。  
<br>

## Section 5: 建立更高效的索引
你也许注意到了，运行上面的程序会花费比较久的时间。如果你真的爬下了所有大学的项目信息，或者有很多关键词想要查询，就可能得花上很久很久。  
<br>

那么，有没有什么办法，加快搜索的速度呢？答案是肯定的，只要你建立一种更为高效的索引。  
<br>

首先，我们要用一个名为 `word_dict` 的 `字典` 变量额外存储这样一张表格（其中 `word` 是这个字典的 `key`）：  

| word | count | occurrences | 
|-----|-----|-----|
| academic | 5 | [1, 4, 5, 8, 9] |
| advantage | 3 | [1, 2, 3] |
| astronomy | 10 | [1, 2, 3, 4, 5, 6, 7, 10, 12, 14] | 
| ... | ... | ... | 
<br>

其中，`word` 是在所有项目里都出现过的单词，`count` 是它们出现过的次数，`occurrences` 记录了单词在哪些页面里面出现过（是一列数字，每个都对应之前的 `document_id`）  
<br>

然后，请用 `pickle` 把之前的 `program_dict` 和 `word_dict` 塞进一个 `tuple` 变量，像这样：
```python
to_save = (program_dict, word_dict)
```

最后，把 `to_save` 保存到 `programs_improved.pkl`。这个**新的索引**可以帮我们更高效地完成搜索。  
<br>

## Section 6: 全局搜索
现在，我们需要实现搜索关键词的功能。请写一个脚本 `search_key_word_improved.py`，重新实现 `Section 5` 的功能。  
<br>

提示：你可以直接在 `word_dict` 搜索一个关键词，得到一列 `document_id`，然后用 `document_id` 去搜索 `program_dict`。  
<br>

做好之后，请再次尝试运行这个程序，看看是不是快了很多！  
<br>

## 总结
在这个项目里，我们完成了一个爬虫项目从数据获取 (`Section 1` 和 `Section 2`)、数据整理 (`Section 3` 和 `Section 5`)以及数据查询 (`Section 4` 和 `Section 6`) 的整个流程。我们可以在流程中加入许多其它的技术，让我们的成果更加有用。我们列出一些可以被优化的方向以及它们的难度（仅供参考），如果大家有兴趣的话，可以深入研究。  

- 数据获取：  
    - （难）我们可以给爬虫加入基础的页面内容判断机制，让它自己适应不同学校的网站，这样就不需要针对每个学校的网页微调自己的爬虫，从而节省劳动力。  
    - （难）我们可以从更广阔的互联网获取信息，而不是只局限于学校的官方网站。  
- 数据整理：  
    - （中等）我们可以使用自然语言处理 (NLP) 的相关技术，对页面的信息进行提取和分析（比如，根据特定关键词的数量和位置，为一个研究生项目打分）。  
    - （简单）我们可以参考搜索引擎相关技术，进一步优化我们的索引。（事实上，我们在这个项目中建立的第二个索引，正是简化了的`倒排索引`，这是搜索引擎中非常常用的索引方法）  
- 数据查询：  
    - （简单）我们可以提供一个更优雅的查询结果展示界面（比如，在建立索引的时候，同时标记单词在文本中出现的位置，这样可以在搜索结果中把关键词高亮展示出来）。  
    - （中等）我们可以加入模糊搜索功能。比如，搜索 `maths`，会出现 `mathematics`，`math` 相关的结果。搜索 `Fibonaci`（一个拼写错误）会出现 `Fibonacci` 的相关结果。  

