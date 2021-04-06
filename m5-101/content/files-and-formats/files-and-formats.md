# 文件和格式

当你使用电脑（`Windows` 或者 `macOS` 操作系统）或手机（`Android` 或者 `iOS` 操作系统）点击打开一个文件的时候，有没有想过，这中间发生了什么呢？  
<br>

你有没有想过，`.jpg` 和 `.png` 文件到底是什么，有什么区别？  
<br>

为了处理数据，我们可能得先知道一下这些原理。  

## 程序的组成
首先，请回顾一下我们在[基本概念](../basic-concepts)中提到的，计算机只能接受 `1` 和 `0` （二进制）组成的指令（机器码）。任何语言书写的程序，都会被先翻译成 `1` 和 `0` 组成的指令，然后才能执行。  
<br>

但是，程序不只包含指令，还包含数据。让我们拿王者荣耀（一个超级复杂的程序）作为例子：  
<br>

当你被打了一下，你会损失生命值，我们来猜测一下它的实现方式。  
<br>

注意以下几点：  
- 这可以看作是不能运行的 `伪代码`，或者代码框架，用来给人读，而不能直接运行；  
- 程序里有很多我们并没有定义的函数，大家可以根据函数名猜测一下它大概是做什么的。这是很重要的**抽象**思想，在之后我们会讲解到；  
- 类似于 `victim.getArmor()` 这样的语法，可以类比一下字符串的 `someString.split()`。`someString.split()` 会把 `someString` 拿过来作为参数，然后输出相关的东西（分割好的字符串列表）；同理，`victim.getArmor()` 会把 `victim` 变量拿来作为参数，输出 `victim` 的当前护甲；  
- 我们只考虑物理伤害；  
<br>

```python
def calculateRealDamage(baseDamage, armorPenFlat, armorPenPercent, armor):
    """
    根据伤害和护甲计算真实伤害
    baseDamage: 技能描述上写的基础伤害
    armorPenFlat: armor penetration flat，攻击者的固定护甲穿透
    armorPenPercent: armor penetration percent，攻击者的百分比护甲穿透
    armor: 被攻击者的护甲
    """ 
    realArmor = (armor - armorPenFlat) - armor * armorPenPercent # 经过穿透后的剩余护甲
    damageReduction = realArmor / (realArmor + 600) # 伤害减免的比例
    
    realDamage = damage * (1 - damageReduction)
    return realDamage

def attack(attacker, ability, victim):
    """
    attacker: 攻击的人
    ability: 攻击的人使用的技能
    victim: 被攻击的人
    """
    baseDamage = ability.getDamage(attacker) # 根据攻击者的属性计算技能基础伤害
    realDamage = calculateRealDamage(baseDamage, attacker.getArmorPenFlat() ,attacker.getArmorPenPercent(), victim.getArmor()) # 调用 calculateRealDamage 计算真实的伤害

    life = victim.getLife() # 获取被攻击者生命值
    newLife = life - realDamage
    if newLife <= 0:  # 如果被攻击者生命值降到 0 以下
        victim.setLife(0)
        victim.die()       
    else:
        victim.setLife(newLife) # 玩家的生命值变为一个新的值（被扣除了一些）
    return 
```
之后，这段代码会被翻译成 `1` 和 `0` 组成的一连串指令，储存在你的手机上。  
每当你玩游戏，有攻击事件发生的时候，这段指令就会被执行。  
<br>

但是，除了**指令**之外，你的手机还有别的东西要储存：这就是**数据**。  
<br> 

让我们来看一下 `victim.die()` 这个函数。有一些面向对象的方法（比如 `class` 等），我们暂时不需要掌握。

