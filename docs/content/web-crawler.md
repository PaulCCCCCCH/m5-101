# Project 3: Web Crawler 网络爬虫

## 引言
时光飞逝。转眼间，小王已经大三了。这么多年来，他一直怀有出国读研的梦想。而现在，正是申请研究生的大好时机。只是，他对申研毫无头绪，不知道从什么地方入手：这么多学校，我怎么知道谁家的研究生更适合我呢？我该上哪去搜索相关的信息呢？  
<br>

他去某度搜索“牛津大学数学系研究生申请”，得到的只有铺天盖地的野鸡中介的广告。听小明说，你是一位会用 `Python` 写程序大佬，上次帮他解决过工作上遇到的难题。于是，经小明的推荐，小王找到了你，希望你能帮帮他。  
<br>

你回想起最近在学习的爬虫，眉头一皱，发现事情可以很简单。一次简单的开发，可以满足很多人的需求。于是，你欣然接下了这个请求<strike>，并且要求小王请自己吃饭</strike>。

## 准备工作
请下载初始代码。
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

你打算先拿上面几所学校做一下实验。比较热门的学校可能有一百来所，你打算找几个同样懂爬虫的朋友，分一下工，大概一天时间就能全部爬下来。  
<br>

## Section 3: 建立简单索引
光有数据，其实用处不大；从数据中提取的信息，才有价值。为了让提取信息的过程更加高效，我们要对数据进行**预处理**。  
<br>

正常情况下，我们需要建立一个**关系型数据库**来高效地存储预处理之后的信息，不过这有点点超纲。我们先用普通的文件来存储。  
<br>

首先，我们遍历所有文件夹里的所有 `html` 文件。对于其中的每一个文件，我们提取以下信息（JSON 格式，以帝国理工 `Advanced Computer Science 为例`）：  
```json
{
    "school_name": "Oxford",
    "program_name": "Advanced Computer Science",
    "file_path": "./oxford/advanced-computer-science.html",
    "program_description": "....."
}
```
每一个 `html` 文件都是这样一个 `json` 文件。请把所有的 `object` 保存下来，放在一个名为 `programs.json` 的文件。  
<br>

注意：`program_description` 字段，即是 `html` 页面的内容。但是，请进行处理以下处理  
- 消除所有 `<script></script>` 标签中间的全部内容。  
- 消除所有 `html` 标签，以及特殊符号。   
- （总之，越干净越好，最好只保留文字信息）。  
<br>

如果忘记了怎么用 `python` 管理文件，可以回顾一下[文件管理](../file-management)这一章的内容。  
<br>

## Section 4: 项目名查询
索引建立好之后，我们需要另外写一个脚本 `search.py`，方便用户搜索信息。  
<br>

这个脚本的需求如下：  
1. 需要读取 `programs.json` 的所有内容，保存成一个 `字典`。  
2. 需要用 `input` 函数监听用户的输入，然后。  
3. 在字典里面搜索**所有`program_name`包含用户输入**的项目并打印。  
<br>

比如，我想申请数学系的研究生，于是我输入 `math` 这个关键词，程序就会输出所有我可能感兴趣的项目。  
<br>

## Section 5: 建立进一步索引



## Section 6: 全局搜索


