$pip install dnspython
# Gathering Relevant Data from User
First_Name = input("Enter the First Name : ") 
First_Initial = First_Name[0]
Last_Name = input("Enter the Last Name : ") 
Last_Initial = Last_Name[0]
Domain_Name = input("Enter the Domain/Compnany Name : ") 
Bare_Min = '@' + Domain_Name + '.com'
DN = Domain_Name + '.com'

#Finding Out All Possible E-mails
mails = []
mails.append(First_Name + Bare_Min)
mails.append(Last_Name + Bare_Min)
mails.append(First_Name + Last_Name + Bare_Min)
mails.append(First_Name + '.' + Last_Name + Bare_Min)
mails.append(First_Initial + Last_Name + Bare_Min)
mails.append(First_Initial + '.' + Last_Name + Bare_Min)
mails.append(First_Name + Last_Initial + Bare_Min)
mails.append(First_Name + '.' + Last_Initial + Bare_Min)
mails.append(First_Initial + Last_Initial + Bare_Min)
mails.append(First_Initial + '.' + Last_Initial + Bare_Min)
mails.append(Last_Name + First_Name + Bare_Min)
mails.append(Last_Name + '.' + First_Name + Bare_Min)
mails.append(Last_Name + First_Initial + Bare_Min)
mails.append(Last_Name + '.' + First_Initial + Bare_Min)
mails.append(Last_Initial + First_Name + Bare_Min)
mails.append(Last_Initial + '.' + First_Name + Bare_Min)
mails.append(Last_Initial + First_Initial + Bare_Min)
mails.append(Last_Initial + '.' + First_Initial + Bare_Min)
mails.append(First_Name + '-' + Last_Name + Bare_Min)
mails.append(First_Initial + '-' + Last_Name + Bare_Min)
mails.append(First_Name + '-' + Last_Initial + Bare_Min)
mails.append(First_Initial + '-' + Last_Initial + Bare_Min)
mails.append(Last_Name + '-' + First_Name + Bare_Min)
mails.append(Last_Name + '-' + First_Initial+ Bare_Min)
mails.append(Last_Initial + '-' + First_Name + Bare_Min)
mails.append(Last_Initial + '-' + First_Initial + Bare_Min)
mails.append(First_Name + '_' + Last_Name + Bare_Min)
mails.append(First_Initial + '_' + Last_Name+ Bare_Min)
mails.append(First_Name + '_' + Last_Initial + Bare_Min)
mails.append(First_Initial + '_' + Last_Initial + Bare_Min)
mails.append(Last_Name + '_' + First_Name + Bare_Min)
mails.append(Last_Name + '_' + First_Initial + Bare_Min)
mails.append(Last_Initial + '_' + First_Name + Bare_Min)
mails.append(Last_Initial + '_' + First_Initial + Bare_Min)

#Printing all Possible E-mails
print("Given Below are All the Possible E-mails Based on the Details Entered :-")
for x in mails:
    print(x)
    
#Verifying how Many of These E-mails Actually Exist
import smtplib
import socket   
import dns.resolver
Add = 'shubhamgdd@gmail.com'
records = dns.resolver.query(DN, 'MX')
MXR = records[0].exchange
MXR = str(MXR)
host = socket.gethostname()
server = smtplib.SMTP()
server.set_debuglevel(0)
success = []
for x in mails:
    server.connect(MXR)
    server.helo(host)
    server.mail(Add)
    code, message = server.rcpt(x)
    server.quit()
    if code == 250:
        success.append(x)

#Printing All Existing E-mails from the List
for x in success:
    print(x)