import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("500061181@stu.upes.ac.in", "abhinav111")
 
msg = "YOUR MESSAGE!"
server.sendmail("500061181@stu.upes.ac.in", "500061181@stu.upes.ac.in", msg)
server.quit()

