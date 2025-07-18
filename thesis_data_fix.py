# -*- coding: utf-8 -*-
"""Thesis_data_fix.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JJDK9Iq4C-Xq5Oq2Q9gNsQowUzzAwzLB
"""

!pip install pandas openpyxl xlrd
import pandas as pd
from google.colab import files

# ====== 交互上传 ======
print("请上传您的文件（支持.xls/.xlsx/.csv）：")
uploaded = files.upload()
file_name = next(iter(uploaded))

# ====== 智能格式识别 ======
try:
    # 尝试作为Excel读取
    df = pd.read_excel(file_name, engine=None)  # 自动选择引擎
except:
    # 失败时尝试作为CSV读取
    try:
        df = pd.read_csv(file_name, encoding_errors='ignore')
    except Exception as e:
        print(f"无法识别文件格式：{str(e)}")
        raise

# ====== 后续处理保持不变 ======
df.insert(
    loc=df.columns.get_loc('title') + 1,
    column='fixed_PublishedAt',
    value=df['title'].str.extract(r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)', expand=False)
)
df.drop('title', axis=1, inplace=True)

# 保存并下载
output_name = f"processed_{file_name.split('.')[0]}.xlsx"
df.to_excel(output_name, index=False)
files.download(output_name)



from google.colab import files
import pandas as pd
from io import BytesIO
import os
import time

def merge_files_safely():
    print("📂 请选择要合并的文件（支持 .xlsx / .xls / .csv）：")
    uploaded = files.upload()

    merged = pd.DataFrame()

    for name, file in uploaded.items():
        ext = os.path.splitext(name)[1].lower()
        try:
            if ext in ['.xlsx', '.xls']:
                df = pd.read_excel(BytesIO(file))
            elif ext == '.csv':
                try:
                    df = pd.read_csv(BytesIO(file))
                except:
                    df = pd.read_csv(BytesIO(file), encoding='gbk')
            else:
                print(f"⚠️ 跳过不支持的文件：{name}")
                continue

            merged = pd.concat([merged, df], ignore_index=True)
            print(f"✅ 已合并：{name}（{len(df)} 行）")
        except Exception as e:
            print(f"❌ 读取失败：{name} - {e}")

    if merged.empty:
        print("⚠️ 没有成功合并任何文件。")
        return

    filename = f"合并结果_{time.strftime('%Y%m%d_%H%M%S')}.xlsx"
    merged.to_excel(filename, index=False)
    print(f"\n🎉 合并完成！共 {len(merged)} 行，{len(merged.columns)} 列")
    print("📥 正在下载合并结果文件...")
    files.download(filename)

merge_files_safely()

from google.colab import files
import pandas as pd
from io import BytesIO
import os

def process_column_safely():
    print("📂 请选择要处理的文件（仅支持 1 个 .xlsx / .xls / .csv）：")
    uploaded = files.upload()

    if not uploaded:
        print("⚠️ 没有选择文件")
        return

    # 只处理第一个文件
    filename, file_data = next(iter(uploaded.items()))
    ext = os.path.splitext(filename)[1].lower()

    try:
        # 读取文件
        if ext in ['.xlsx', '.xls']:
            df = pd.read_excel(BytesIO(file_data))
        elif ext == '.csv':
            try:
                df = pd.read_csv(BytesIO(file_data))
            except UnicodeDecodeError:
                df = pd.read_csv(BytesIO(file_data), encoding='gbk')
        else:
            raise ValueError("❌ 不支持的文件格式")

        # 检查必要列
        required_cols = ['Same_video_group', 'region']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            raise KeyError(f"❌ 缺少必要列：{', '.join(missing_cols)}")

        # 显示原始预览
        print("📄 原始数据预览（前5行）：")
        display(df.head())

        # 处理列
        df['Same_video_group'] = df['region'].astype(str) + df['Same_video_group'].astype(str)

        # 显示处理后预览
        print("\n✨ 处理后的数据预览（前5行）：")
        display(df.head())

        # 保存并下载
        new_filename = f"processed_{filename}"
        if ext in ['.xlsx', '.xls']:
            df.to_excel(new_filename, index=False)
        else:
            df.to_csv(new_filename, index=False)
        print("📥 正在下载处理后的文件...")
        files.download(new_filename)

    except Exception as e:
        print(f"❌ 处理失败：{str(e)}")

# 运行程序
process_column_safely()

from google.colab import files
import pandas as pd
from io import BytesIO
import os

def process_column_safely():
    print("📂 请选择要处理的文件（仅支持 1 个 .xlsx / .xls / .csv）：")
    uploaded = files.upload()

    if not uploaded:
        print("⚠️ 没有选择文件")
        return

    # 只处理第一个文件
    filename, file_data = next(iter(uploaded.items()))
    ext = os.path.splitext(filename)[1].lower()

    try:
        # 读取文件
        if ext in ['.xlsx', '.xls']:
            df = pd.read_excel(BytesIO(file_data))
        elif ext == '.csv':
            try:
                df = pd.read_csv(BytesIO(file_data))
            except UnicodeDecodeError:
                df = pd.read_csv(BytesIO(file_data), encoding='gbk')
        else:
            raise ValueError("❌ 不支持的文件格式")

        # 检查必要列
        required_cols = ['Same_video_group', 'region']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            raise KeyError(f"❌ 缺少必要列：{', '.join(missing_cols)}")

        # 显示原始预览
        print("📄 原始数据预览（前5行）：")
        display(df.head())

        # 处理列
        df['Same_video_group'] = df['region'].astype(str) + df['Same_video_group'].astype(str)

        # 显示处理后预览
        print("\n✨ 处理后的数据预览（前5行）：")
        display(df.head())

        # 保存并下载
        new_filename = f"processed_{filename}"
        if ext in ['.xlsx', '.xls']:
            df.to_excel(new_filename, index=False)
        else:
            df.to_csv(new_filename, index=False)
        print("📥 正在下载处理后的文件...")
        files.download(new_filename)

    except Exception as e:
        print(f"❌ 处理失败：{str(e)}")

# 运行程序
process_column_safely()