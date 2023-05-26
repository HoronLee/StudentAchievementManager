import tkinter as tk
import func

window = tk.Tk()
window.title('学生成绩管理系统')
window.geometry('1024x728')

# 设置menu栏
menu = tk.Menu(window)

wenjian = tk.Menu(menu, tearoff=0)
wenjian.add_command(label='导出学生成绩', font=("宋体", 8, "normal"))
wenjian.add_command(label='导入学生成绩', font=("宋体", 8, "normal"))
menu.add_cascade(label="文件", menu=wenjian, font=("宋体", 12, "normal"))

bangzhu = tk.Menu(menu, tearoff=0)
bangzhu.add_command(label='使用说明', command=func.help, font=('黑体', 8, 'normal'))
menu.add_cascade(label='帮助', menu=bangzhu, font=('宋体', 12, 'normal'))

caozuo = tk.Menu(menu, tearoff=0)
caozuo.add_command(label='添加成绩', command=lambda: func.run(r'views/insert.py'), font=('宋体', 8, 'normal'))
caozuo.add_command(label='修改成绩', command=lambda: func.run(r'views/update.py'), font=('宋体', 8, 'normal'))
caozuo.add_command(label='查询成绩', command=lambda: func.run(r'views/search.py'), font=('宋体', 8, 'normal'))
caozuo.add_command(label='删除成绩', command=lambda: func.run(r'views/delete.py'), font=('宋体', 8, 'normal'))
caozuo.add_command(label='排序', command=lambda: func.run(r'views/sort.py'), font=('宋体', 8, 'normal'))
menu.add_cascade(label='操作', menu=caozuo, font=('宋体', 12, 'normal'))

zanzhu = tk.Menu(menu, tearoff=0)
zanzhu.add_command(label='赞助', command=func.help, font=('宋体', 8, 'normal'))
menu.add_cascade(label='赞助', menu=zanzhu, font=('宋体', 12, 'normal'))

window.config(menu=menu)

# 设置背景图片
canvas_root = tk.Canvas(window, width=1024, height=728)
im_root = func.get_image('photo/bg.png', 1024, 728)
canvas_root.create_image(512, 364, image=im_root)

# 设置组件
im_label1 = func.get_image('photo/bt.png', 1024, 70)
label = tk.Label(window, image=im_label1)

im_button1 = func.get_image('photo/4.png', 250, 50)
button1 = tk.Button(window, image=im_button1, compound=tk.CENTER, command=func.help)

im_button2 = func.get_image('photo/5.png', 250, 50)
button2 = tk.Button(window, image=im_button2, compound=tk.CENTER, command=func.help)

label.place(y=0)  # 建议把这个label标题p到背景图上，运行后全屏窗口就知道为什么这么建议了
canvas_root.pack()
button1.place(x=700, y=550)
button2.place(x=700, y=650)

window.mainloop()
