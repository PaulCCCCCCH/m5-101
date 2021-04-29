# 网页信息提取

爬虫最基础的功能，是从服务器发送给你的 `HTML` 文件里提取信息。只要是 `HTML` 页面上写的东西，都有办法可以程序自动地、批量地获取。我们就从这一步开始。  
<br>

## `HTML`
`HTML` 由一系列标签组成。标签一般都是成对出现的，被标签包裹的文字，究竟以何种形式展示给用户，是被标签定义的，像这样：  
```html
<h1> 一号字体的标题 </h1>
<div> 
    <h2> 二号字体的标题 </h2>
    <p> 一小段文字 </p>
</div>
<div>
    <h2> 第二个标题 </h2>
    <p> 另一小段文字 </p>
<div>
```

可以暂时不需要知道每个标签对应的意思，只要知道，一般情况下，你要爬取的数据会有规律地出现在标签上，标签中间或标签附近。  

## 提取文本
大部分情况下，我们会爬取文本，也就是直接把 `HTML` 标签包裹的东西拿过来，并保存。
我们可以使用 `BeautifulSoup` 获取标签后，直接使用 `get_text`，获得文字内容。比如上面那段 `HTML` 代码，想从中提取第一个 `<p>` 标签中的内容（`一小段文字`），可以这样：

```python
from bs4 import BeautifulSoup

# html 需要转化成字符串，才能进行处理
html = '<h1> 一号字体的标题 </h1> <div> <h2> 二号字体的标题 </h2> <p> 一小段文字 </p> </div> <p> 另一小段文字 </p>'

soup = BeautifulSoup(html)
div_tag = soup.findAll('div')[1] # 获取第二个 <div> 标签及其全部内容
p = div_tag.p # 获得 <div> 标签下的 <p> 标签

print(p.get_text) # 会打印“另一小段文字”
```

## 提取图片
与文字不同，图片一般会写在标签里，像这样：  

```html
<img src="url_to_image"></img>
```

`src` 属性里头的 `url_to_image` 会指向图片的链接。我们需要提取这个链接，然后下载这个链接的内容，像这样：  

```python
# 假设已经获得了名为 `html` 的字符串变量，用 BeautifulSoup 预处理
soup = BeautifulSoup(html)

# 获得标签上的 `src` 属性的内容，即图片链接
image_url = soup.img.get('src')

# 向对应的链接发送请求，获得数据
data = requests.get(image_url)

# 把数据保存到本地文件（也就是图片）
with open("image.jpg", "wb") as f:
    f.write(data.content)
```


