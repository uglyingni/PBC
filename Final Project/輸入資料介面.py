import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

# 建立主視窗
root = tk.Tk()
root.geometry("600x550")
root.title("輸入專案資料")

# 自己設定，希望之後能夠修成使用者在介面上輸入
num_of_project = 6

# 初始介面設為第一頁
# 概念是import data裡的每個工作表是一頁的輸入內容，所以共四頁
page_var = tk.IntVar()
page_var.set(1)

# 下一頁Function
def next_page():
    current_page = page_var.get()
    if current_page == 1:
        page_one.pack_forget()
        page_two.pack()
        page_var.set(2)
    elif current_page == 2:
        page_two.pack_forget()
        page_three.pack()
        page_var.set(3)
    else:
        page_three.pack_forget()
        page_four.pack()
        page_var.set(4)

# 上一頁Function
def previous_page():
    current_page = page_var.get()
    if current_page == 2:
        page_two.pack_forget()
        page_one.pack()
        page_var.set(1)
    elif current_page == 3:
        page_three.pack_forget()
        page_two.pack()
        page_var.set(2)
    else:
        page_four.pack_forget()
        page_three.pack()
        page_var.set(3)

# 第一頁
page_one = tk.Frame(root)
page_one.pack()

page_one_entries = []

# 按添加Button觸發此Function，將輸入的值存進page_one_entries中
def add_page_one_entry():
    project = project_combo.get()
    project_days = int(project_days_entry.get())
    start_date = start_cal.selection_get()
    end_date = end_cal.selection_get()

    entry = [project, project_days, start_date, end_date]
    page_one_entries.append(entry)

    # 存完後清空欄位
    project_combo.set('')
    project_days_entry.delete(0, tk.END)
    start_cal.selection_clear()
    end_cal.selection_clear()

# 專案下拉選單
project = [f"專案 {i+1}" for i in range(num_of_project)]
project_label = ttk.Label(page_one, text="選擇專案：")
project_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
project_combo = ttk.Combobox(page_one, value=project)
project_combo.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# 專案天數input
project_days_label = ttk.Label(page_one, text="專案天數：")
project_days_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
project_days_entry = ttk.Entry(page_one)
project_days_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# 起始日期input
start_label = ttk.Label(page_one, text="起始日期：")
start_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
start_cal = Calendar(page_one, selectmode="day")
start_cal.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# 結束日期input
end_label = ttk.Label(page_one, text="結束日期：")
end_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
end_cal = Calendar(page_one, selectmode="day")
end_cal.grid(row=3, column=1, padx=5, pady=5, sticky="w")

# 添加Button
add_button = tk.Button(page_one, text="添加", command=add_page_one_entry)
add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

# 下一頁Button
next_button = tk.Button(page_one, text="下一頁", command=next_page)
next_button.grid(row=5, column=0, columnspan=2, padx=5, pady=20)

# 第二頁
page_two = tk.Frame(root)

page_two_entries = []

def add_page_two_entry():
    level = level_combo.get()
    how_many = int(how_many_entry.get())
    normal_wage = float(normal_wage_entry.get())
    overtime_wage = float(overtime_wage_entry.get())

    entry = [level, how_many, normal_wage, overtime_wage]
    page_two_entries.append(entry)

    level_combo.set('')
    how_many_entry.delete(0, tk.END)
    normal_wage_entry.delete(0, tk.END)
    overtime_wage_entry.delete(0, tk.END)

# Level下拉選單
level_label = ttk.Label(page_two, text="選擇員工：")
level_label.grid(row=0, column=0, padx=5, pady=10, sticky="e")
level_combo = ttk.Combobox(page_two, values=["L1", "L2", "L3", "L4"])
level_combo.grid(row=0, column=1, padx=5, pady=10, sticky="w")

# 員工數input
how_many_label = ttk.Label(page_two, text="員工人數：")
how_many_label.grid(row=1, column=0, padx=5, pady=10, sticky="e")
how_many_entry = ttk.Entry(page_two)
how_many_entry.grid(row=1, column=1, padx=5, pady=10, sticky="w")

# 一般薪資input
normal_wage_label = ttk.Label(page_two, text="一般薪資：")
normal_wage_label.grid(row=2, column=0, padx=5, pady=10, sticky="e")
normal_wage_entry = ttk.Entry(page_two)
normal_wage_entry.grid(row=2, column=1, padx=5, pady=10, sticky="w")

# 加班薪資input
overtime_wage_label = ttk.Label(page_two, text="加班薪資：")
overtime_wage_label.grid(row=3, column=0, padx=5, pady=10, sticky="e")
overtime_wage_entry = ttk.Entry(page_two)
overtime_wage_entry.grid(row=3, column=1, padx=5, pady=10, sticky="w")

# 添加Button
add_button = tk.Button(page_two, text="添加", command=add_page_two_entry)
add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

# 上一頁Button
next_button = tk.Button(page_two, text="上一頁", command=previous_page)
next_button.grid(row=5, column=0, padx=10, pady=20, sticky="w")

# 下一頁Button
next_button = tk.Button(page_two, text="下一頁", command=next_page)
next_button.grid(row=5, column=1, padx=10, pady=20, sticky="e")

