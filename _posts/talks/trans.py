import re
from datetime import datetime

# 读取源文件内容
with open('source.txt', 'r') as source_file:
    lines = source_file.readlines()

# 遍历每一行内容
for line in lines:
    line = line.strip()
    match = re.match(r'\[(\d{4}/\d{2})\](.*)', line)  # 匹配 [yyyy/mm] 格式
    if match:
        date_part = match.group(1)  # 提取日期部分
        rest_of_line = match.group(2)  # 提取后面部分
        date_obj = datetime.strptime(date_part, '%Y/%m')  # 解析日期
        formatted_date = date_obj.strftime('%Y-%m-%d')  # 转换成 yyyy-mm-dd 格式
        new_filename = f'{formatted_date}-{rest_of_line}.markdown'  # 新文件名

        # Markdown 文件头部内容
        markdown_header = f"---\ndate: \"{formatted_date}\"\ntitle: \"{rest_of_line}\"\ncategories: talks\n---\n"

        # 将 Markdown 头部内容与当前行内容写入新 Markdown 文件
        with open(new_filename, 'w') as new_file:
            new_file.write(markdown_header)
            new_file.write(line)
