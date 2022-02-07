import smtplib

sender = 'vanshbafnajain@gmail.com'
pswd = 'wfcgrjpdladotccn'
reciver = ['vanshbafnajain@gmail.com']
message = 'Hi! This Is Vansh, This Is A Test Email'



try:
	server = smtplib.SMTP("smtp.gmail.com",587)
	server.starttls() 
	server.login(sender, pswd)
	print("sucess")
	server.sendmail(sender, reciver, message)
	print("email sent")
	
except Exception as e:
	print(e)
finally:
	server.quit()
