from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
host_server='stmp.qq.com'
sender_qq='1360061257@qq.com'
pwd='ttfc oeih hmcl jbeb'
sender_qq_mail='1360061257@qq.com'
receiver='13231031398@163.com'
mail_content='nihaoay'
mail_title='max'
smtp=SMTP_SSL(host_server)
smtp.set_debuglevel(1)
smtp.ehlo(host_server)
smtp.login(sender_qq,pwd)
msg=MIMEText(mail_content,'plain','utf-8')
msg['Subject']=Header(mail_title,'utf-8')
msg['From']=sender_qq_mail
msg['To']=receiver
smtp.sendmail(sender_qq_mail,receiver,msg.as_string())
smtp.quit()