```python 
import soundLibrary
class Player: # victim 就是一个 Player

    def die(self):
        """
        英雄阵亡时播放英雄专属的阵亡音效
        """
        with open(self.getSoundFilePath(), 'rb') as f: 
        # self.getSoundFilePath() 可能返回类似于 'Libai-die-2.wav' 这样的字符串
            soundWave = soundLibrary.process(f) # 把声音处理成可以播放的
            soundLibrary.play(soundWave) # 播放英雄专属的阵亡音效

    #####################
    ## 可能还有很多其它函数...
    #####################


```  
<br>

这里，`f` 就是二进制的声音文件，它是和整个游戏一起被下载到你的手机里，并储存起来的。我们管这样的东西叫做 `数据`。  
<br> 

事实上，好几个 `GB` 大小的王者荣耀游戏文件中，`指令` 可能只占了不到百分之一，剩下的全部都是图片、音频、文字、模型等等`数据`，这些 `数据` 需要在运行的时候被读取、处理、展示。  
（当然，`die` 函数的逻辑肯定不是上面这样，因为每次有英雄阵亡都重新读文件非常非常耗时（读取文件是相当慢的操作），一定是加载游戏的时候读出来，然后反复使用的）


## 数据的本质
那么，这些数据是怎么保存在电脑上的呢？  
<br>

和指令一样，它也是以二进制的形式保存的。对电脑来说，硬盘里的存储介质被磁化就代表 `1`，否则就是 `0`。  
<br>

我们要存储的信息（比如一个图片）先是以一定规则被 `编码` 成二进制（比如，规定好，文件的每 `24` 位二进制数代表一个像素的 `RGB` 值，用这种方式保存图片），存储下来，用到的时候，再用对应的 `解码` 方式还原出来。我们可以用任何方法 `解码` 任何数据，只不过解出来的东西会让人不知所云。比如，对一个 `.doc` 文件（`word` 文档），你可以选择`使用记事本打开`，然后会看到一堆乱码，这就是所谓的 **打开方式不对**。  
<br>

`.doc`，`.docx`，`.jpg` 等拓展名，只是用来标明文件的类型，告诉人们需要用什么方式来 `解码`的，并没有什么实际的作用。当然，现在的 `Windows` 系统会根据对应的拓展名自动选择解码方式（指定默认打开方式），所以会出现更改拓展名之后无法打开的情况。当然，你可以强行把一个 `.jpg` 文件的拓展名改成 `.doc`，然后手动选择用图片查看器打开，这完全没有问题。  
<br>


## Python 中的实现
`Python` 中的 `open` 函数，会返回一个变量。这个变量本身并不包含任何内容，它只是一个读取文件用的“窗口”，我们可以通过这个变量读取文件内容。
<br> 

通常情况下，对于文本文件（就是使用记事本打开，能直接看到文字内容，而不是乱码的东西），我们使用 `open(filename)`，对于非文本（图片、音频等），我们使用 `open(filename, 'rb')`。  
<br>

用 `open` 打开一个 `txt` 文件，并且调用 `readlines`，你可以看到它的内容。  
```python
f = open("txtFile.txt")
print(f.readlines())
```

你可以试试用它来打开其它格式的文件。你会发现，大多数情况下会得到乱码。这是因为，`readlines()` 会从字面意思上读取文件（得到二进制码），而 `print` 会尝试把它 `解码` 成英文字符。然而，由于它实际上是其它东西，所以 `解码` 出来的东西会不知所云。  
<br>

想要读取特定类型的文件，我们需要与文件匹配的 `解码` 方法。在 `Python` 中，我们可以使用第三方库来解决。   
比如，如果你想读取一个图片并展示出来，你可以使用 `Pillow` 这个库。  
<br>

```python
import PIL
from PIL import Image
image = Image.open("yazi.jpg") # 这个函数其实先使用了 Python 的 open 函数，然后进行解码。
# 希望深究的同学可以看一下它的源码　https://pillow.readthedocs.io/en/stable/_modules/PIL/Image.html#open
image.show()    # 这句段代码可以打开一个新的窗口来展示图片。
                # 你也可以直接通过 image 变量读取或修改每一个像素点。
```


