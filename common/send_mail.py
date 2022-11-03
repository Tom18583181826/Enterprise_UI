import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.read_ini import ReadIni


class SendMail(object):
    def send_mail(self, path):
        try:
            # 1.配置邮箱服务器信息
            host = "smtp.qq.com"

            sender = ""
            auth_code = ""
            receivers = ""

            # 2.创建邮件对象
            message = MIMEMultipart()
            message["from"] = sender
            message["to"] = receivers
            message["subject"] = "测试报告"
            with open(path, mode="rb") as report:
                mail_body = report.read().decode(encoding="utf8")

            # 3.编写正文
            text = MIMEText(mail_body, "html", "utf8")
            message.attach(text)

            # 4.添加附件
            attachment = MIMEText(mail_body, "base64", "utf8")
            attachment["Content-Type"] = "application/octet-stream"
            attachment["Content-Disposition"] = 'attachment;filename = %s' % path
            message.attach(attachment)

            # 5.发送邮件
            smtpobj = smtplib.SMTP()
            smtpobj.connect(host)
            smtpobj.login(sender, auth_code)
            smtpobj.sendmail(sender, receivers.split(";"), message.as_string())
            print("邮件发送成功！！！")
        except smtplib.SMTPException:
            print("邮件发送失败！！！")


if __name__ == '__main__':
    read = ReadIni()
    report_file_path = read.get_report_file_path()
    test_send = SendMail()
    test_send.send_mail(report_file_path)
