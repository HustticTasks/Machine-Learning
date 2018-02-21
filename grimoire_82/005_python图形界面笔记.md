# python图形界面

##一、wxPython

### 1、开始

​	基本结构

```python
import wx
app = wx.App() #创建一个对象
app.MainLoop() #结束操作
```

### 2、窗口与组件

​	一个窗口也称为框架（Frame），拥有与其绑定的按钮（Button）和文本控件（TextCtrl）等组件。其中控件有标签，坐标，大小等参数。

​	其中默认的文本控件是文本框，其 `style` 参数本质上是整数，使用按位或 `or` 或管道运算符 `|` 即可联合不同的风格；下面通过添加 `wx.TE_MULTILINE` 获得了垂直滚动条，使之成为多行文本区， `wx.HSCROLL` 获取了水平滚动条。

```python
import wx

# 开始，创建一个窗口
app = wx.App()
win = wx.Frame(None, title="Simple Editor", size=(410, 335))
win.Show()

# 创造各组件
## 创造两个按钮对象 
loadButton = wx.Button(win, label='Open', pos=(225, 5), size=(80, 25))
saceButton = wx.Button(win, label='Save', pos=(315, 5), size=(80, 25))

## 创造两个文本控件
filename = wx.TextCtrl(win, pos=(5, 5), size=(210, 25))
contents = wx.TextCtrl(win, pos=(5, 35), size=(390, 260), style=wx.TE_MULTILINE | wx.HSCROLL)

app.MainLoop()
```

​	*PS：注意窗口名参数是 `title` ，组件名参数是 `label`  。*

### 3、动态布局

​	窗口大小发生变化时，如果组件的几何位置不变就会很怪异。我们通过尺寸器（sizer）可以用相对位置替换上面的绝对位置。

​	`wx.BoxSizer()` 方法有一个决定它控制的组件是水平或是垂直排列的参数（前者为 `wx.HORIZONAL` ，后者为 `wx.VERTICAL` ），默认为水平排列。

​	`.Add()` 方法有以下三个参数：

​	1、`porportion` 参数可以设为任意数，在窗口改变大小时按比例分配空间。

​	2、`falg` 参数可以将多个模式联合在一起，其中 `wx.EXPAND` 使组件能扩展到分配的空间中；其他上、下、左、右、和全部五个模式表示边框参数应用在哪一边。

​	3、`border` 参数用于设置边缘宽度，即间隔。

```python
import wx

app = wx.App()
win = wx.Frame(None, title="Simple Editor", size=(410, 335))
bkg = wx.Panel(win)

loadButton = wx.Button(bkg, label='Open')
saveButton = wx.Button(bkg, label='Save')
filename = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(filename, proportion=1, flag=wx.EXPAND)
hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(saveButton, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, porportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents, porportion=1, flag=wx.EXPAND  | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

bkg.SetSizer(vbox)
win.Show()

app.MainLoop()
```

### 4、事件处理

​	把函数绑定到涉及事件可能会发生的组件上。

```python
# 按下load键后，会激活load函数
loadButton.Bind(wx.EVT_BUTTON, load)
```

​	*PS：这样的函数传入的形参应当为 event*

### 5、文本控件操作

​	通过文本控件对象的 `GetValue`  和 `SetValue` 方法，可以分别从文本控件中取出数据和把数据显示在文本控件中。

*PS：文本控件获得垂直和水平滚动条的常数有 `wx.TE_MULTILINE` 和 `wx.HSCROLL` ；尺寸器对组件横向排列和纵向排列的常数有 `wx.HORIZONAL` 和 `wx.VERTICAL` ；尺寸器的 `Add()` 方法中 ` flag` 参数也有六个参数，一个表示组件可变大小，另外五个表示边界参数应用的边*