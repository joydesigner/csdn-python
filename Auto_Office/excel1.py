import pandas as pd
import os
from send_email import send_email

# excel_path = input('excel文件路径： ')
excel_path = '渠道数据分析总表.xlsx'
data = pd.read_excel(excel_path)

names = {
    '瞿丹': 'jason.zhengxin@gmail.com',
    '陈文': 'jason.zhengxin@gmail.com',
}

dirname = 'exceldir'

if not os.path.exists(dirname):
    os.makedirs(dirname)

for name, email in names.items():
    df = data.loc[data['负责人'] == name]
    filepath = os.path.join(dirname, f'{name}.xlsx')
    writer = pd.ExcelWriter(filepath)
    df.to_excel(writer, 'Sheet1')
    writer.save()

    if email:
        # send email
        send_email(name, email, filepath)
