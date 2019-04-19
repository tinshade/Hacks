import imaplib
box = imaplib.IMAP4_SSL('imap.gmail.com', 993)
box.login("mailID","Password")
box.select('Inbox')
typ, data = box.search(None,'from','mailID')
for num in data[0].split():
   box.store(num, '+FLAGS', '\\Deleted')
box.expunge()
box.close()
box.logout()

email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))