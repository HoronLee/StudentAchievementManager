import tkinter as tk
from tkinter import ttk
import func

#输入查询依据
def search():
    tksearch= tk.Tk()
    tksearch.title('查询成绩')
    tksearch.geometry('512x364')
    v = tk.IntVar()
    #设置背景
    canvas_root = tk.Canvas(tksearch,width=512,height=364)
    im_root = func.get_image('photo/search.png',512,364)
    canvas_root.create_image(256,182,image = im_root)
    #输入组件
    entry = tk.Entry(bg='white',bd=1,cursor='arrow',font='宋体',fg='black',width=40,exportselection=0,highlightcolor='blue',textvariable='使用学号查找',xscrollcommand=1)
    image1 = func.get_image('photo/qd.png',95,35)
    button = tk.Button(image=image1,compound=tk.CENTER,command=lambda :func.ViewMark.view_show(entry.get()))
    w = tk.Label(tksearch, text="")
    w.pack()
    #组件布局
    canvas_root.pack()
    entry.place(x=20,y=200)
    button.place(x=400,y=300)

    tksearch.mainloop()

#显示结果新窗体
def output(out):
    tkouput = tk.Tk()
    tkouput.title('查询结果')
    tkouput.geometry('1024x728')
    columns = ('ID','姓名','语文','数学','英语')
    scrollBar1 = tk.Scrollbar(tkouput,orient='vertical')
    treeview = ttk.Treeview(tkouput,height=31,show='headings',columns=columns,yscrollcommand=scrollBar1.set)


    for col in columns:
        treeview.column(col,width=80,anchor='w')   #每一行的宽度,'w'意思为靠右

    for i in out:
        treeview.insert('','end',values=i)

    scrollBar1.config(command=treeview.yview)
    scrollBar1.pack(side='right',fill='y')    
    treeview.pack(fill='x')
    tkouput.mainloop()

if __name__ == '__main__':
    search()