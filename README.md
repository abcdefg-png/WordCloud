# 七夕特辑之词云——你和ta的聊天高频词

现在是2022年8月02日10点13分，我发布了第一条CSDN博客。蹭着这波七夕的热度，给朋友们分享一份自制的**爱心云图**。咱们先上源代码和效果图：

## 兄弟们最想要的源代码(for FREE)

[abcdefg-png/WordCloud: 七夕云图 (github.com)](https://github.com/abcdefg-png/WordCloud)

## 兄弟们最关心的效果展示

![to_lover22](https://github.com/abcdefg-png/WordCloud/tree/main/images/to_lover22.png)

注：想做出云图来，需要你和另一半**有一定量的聊天记录**哦（yysy，情侣之间的聊天记录绰绰有余）

## 兄弟们最想看的使用方法

咱们从上到下依次讲，Python版本我当时用的是3.10，**正常情况下所有版本的Python3都可以运行**，大家放心。

### 1.requirements.txt

为了节省大家的宝贵时间，我们使用清华源安装所需要的第三方包，在pycharm终端输入如下命令即可安装（快的飞起）

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt  // 一次
```

如果你想**每次都这么快**，可以再进行pip的换源，把镜像地址写入php.ini。一句话执行：

```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

![8](\images\8.jpg)

### 2.导出并读取QQ聊天记录文件

我和她的聊天记录怎么导出呢？别急，按照下面的操作1分钟完事

首先打开消息管理

![10](https://github.com/abcdefg-png/WordCloud/tree/main/images/10.jpg)

之后右键选择导出消息记录，非常方便！

![11](\images\11.jpg)

最后选择文件格式，**一定要选txt**，bak加密过的打开是乱码

![12](\images\12.jpg)

在代码的**第18行**，替换文件目录。

```Python
fn = open('聊天记录.txt', encoding="utf-8")  # 打开文件
```

### 3.聊天记录后处理

这一步非常重要，直接决定做出云图的效果：

```
我们需要把自己QQ曾经用过的昵称、给对象曾经的备注都替换为空。
因为聊天记录每句话自带QQ备注，所以如果不去掉做出来的大概率会是彼此的QQ备注/昵称。
```

![9](\images\9.jpg)

同样的道理，为了咱们的云图更能体现每对cp的特点，我把乱七八糟字符，常用语气词、助词也都去掉了，分别在代码的22行和29行，兄弟们根据需求自动修改呀！

```Python
rule = re.compile(u"[^a-zA-Z\u4e00-\u9fa5]") # 留下字母数字和中文

remove_words = ["没", " ", "嗯", "了", "是", "的", '我', '的', "在", "不", "就", "也", "你", "吧", "和", "啊"] # 去掉常用关键字
```

### 4.字体和模板

为了能做出心形形状和字体，我们还需要导入一下两个文件，分别在代码的**45行和53行** 。同样的，云图的其他参数兄弟们都可以根据需求自行修改。

```Python
color_mask = imread('heart.png') # 心形模板
wc = WordCloud(
    width=600,
    height=700,
    scale=9, # 更加清晰
    background_color="lightpink",
    # background_color="white",
    # font_path='C:/Windows/Fonts/simhei.ttf',
    font_path='C:/Windows/Fonts/msyh.ttc',  # 设置字体格式
    mask=color_mask,  # 设置背景图
    max_words=300,  # 最多显示词数
    max_font_size=50  # 字体最大值
)
```

### FINAL

最后生成的图片会自动导出，大家注意查收；由于云图的配色不受控制，建议多做几张，保存的名字不要一样，否则会被平替（现实版狗熊掰玉米）

```Python
wc.to_file("导出图片.png")  # 生成文件
```

## 结语

这里本来想讲一下代码的具体内容，感觉会使用、看看注释大家都能理解，就不过多赘述了。

最后，祝大家有个愉快的七夕，有情人终成眷属！

等等，如果你还没有女朋友怎么办？那只是大家还没有发现茫茫人海中优秀的你！好好学习，认真工作，你终将遇到自己的另一半。而在这之前，不如先准备一下你们在一起的未来☺



`最后感谢女朋友晓辉的封面设计和文案修改❤`



