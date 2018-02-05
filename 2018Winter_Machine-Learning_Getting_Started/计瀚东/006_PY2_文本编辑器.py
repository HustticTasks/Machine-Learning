#coding=utf-8
import wx

# 这个函数用于创建一个简单文本编辑器窗口
def creatFrame(event):
	# 打开文件的函数，与按钮load绑定
	def load(event):
		try:
			f = open(fileName.GetValue(), 'r')
			contents.SetValue(f.read())
		finally:
			if f:
				f.close()
	# 保存文件的函数，与按钮save绑定
	def save(event):
		try:
			f = open(fileName.GetValue(), 'w')
			f.write(contents.GetValue())
		finally:
			if f:
				f.close()
	# 记录窗口的编号，支持多文件同时编辑
	global i
	i += 1

	app = wx.App()
	win = wx.Frame(None, title="简单文本编辑器"+str(i), size=(410, 335))
	bkg = wx.Panel(win)

	# 各组件与绑定事件
	loadButton = wx.Button(bkg, label="打开")
	loadButton.Bind(wx.EVT_BUTTON, load)
	saveButton = wx.Button(bkg, label="保存")
	saveButton.Bind(wx.EVT_BUTTON, save)
	newButton = wx.Button(bkg, label="新窗口")
	newButton.Bind(wx.EVT_BUTTON, creatFrame) # 在这里实现递归，新窗口按钮会再次调用这个函数
	fileName = wx.TextCtrl(bkg)
	contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)
	
	# 上面部分的尺寸器
	hbox = wx.BoxSizer()
	hbox.Add(fileName, proportion=1, flag=wx.EXPAND)
	hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)
	hbox.Add(saveButton, proportion=0, flag=wx.LEFT, border=5)
	hbox.Add(newButton, proportion=0, flag=wx.LEFT, border=5)

	#最终的尺寸器
	vbox = wx.BoxSizer(wx.VERTICAL)
	vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
	vbox.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=5)

	bkg.SetSizer(vbox)
	win.Show()

	app.MainLoop()

i = 0	
creatFrame(None)
