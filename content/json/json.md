# JSON —— 超时空胶囊

在互联网上传输消息，目前最常用的格式是用 JavaScript Object Notion，或 `JSON`。  
<br>

它就像是一个胶囊，你把数据塞进去，然后它就可以通过网络，“嗖”的一下飞到别人电脑上（当然，也有 `XML` 之类的胶囊可以用）。  
<br>

简单来说，`JSON` 就是 `JavaScript` 版的 `Python` 字典，即很多很多键值对(`key-value pairs`) 堆在一起，像下面这样：
```json
{
    "name": "Paul Chen",
    "age": 22,
    "city": "Shanghai",
    "birthdate": "November 27 1998"
}
```
这里，每个索引 (`key`) 是一个字符串或数字，每个值 (`value`) 也是字符串或数字。  
<br>

像 `Python` 的字典一样，`JSON` 也可以像下面这样嵌套：
```json
{
    "name": "Paul Chen",
    "age": 22,
    "city": "Shanghai",
    "birthdate": {
        "year": 1998,
        "month": 11,
        "day": 27
    }
}
```

`JSON` 也可以囊括数组，这样就可以记录一个表格的信息：  
```json
{
    "TAs": [
    {
        "name": "Paul Chen",
        "age": 22,
        "city": "Shanghai",
        "birthdate": "November 27 1998"
    },
    {
        "name": "皮",
        "age": 100,
        "city": "Mars",
        "birthdate": "Feburary 31 19998"
    },
    {
        "name": "Kobe",
        "age": 3,
        "city": "The Wild Rift",
        "birthdate": "Jan 1 1BC"
    }
    ]
}
```

使用 `Python` 自带的 `json` 库可以很方便地把字典转化成 `JSON`：  
```python
import json
my_dict = {"name": "Paul Chen", "age": 22, "city": "Shanghai", "birthdate": "November 27 1998"}
my_json = json.dumps(my_dict)
```

也可以把从服务器那里拿到的 `JSON` 当成字典去使用（可以复制这段代码运行一下试试看）：  
```python
import json
import requests

response = requests.get("http://icewould.com:5201/getProduct?id=1") # 向服务器发送请求
my_dict = response.json() # 把返回的消息处理成 python 的字典

print(my_dict)
print(my_dict["name"])
```

这在与服务器交互的时候会经常用到，在编写爬虫脚本的时候也可能会涉及。
