"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:788392508
在线反馈:https://support.qq.com/product/618914
"""
import random
from tkinter import *
from tkinter.ttk import *
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_progressbar_bar = self.__tk_progressbar_bar(self)
        self.tk_button_start = self.__tk_button_start(self)
        self.tk_input_inpath = self.__tk_input_inpath(self)
        self.tk_input_outpath = self.__tk_input_outpath(self)
        self.tk_input_time = self.__tk_input_time(self)
        self.tk_label_time = self.__tk_label_time(self)
        self.tk_label_inpath = self.__tk_label_inpath(self)
        self.tk_label_outpath = self.__tk_label_outpath(self)
        self.tk_button_inpath = self.__tk_button_inpath(self)
        self.tk_button_outpath = self.__tk_button_outpath(self)
    def __win(self):
        self.title("Subtitle Delay Adjuster")
        # 设置窗口大小、居中
        width = 500
        height = 170
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_progressbar_bar(self,parent):
        progressbar = Progressbar(parent, orient=HORIZONTAL,)
        progressbar.place(x=10, y=130, width=480, height=30)
        return progressbar
    def __tk_button_start(self,parent):
        btn = Button(parent, text="开始处理", takefocus=False,)
        btn.place(x=370, y=90, width=120, height=30)
        return btn
    def __tk_input_inpath(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=100, y=10, width=320, height=30)
        return ipt
    def __tk_input_outpath(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=100, y=50, width=320, height=30)
        return ipt
    def __tk_input_time(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=100, y=90, width=260, height=30)
        return ipt
    def __tk_label_time(self,parent):
        label = Label(parent,text="时间(ms)",anchor="center", )
        label.place(x=10, y=90, width=80, height=30)
        return label
    def __tk_label_inpath(self,parent):
        label = Label(parent,text="输入路径",anchor="center", )
        label.place(x=10, y=10, width=80, height=30)
        return label
    def __tk_label_outpath(self,parent):
        label = Label(parent,text="输出路径",anchor="center", )
        label.place(x=10, y=50, width=80, height=30)
        return label
    def __tk_button_inpath(self,parent):
        btn = Button(parent, text="浏览", takefocus=False,)
        btn.place(x=430, y=10, width=60, height=30)
        return btn
    def __tk_button_outpath(self,parent):
        btn = Button(parent, text="浏览", takefocus=False,)
        btn.place(x=430, y=50, width=60, height=30)
        return btn
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_button_start.bind('<Button-1>',self.ctl.on_start)
        self.tk_button_inpath.bind('<Button-1>',self.ctl.select_input_folder)
        self.tk_button_outpath.bind('<Button-1>',self.ctl.select_output_folder)
        pass
    def __style_config(self):
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()