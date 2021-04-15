# 文件管理

## 引言

通过 `Python` 脚本，我们可以很方便地批量管理自己电脑中的文件。  
<br>

先回忆一下我们在 `Python 基础练习 3` 中的操作：  

```python
dir_path = 'txt_files'
file_name = 'hongloumeng.txt'
full_path = os.path.join(dir_path, file_name) 
# full_path 是 'txt_files/hongloumeng.txt' 或 'txt_files\\hongloumeng.txt
# 取决于你的操作系统是 Windows 还是 MacOS / Linux

if not os.path.exists(dir_path): # 如果文件夹不存在，就创建文件夹
    os.mkdir(dir_path) # mkdir 是 make directory，即创建文件夹

if not os.path.exists(full_path): # 如果文件不存在，就下载文件
    url = "http://icewould.com/m5-101/hongloumeng"
    print("正在下载文件...")
    result = requests.get(url)
    with open(full_path, "wb") as f:
        f.write(result.content)
        print("下载完成")

```

这段代码，会自动下载文件并创建文件夹，非常方便。  
<br>

文件操作都是在 `os` 包中的，使用的时候，要先 `import os`。  
（`os` 是 `Operating System`，即操作系统的缩写。非技术人员比较常用的是 `Windows` 和 `MacOS`。）  
<br>

## 绝对路径和相对路径
操作文件的时候，这个概念非常重要。  
<br>

比如，你当前的目录是 `D:\python\project2`。在这个目录下，你有一个 `experiment3` 文件夹，其中有一个 `result.txt` 文件。于是，这个文件的绝对路径就是 `D:\python\project2\experiment3\result.txt`，但它的相对路径（相对你当前的路径）就是 `.\experiment3\result.txt`。其中，最开始的 `.` 代表当前目录。  
<br>

你也可以使用 `..` 在相对路径中访问上级目录：  
`D:\python\project1\experiment1\result.txt` 与 `..\project1\experiment1\result.txt`是一样的。  
<br>


## 常用操作
我们列出几个比较常用的方法。各位下次遇到需要创建文件夹、移动文件等操作的时候，可以试试用 `Python` 去进行。  
<br>

### 获取目录和文件夹
- 使用 `os.getcwd()` 获得当前目录的完整路径 (`getcwd`: get current working directory)。
- 使用 `os.listdir(path)` 获得 `path` 目录下的所有文件和文件夹名字。

### 创建或删除文件
- 使用 `os.remove(path)` 删除某个文件。  

### 创建或删除文件夹
- 使用 `os.mkdir(path)` 创建一个文件夹。
- 使用 `os.makedirs(path)` 沿着 `path` 一路从浅到深连续创建文件夹。
<br>

- 使用 `os.rmdir(path)` 删除一个文件夹。
- 使用 `os.removedirs(path)` 沿着 `path` 一路从深到浅连续删除文件夹。
<br>

注意，在删除文件夹的时候，如果文件夹不是空的，就会删除失败。所以删除之前要先清空文件。

### 文件或文件夹改名
- 使用 `os.rename(src, dst)` 把名字是 `src` 的文件名字改成 `dst`。  
<br>

注意，如果 `src` 是一个路径，那么 `dst` 也得是一个路径。

### 文件的移动和复制
我们需要先 `import shutil`   
<br>

- 使用 `shutil.copyfile(src, dst)` 把路径为 `src` 的文件复制到 `dst` 去。
- 使用 `shutil.move(src, dst)` 把路径为 `src` 的文件移动到 `dst` 去。
