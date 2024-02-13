import os
import ass
from datetime import timedelta
from chardet import detect
import codecs


def detect_encoding(file):
    with open(file, 'rb') as rawdata:
        # 读取前几个字节来检测是否包含BOM
        bom = rawdata.read(3)
        
        if bom == codecs.BOM_UTF8:  # 检测到BOM（Byte Order Mark）表示是带有BOM的UTF-8
            return 'utf-8-sig'
        else:
            # 使用chardet进行编码检测
            result = detect(rawdata.read())
            return result['encoding']



def adjust_delay(input_file, output_folder, time_offset):
    # 使用ass库加载字幕文件
    detected_encoding = detect_encoding(input_file)
    with open(input_file, 'r', encoding=detected_encoding) as f:
        subs = ass.parse(f)

    time_offset_td = timedelta(milliseconds=time_offset)

    events_count = len(subs.events)
    
    for i, event in enumerate(subs.events):
        event.start += time_offset_td
        event.end += time_offset_td

    # 创建输出文件路径
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join(output_folder, base_name + '.ass')

    # 将调整后的字幕保存到新的ASS文件
    with open(output_file, 'w', encoding='utf-8-sig') as f:
        subs.dump_file(f)

def batch_delay(input_folder, output_folder, time_offset):
    if not os.path.isdir(input_folder):
        raise ValueError(f"'{input_folder}' is not a valid directory.")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder, exist_ok=True)

    files = [f for f in os.listdir(input_folder) if f.endswith('.ass')]
    total_files = len(files)

    for i, file_name in enumerate(files):
        input_file = os.path.join(input_folder, file_name)
        adjust_delay(input_file, output_folder, time_offset)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="批量调整ASS字幕文件的时间延迟")
    parser.add_argument("input_folder", help="输入的包含ASS字幕文件的目录路径")
    parser.add_argument("output_folder", help="输出的文件夹路径")
    parser.add_argument("time_offset", type=float, help="时间偏移量（单位：毫秒）")

    args = parser.parse_args()

    try:
        # 批量调整字幕时间，并显示总体进度
        batch_delay(args.input_folder, args.output_folder, args.time_offset)
    except ValueError as ve:
        print(ve)