"""
今日寄语:知不足而奋进,望远山而前行
时间:2025/12/8 上午12:49
"""

import tkinter as tk
import threading
import random

class Frame:
    def __init__(self):
        # 自定义文本和颜色
        self.random_texts = ["每天都要开心哦","我想你啦","可爱的宝宝","加油!","今天也真棒哦","记得吃饭哦","今天要努力哦"]
        self.random_colors = ["pink","grey","lightblue","lightgreen","lightyellow","lightcoral","lightgray","lightseagreen"]
    def show(self):
        window = tk.Tk()
        window.title("Laity")
        window.geometry("250x40")
        # 获取屏幕尺寸
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        # 随机位置
        x = random.randint(0, width - 250)
        y = random.randint(0, height - 40)
        window.geometry(f"250x40+{x}+{y}")
        # 随机选择文本和颜色
        random_text = random.choice(self.random_texts)
        random_color = random.choice(self.random_colors)
        tk.Label(window, text=random_text, font=("Arial", 16),bg=random_color,width=20,height=2).pack()
        window.mainloop()

    def start(self,num_threads=10):
        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=self.show)
            t.daemon = True
            t.start()
            threads.append(t)
        return threads

if __name__ == '__main__':
    frame = Frame()
    frame.start(50)