# 第三頁
page_three = tk.Frame(root)

page_three_entries = []

def add_page_three_entry():
    module0 = module0_combo.get()
    L1 = int(L1_entry.get())
    L2 = int(L2_entry.get())
    L3 = int(L3_entry.get())
    L4 = int(L4_entry.get())

    entry = [module0, L1, L2, L3, L4]
    page_three_entries.append(entry)

    module0_combo.set('')
    L1_entry.delete(0, tk.END)
    L2_entry.delete(0, tk.END)
    L3_entry.delete(0, tk.END)
    L4_entry.delete(0, tk.END)

# Module下拉選單
module0_label = ttk.Label(page_three, text="選擇模組：")
module0_label.grid(row=0, column=0, padx=5, pady=10, sticky="e")
module0_combo = ttk.Combobox(page_three, values=["PP", "MM", "SD", "CO", "FI"])
module0_combo.grid(row=0, column=1, padx=5, pady=10, sticky="w")

# L1 input
L1_label = ttk.Label(page_three, text="L1人數：")
L1_label.grid(row=1, column=0, padx=5, pady=10, sticky="e")
L1_entry = ttk.Entry(page_three)
L1_entry.grid(row=1, column=1, padx=5, pady=10, sticky="w")

# L2 input
L2_label = ttk.Label(page_three, text="L2人數：")
L2_label.grid(row=2, column=0, padx=5, pady=10, sticky="e")
L2_entry = ttk.Entry(page_three)
L2_entry.grid(row=2, column=1, padx=5, pady=10, sticky="w")

# L3 input
L3_label = ttk.Label(page_three, text="L3人數：")
L3_label.grid(row=3, column=0, padx=5, pady=10, sticky="e")
L3_entry = ttk.Entry(page_three)
L3_entry.grid(row=3, column=1, padx=5, pady=10, sticky="w")

# L4 input
L4_label = ttk.Label(page_three, text="L4人數：")
L4_label.grid(row=4, column=0, padx=5, pady=10, sticky="e")
L4_entry = ttk.Entry(page_three)
L4_entry.grid(row=4, column=1, padx=5, pady=10, sticky="w")

# 添加Button
add_button = tk.Button(page_three, text="添加", command=add_page_three_entry)
add_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

# 上一頁Button
next_button = tk.Button(page_three, text="上一頁", command=previous_page)
next_button.grid(row=6, column=0, padx=5, pady=20, sticky="w")

# 下一頁Button
next_button = tk.Button(page_three, text="下一頁", command=next_page)
next_button.grid(row=6, column=1, padx=5, pady=20, sticky="e")

# 第四頁
page_four = tk.Frame(root)

page_four_entries = []

def add_page_four_entry():
    module = module_combo.get()
    entry = [float(field.get()) for field in entry_fields]
    entry.insert(0, module)

    page_four_entries.append(entry)

    module_combo.set('')
    for field in entry_fields:
        field.delete(0, tk.END)

# Module下拉選單
# 第三頁跟第四頁的下拉選單如果取名一樣，運作會錯亂><
module_label = ttk.Label(page_four, text="選擇模組：")
module_label.grid(row=0, column=0, padx=5, pady=10, sticky="e")
module_combo = ttk.Combobox(page_four, values=["PP", "MM", "SD", "CO", "FI"])
module_combo.grid(row=0, column=1, padx=5, pady=10, sticky="w")

entry_fields = []

# 根據前面設定的num_of_project去產生相對應的欄位數
for i in range(num_of_project):
    label = ttk.Label(page_four, text=f"專案 {i+1}：")
    label.grid(row=i+1, column=0, padx=5, pady=10, sticky="e")
    field = ttk.Entry(page_four)
    field.grid(row=i+1, column=1, padx=5, pady=10, sticky="w")
    entry_fields.append(field)

# 添加Button
add_button = tk.Button(page_four, text="添加", command=add_page_four_entry)
add_button.grid(row=num_of_project+1, column=0, columnspan=2, padx=5, pady=10)

# 上一頁Button
next_button = tk.Button(page_four, text="上一頁", command=previous_page)
next_button.grid(row=num_of_project+2, column=0, columnspan=2, padx=5, pady=20)

root.mainloop()

# 建立import data test.xlxs，用ExcelWriter能夠在同一個檔案新增多個工作表
writer = pd.ExcelWriter("C:\\Users\\User\\Desktop\\python\\import data test.xlsx", engine="xlsxwriter")

# 將page_X_entries轉為pandas dataframe
module1 = pd.DataFrame(page_one_entries, columns=["project", "project_days", "start_date", "end_date"])
module2 = pd.DataFrame(page_two_entries, columns=["level", "how_many", "normal_wage", "overtime_wage"])
module3 = pd.DataFrame(page_three_entries, columns=["module", "L1", "L2", "L3", "L4"])

columns = project
columns.insert(0, "module")
module4 = pd.DataFrame(page_four_entries, columns=columns)

module1.to_excel(writer, sheet_name="project", index=False)
module2.to_excel(writer, sheet_name="level", index=False)
module3.to_excel(writer, sheet_name="level_and_module", index=False)
module4.to_excel(writer, sheet_name="project_and_module", index=False)

writer.close()
