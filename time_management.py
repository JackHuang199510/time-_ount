#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
from tkinter import ttk, messagebox
import time
from datetime import datetime

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("計時器")

        self.running = False
        self.time_elapsed = 0

        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.label.pack()

        self.start_button = tk.Button(root, text="開始", command=self.start_timer)
        self.start_button.pack(side="left")

        self.pause_button = tk.Button(root, text="暫停", command=self.pause_timer)
        self.pause_button.pack(side="left")

        self.reset_button = tk.Button(root, text="重置", command=self.reset_timer)
        self.reset_button.pack(side="left")

        self.clear_button = tk.Button(root, text="清除記錄", command=self.clear_logs)
        self.clear_button.pack(side="left")

        # 輸入框，用於輸入項目名稱
        self.item_entry = tk.Entry(root, width=20)
        self.item_entry.pack(side="left", padx=10)

        # Treeview 表格
        self.tree = ttk.Treeview(root, columns=("日期", "項目", "時間"), show='headings', height=10)
        self.tree.heading("日期", text="日期")
        self.tree.heading("項目", text="項目")
        self.tree.heading("時間", text="時間")
        self.tree.pack(fill="both", expand=True)

    def update_timer(self):
        if self.running:
            self.time_elapsed += 1
            time_str = time.strftime("%H:%M:%S", time.gmtime(self.time_elapsed))
            self.label.config(text=time_str)
            self.root.after(1000, self.update_timer)

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def pause_timer(self):
        if self.running:
            self.running = False

    def reset_timer(self):
        item_text = self.item_entry.get()
        if not item_text.strip():
            messagebox.showwarning("輸入錯誤", "請輸入項目名稱")
            return

        if self.time_elapsed > 0:
            time_str = time.strftime("%H:%M:%S", time.gmtime(self.time_elapsed))
            date_str = datetime.now().strftime("%Y-%m-%d")
            self.tree.insert("", "end", values=(date_str, item_text, time_str))
        
        self.running = False
        self.time_elapsed = 0
        self.label.config(text="00:00:00")

    def clear_logs(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.item_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()


# In[ ]:




