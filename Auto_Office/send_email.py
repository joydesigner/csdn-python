import yagmail


def send_email(name, to, filepath):
    contents = f'''
  {name}, 您好，你的汇报数据已整理发送到邮件附件
  '''

    yag = yagmail.SMTP(
        user='joy_designer@sina.com',
        password='4922696ecc3a367f',
        host='smtp.sina.com'
    )

    yag.send(to=to, subject='汇报数据', contents=contents, attachments=filepath)
