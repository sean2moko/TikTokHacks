import os
import smtplib
import imghdr
from email.message import EmailMessage
import re

EMAIL_ADDRESS = seanmax2004@icloud.com
EMAIL_PASSWORD = Sean11162004

firstname = Sean-Maxwell
lastname = Massey
address = 7621 Addison Way
town = Sacramento 
zip = 95822
state = California 

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
	with open("test.txt") as fp:
		line = fp.readline()
		while(line):
			linesplit = re.split(r'\t+', line)
			print(linesplit[0] + " : " + linesplit[1])
			msg = EmailMessage()
			msg['Subject'] = 'A Request From A Future Applicant'
			msg['From'] = EMAIL_ADDRESS
			msg.set_content('Hello ' + linesplit[0] + ' Admissions.\n\nI just finished my overseas gap-year program and want to apply to ' + linesplit[0] + ' for the upcoming spring semester. It would mean the world to me you could send me a shirt so I could represent your university.\n\nIf possible, could you please send to \n\n'+ firstname + ' ' + lastname +'\n'+ address + '\n' + town + ',' + state + ' ' + zip + '\n\n Thank you,\n' + firstname)
			msg['To'] = linesplit[1]
			line = fp.readline()		
			smtp.send_message(msg)
