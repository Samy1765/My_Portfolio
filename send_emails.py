import smtplib, ssl

def send_email(message):
   host="smtp.gmail.com"
   port=587

   username="swayamdeshmukh1765p@gmail.com"
   password="egttctrvqcjelxul"   
   reciever="swayamdeshmukh1765p@gmail.com"
   context=ssl.create_default_context

   with smtplib.SMTP_SSL(host,port,context=context) as server:
      server.login(username,password)
      server.sendmail(username,reciever,message)