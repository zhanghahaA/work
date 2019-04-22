from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib
def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

from_addr='1360061257@qq.com'
hah=input('模拟发件人')
password='ttfcoeihhmcljbeb'
to_addr='3441717698@qq.com'
zhengwen=input('请输入正文:')
smtp_server='smtp.qq.com'
msg=MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
msg['From']=_format_addr('python爱好者<%s>'%hah)
msg['To']=_format_addr('管理 <%s>'%to_addr)
msg['Subject']=Header('来自张书源的问候...','utf-8').encode()

server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()