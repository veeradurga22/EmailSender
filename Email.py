
def EMailSend(toaddr,filename=None,subject="",b=""):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    fromaddr = "Enter ur Email"                 #from address
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    body = b
    msg.attach(MIMEText(body, 'plain'))
    if filename:
        filename = filename
        attachment = open(filename, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "Enter user gmail password here")
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()
    return 1
