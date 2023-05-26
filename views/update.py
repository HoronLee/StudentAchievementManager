#借鉴creative.py,只需要改布局，背景及文字，command参数就可以了
import tkinter as tk
import func

creative= tk.Tk()
creative.title('修改成绩')
creative.geometry('512x364')
v = tk.IntVar()
#设置背景
canvas_root = tk.Canvas(creative,width=512,height=364)
im_root = func.get_image('photo/bg142.png',512,364)
canvas_root.create_image(256,182,image = im_root)
#输入组件
E_sno = tk.Entry(bg='white',bd=1,cursor='arrow',font='宋体',fg='black',width=40,exportselection=0,highlightcolor='blue',textvariable='请输入学号',xscrollcommand=1)
E_sname = tk.Entry(bg='white',bd=1,cursor='arrow',font='宋体',fg='black',width=40,exportselection=0,highlightcolor='blue',textvariable='请输入姓名（不修改请留空）',xscrollcommand=1)
E_chinese = tk.Entry(bg='white',bd=1,cursor='arrow',font='宋体',fg='black',width=40,exportselection=0,highlightcolor='blue',textvariable='请输入语文成绩（不修改请留空）',xscrollcommand=1)
E_math = tk.Entry(bg='white',bd=1,cursor='arrow',font='宋体',fg='black',width=40,exportselection=0,highlightcolor='blue',textvariable='请输入数学成绩（不修改请留空）',xscrollcommand=1)
E_english = tk.Entry(bg='white',bd=1,cursor='arrow',font='宋体',fg='black',width=40,exportselection=0,highlightcolor='blue',textvariable='请输入英语成绩（不修改请留空）',xscrollcommand=1)
image1 = func.get_image('photo/qd.png',95,35)
button = tk.Button(image=image1,compound=tk.CENTER,command=lambda :func.ViewMark.view_update(E_sno.get(),E_sname.get(),E_chinese.get(),E_math.get(),E_english.get()))
#组件布局
canvas_root.pack()
E_sno.place(x=20,y=40)
E_sname.place(x=20,y=108)
E_chinese.place(x=20,y=180)
E_math.place(x=20,y=250)
E_english.place(x=20,y=310)
button.place(x=400,y=320)

creative.mainloop()