import tkinter as tk
import tkinter.font as tkFont
import math
from PIL import ImageTk

class Calculator(tk.Frame):

  shouldReset = True
  conductAdd = False
  conductMin = False
  conductMul = False
  conductDiv = False
  
  def __init__(self):
    tk.Frame.__init__(self) 
    self.grid()
    self.createWidgets()

  def createWidgets(self):
    f1 = tkFont.Font(size = 48, family = "Courier New")
    f2 = tkFont.Font(size = 32, family = "Courier New")
	
    self.btnNum1 = tk.Button(self, text = "1", height = 1, width = 2, command = self.clickBtnNum1, font = f2) 
    self.btnNum2 = tk.Button(self, text = "2", height = 1, width = 2, command = self.clickBtnNum2, font = f2) 
    self.btnNum3 = tk.Button(self, text = "3", height = 1, width = 2, command = self.clickBtnNum3, font = f2) 
    self.btnNum4 = tk.Button(self, text = "4", height = 1, width = 2, command = self.clickBtnNum4, font = f2) 
    self.btnNum5 = tk.Button(self, text = "5", height = 1, width = 2, command = self.clickBtnNum5, font = f2) 
    self.btnNum6 = tk.Button(self, text = "6", height = 1, width = 2, command = self.clickBtnNum6, font = f2) 
    self.btnNum7 = tk.Button(self, text = "7", height = 1, width = 2, command = self.clickBtnNum7, font = f2) 
    self.btnNum8 = tk.Button(self, text = "8", height = 1, width = 2, command = self.clickBtnNum8, font = f2) 
    self.btnNum9 = tk.Button(self, text = "9", height = 1, width = 2, command = self.clickBtnNum9, font = f2) 
    self.btnNum0 = tk.Button(self, text = "0", height = 1, width = 2, command = self.clickBtnNum0, font = f2) 
    self.btnAdd = tk.Button(self, text = "+", height = 1, width = 2, command = self.clickBtnAdd, font = f2) 
    self.btnMin = tk.Button(self, text = "-", height = 1, width = 2, command = self.clickBtnMin, font = f2)
    self.btnMul = tk.Button(self, text = "*", height = 1, width = 2, command = self.clickBtnMul, font = f2)
    self.btnDiv = tk.Button(self, text = "/", height = 1, width = 2, command = self.clickBtnDiv, font = f2)
    self.btnAns = tk.Button(self, text = "=", height = 1, width = 2, command = self.clickBtnAns, font = f2)    
    self.btnAC = tk.Button(self, text = "AC", height = 1, width = 2, command = self.clickBtnAC, font = f2)

    self.txtNum = tk.Text(self, height = 1, width = 9, font = f1) 
	
    self.btnNum1.grid(row = 1, column = 0, sticky = tk.NE + tk.SW)
    self.btnNum2.grid(row = 1, column = 1, sticky = tk.NE + tk.SW)
    self.btnNum3.grid(row = 1, column = 2, sticky = tk.NE + tk.SW)
    self.btnNum4.grid(row = 2, column = 0, sticky = tk.NE + tk.SW)
    self.btnNum5.grid(row = 2, column = 1, sticky = tk.NE + tk.SW)
    self.btnNum6.grid(row = 2, column = 2, sticky = tk.NE + tk.SW)
    self.btnNum7.grid(row = 3, column = 0, sticky = tk.NE + tk.SW)
    self.btnNum8.grid(row = 3, column = 1, sticky = tk.NE + tk.SW)
    self.btnNum9.grid(row = 3, column = 2, sticky = tk.NE + tk.SW)
    self.btnNum0.grid(row = 4, column = 0, sticky = tk.NE + tk.SW)
    self.btnAns.grid(row = 4, column = 1, sticky = tk.NE + tk.SW)
    self.btnAC.grid(row = 4, column = 2, sticky = tk.NE + tk.SW)
    self.btnAdd.grid(row = 1, column = 3, sticky = tk.NE + tk.SW) 
    self.btnMin.grid(row = 2, column = 3, sticky = tk.NE + tk.SW)
    self.btnMul.grid(row = 3, column = 3, sticky = tk.NE + tk.SW)
    self.btnDiv.grid(row = 4, column = 3, sticky = tk.NE + tk.SW)
    self.txtNum.grid(row = 0, column = 0, columnspan = 4, sticky = tk.NE + tk.SW)

  def setNumStr(self, content):
    if self.shouldReset == True:
        self.txtNum.delete("1.0", tk.END)
        self.txtNum.insert("1.0", content)
        self.shouldReset = False
    else: 
        self.txtNum.insert(tk.END, content)
        
  def clickBtnAns(self):
    self.nextNum = float(self.txtNum.get("1.0", tk.END))
    self.txtNum.delete("1.0", tk.END)
    if self.conductAdd == True:
        self.txtNum.insert("1.0", str(self.curNum + self.nextNum))
        self.conductAdd = False
    elif self.conductMin == True:
        self.txtNum.insert("1.0", str(self.curNum - self.nextNum))
        self.conductMin = False
    elif self.conductMul == True:
        self.txtNum.insert("1.0", str(self.curNum * self.nextNum))
        self.conductMul = False
    elif self.conductDiv == True:
        self.txtNum.insert("1.0", str(self.curNum / self.nextNum))
        self.conductDiv = False
    self.shouldReset = True
       
  def clickBtnAdd(self):
    self.curNum = float(self.txtNum.get("1.0", tk.END))
    self.shouldReset = True
    self.conductAdd = True
  
  def clickBtnMin(self):
    self.curNum = float(self.txtNum.get("1.0", tk.END))
    self.shouldReset = True
    self.conductMin = True
    
  def clickBtnMul(self):
    self.curNum = float(self.txtNum.get("1.0", tk.END))
    self.shouldReset = True
    self.conductMul = True
      
  def clickBtnDiv(self):
    self.curNum = float(self.txtNum.get("1.0", tk.END))
    self.shouldReset = True
    self.conductDiv = True
    
  def clickBtnAC(self):
    self.txtNum.delete("1.0", tk.END)
    
  def clickBtnNum1(self):
    self.setNumStr("1")

  def clickBtnNum2(self):
    self.setNumStr("2")

  def clickBtnNum3(self):
    self.setNumStr("3")

  def clickBtnNum4(self):
    self.setNumStr("4")

  def clickBtnNum5(self):
    self.setNumStr("5")

  def clickBtnNum6(self):
    self.setNumStr("6")

  def clickBtnNum7(self):
    self.setNumStr("7")
	
  def clickBtnNum8(self):
    self.setNumStr("8")
	
  def clickBtnNum9(self):
    self.setNumStr("9")

  def clickBtnNum0(self):
    self.setNumStr("0")

cal = Calculator()
cal.master.title("My Calculator")
cal.mainloop()