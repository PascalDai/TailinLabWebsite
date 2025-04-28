#!/bin/bash

# 指定要读取的文本文件的路径
file_path="./source.txt"

# 获取当前日期的年月日，格式为"年-月-日"
current_date=$(date +"%Y-%m-%d")

# 使用 while 循环逐行读取文件内容
while IFS= read -r line
do
  # 创建以当前日期和行内容命名的文件名
  file_name="${current_date}-${line}.markdown"
  
  # 创建文件并写入元数据块和行内容
  echo "---" > "$file_name"
  echo "categories: news" >> "$file_name"
  echo "---" >> "$file_name"
  echo "$line" >> "$file_name"
  
  echo "Created $file_name"
done < "$file_path"
