import email, imaplib

user = "osipov180"
pwd = "marat1991"

# connecting to the gmail imap server
m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login(user,pwd)
m.select("Inbox") # here you a can choose a mail box like INBOX instead
# use m.list() to get all the mailboxes

typ, data = m.search(None, 'FROM', '"info@jobnet.co.il"')

for num in data[0].split() :
    typ, data = m.fetch(num, '(RFC822)')     #fetch == get
    print('Message %sn%sn' % (num, data[0][1]))

m.close()
m.logout()