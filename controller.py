"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:788392508
在线反馈:https://support.qq.com/product/618914
"""
from tkinter import filedialog,messagebox
from ui import Win
import tkinter as tk
from delay import *
from threading import Thread

class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: Win
    def __init__(self):
        pass
    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作
    def on_start(self,evt):

        input_path = self.ui.tk_input_inpath.get()
        output_path = self.ui.tk_input_outpath.get()
        time_offset_str = self.ui.tk_input_time.get()
        
        if not (time_offset_str and output_path and time_offset_str):
            messagebox.showerror("错误", "输入不能为空！")
            return False
        else:
            try:
                int_value = int(time_offset_str)  # 尝试转换为整数
            except ValueError:  # 如果转换失败，则不是整数
                messagebox.showerror("错误", "请输入一个整数！")
                return False
            else:
                time_offset = float(time_offset_str)
                if not os.path.isdir(input_path):
                    messagebox.showerror("错误", "输入路径不存在！")
                if not os.path.exists(output_path):
                    os.makedirs(output_path, exist_ok=True)

                files = [f for f in os.listdir(input_path) if f.endswith('.ass')]
                total_files = len(files)
                self.ui.tk_progressbar_bar.config(maximum=total_files)
                error_list = []

                def update_bar():
                    for i, file_name in enumerate(files):
                        self.ui.tk_progressbar_bar.config(value=i+1)
                        input_file = os.path.join(input_path, file_name)
                        try:
                                adjust_delay(input_file, output_path, time_offset)
                        # except ValueError as ve:
                        #     print(f"文件编码存在错误：{ve}")
                        #     messagebox.showerror("错误", f"文件 {file_name} 的编码无法识别，请检查并确保其为有效的UTF-8或其他支持的编码格式。")
                        except Exception as e:  # 捕获所有其他未知异常
                            # print(f"处理文件 {file_name} 时出现错误：{e}")
                            error_list.append(f"处理文件 {file_name} 时发生意外错误，请查看详细信息：{str(e)}")
                            continue
                    if len(error_list) == 0:
                        messagebox.showinfo("信息", "处理完毕。")
                    else:
                        messagebox.showerror("错误", "\n".join(error_list))
                    

                Thread(target=update_bar).start()

    def select_input_folder(self,evt):
        input_path = filedialog.askdirectory()
        self.ui.tk_input_inpath.delete(0, tk.END)
        self.ui.tk_input_inpath.insert(0, input_path)
    def select_output_folder(self,evt):
        output_path = filedialog.askdirectory()
        self.ui.tk_input_outpath.delete(0, tk.END)
        self.ui.tk_input_outpath.insert(0, output_path)
