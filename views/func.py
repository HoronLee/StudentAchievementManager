from PIL import Image, ImageTk
from os import system
import webbrowser


# 打开帮助页（赞赏）
def help():
    webbrowser.open('https://blog.horon.top', new=0, autoraise=True)


class Student:
    def __init__(self, sno, sname, chinese=0, math=0, english=0):
        self.sno = sno
        self.sname = sname
        self.chinese = chinese
        self.math = math
        self.english = english

    def show(self):
        print(self.sno, self.sname, self.chinese, self.math, self.english, self.chinese + self.math + self.english)


class Mark:
    def __init__(self):
        self.students = []

    # 添加学生成绩
    def insert(self, sno, sname, chinese, math, english):
        student = Student(sno, sname, chinese, math, english)
        self.students.append(student)

    # 修改学生成绩
    def update(self, student):
        for s in self.students:
            if s.sno == student.sno:
                s.sname = student.sname
                s.chinese = student.chinese
                s.math = student.math
                s.english = student.english
                break

    # 删除学生成绩
    def delete(self, sno):
        for s in self.students:
            if s.sno == sno:
                self.students.remove(s)
                break

    # 按学号查询学生成绩
    def showByNo(self, sno):
        for s in self.students:
            if s.sno == sno:
                s.show()

    # 按姓名查询学生成绩
    def showByName(self, sname):
        for s in self.students:
            if s.sname == sname:
                s.show()

    # 按总分排序
    def orderByTotal(self):
        # 使用lambda表达式表示出学生的总成绩，作为key传入给sort方法，然后设定为降序
        self.students.sort(key=lambda x: x.chinese + x.math + x.english, reverse=True)

    # 统计平均分和总分
    def statistics(self):
        chinese_sum = 0
        math_sum = 0
        english_sum = 0
        total_sum = 0
        for s in self.students:
            chinese_sum += s.chinese
            math_sum += s.math
            english_sum += s.english
            total_sum += s.chinese + s.math + s.english
        chinese_avg = chinese_sum / len(self.students)
        math_avg = math_sum / len(self.students)
        english_avg = english_sum / len(self.students)
        total_avg = total_sum / len(self.students)
        print("语文平均分：%.2f，数学平均分：%.2f，英语平均分：%.2f，总分平均分：%.2f" % (
            chinese_avg, math_avg, english_avg, total_avg))

    # 导入成绩
    def load_mark(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f.readlines():
                    # 去除首位的空格，然后用空格作为分隔符将列表中每一项的内容分发给五个变量
                    sno, sname, chinese, math, english = line.strip().split()
                    chinese = int(chinese)
                    math = int(math)
                    english = int(english)
                    self.insert(sno, sname, chinese, math, english)
            print("导入成功！")
        except Exception as err:
            print("导入失败：%s" % err)

    # 导出成绩
    def save_mark(self, filename):
        try:
            with open(filename, "w") as f:
                for s in self.students:
                    f.write("%s %s %s %s %s\n" % (s.sno, s.sname, s.chinese, s.math, s.english))
            print("导出成功！")
        except Exception as err:
            print("导出失败：%s" % err)


class ViewMark:
    def view_insert(sno, sname, chinese, math, english):
        students = Mark()
        students.load_mark("marks.txt")
        students.insert(sno, sname, chinese, math, english)
        students.save_mark("marks.txt")

    def view_update(sno, sname, chinese, math, english):
        students = Mark()
        students.load_mark("marks.txt")
        student = Student(sno, sname, chinese, math, english)
        students.update(student)
        students.save_mark("marks.txt")
        print("修改成功！")

    def view_show(self, sno, sname):
        self.sno = sno
        self.sname = sname
        students = Mark()
        students.load_mark("marks.txt")
        if self.sno != "" and self.sname != "":
            return "只能输入学号和名字中的一个！"
        elif self.sno != "" and self.sname == "":
            return Mark.showByNo(sno)
        elif self.sno == "" and self.sname != "":
            return Mark.showByName(sname)
        students.save_mark("marks.txt")
        print("修改成功！")

    def view_delete(self, sno):
        self.sno = sno
        students = Mark()
        students.load_mark("marks.txt")
        Mark.delete(sno)
        students.save_mark("marks.txt")
        print("删除成功！")

    def view_sort(self):
        students = Mark()
        students.load_mark("marks.txt")
        Mark.showByName()
        students.save_mark("marks.txt")
        print("总分排序成功！")


def main():
    # 从文件中导入成绩
    students = Mark()
    students.load_mark("marks.txt")
    print("默认的导出文件为“mark.txt”")
    print("=============================学生成绩管理系统===========================\n"
          " _____    _ _ _     _    _ _ _   _       _   _                       \n"
          "|  ___|  | (_) |   | |  | (_) | | |     | | | |                      \n"
          "| |__  __| |_| |_  | |  | |_| |_| |__   | |_| | ___  _ __ ___  _ __  \n"
          "|  __|/ _` | | __| | |/\| | | __| '_ \  |  _  |/ _ \| '__/ _ \| '_ \ \n"
          "| |__| (_| | | |_  \  /\  / | |_| | | | | | | | (_) | | | (_) | | | |\n"
          "\____/\__,_|_|\__|  \/  \/|_|\__|_| |_| \_| |_/\___/|_|  \___/|_| |_|\n"
          "-------------------------------Ver 0.1.1-----------------------------"
          )
    while True:
        print("====================\n"
              "|1. 添加学生成绩     |\n"
              "|2. 修改学生成绩     |\n"
              "|3. 删除学生成绩     |\n"
              "|4. 按学号查询学生成绩|\n"
              "|5. 按姓名查询学生成绩|\n"
              "|6. 按总分排序      |\n"
              "|7. 统计平均分和总分 |\n"
              "|8. 导入成绩       |\n"
              "|9. 导出成绩       |\n"
              "|0. 退出系统       |\n"
              "====================\n")
        choice = input("请选择功能：")
        if choice == "1":
            sno = input("请输入学号：")
            sname = input("请输入姓名：")
            chinese = int(input("请输入语文成绩："))
            math = int(input("请输入数学成绩："))
            english = int(input("请输入英语成绩："))
            students.insert(sno, sname, chinese, math, english)
            print("添加成功！")
        elif choice == "2":
            sno = input("请输入学号：")
            sname = input("请输入姓名（不修改请留空）：")
            chinese = input("请输入语文成绩（不修改请留空）：")
            math = input("请输入数学成绩（不修改请留空）：")
            english = input("请输入英语成绩（不修改请留空）：")
            student = Student(sno, sname, chinese, math, english)
            students.update(student)
            print("修改成功！")
        elif choice == "3":
            sno = input("请输入学号：")
            students.delete(sno)
            print("删除成功！")
        elif choice == "4":
            sno = input("请输入学号：")
            students.showByNo(sno)
        elif choice == "5":
            sname = input("请输入姓名：")
            students.showByName(sname)
        elif choice == "6":
            students.orderByTotal()
            print("排序成功！")
        elif choice == "7":
            students.statistics()
        elif choice == "8":
            filename = input("请输入文件名：")
            students.load_mark(filename)
        elif choice == "9":
            filename = input("请输入文件名：")
            students.save_mark(filename)
        elif choice == "0":
            students.save_mark("marks.txt")
            print("退出系统！")
            print("  ____                 _ ____        _ \n"
                  " / ___| ___   ___   __| | __ ) _   _| |\n"
                  "| |  _ / _ \ / _ \ / _` |  _ \| | | | |\n"
                  "| |_| | (_) | (_) | (_| | |_) | |_| |_|\n"
                  " \____|\___/ \___/ \__,_|____/ \__, (_)\n"
                  "                               |___/")
            break
        else:
            print("输入错误，请重新输入！")


# 运行其他程序
def run(a):
    dire = a
    system('python %s' % dire)


# 调整背景图大小
def get_image(filename, width, height):
    im = Image.open(filename).resize((width, height))
    return ImageTk.PhotoImage(im)


if __name__ == '__main__':
    main()
