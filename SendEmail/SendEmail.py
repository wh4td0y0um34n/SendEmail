# Import Library smtplib 
import smtplib

# Setup Email Login 
gmail_user = input (str("Masukan Akun Gmail : "))
gmail_app_pass = input(str("Masukan Password Gmail : "))

# Setup Pengirim, penerima, judul dan isi email 

sent_from = gmail_user
sent_to = input(str("Masukan Gmail Penerima Lalu Akhiri Dengan Enter : "))
sent_subject = input(str("Masukan Subject : "))
sent_body = input(str("Masukan Pesan : "))

email_text = """\ 
From : %s 
To : %s
Subject : %s

%s
""" % (sent_from, ",".join(sent_to), sent_subject, sent_body)

try : 
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_app_pass)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()

    print('Email Sent!')
except Exception as exception:
    print("Eror : %s!\n\n" % exception)
