import poplib
from email.parser import Parser
from email.header import decode_header


def connect_email():
    user = 'joy_designer@sina.com'
    password = '4922696ecc3a367f'
    host = 'pop.sina.com'

    server = poplib.POP3(host)

    server.set_debuglevel(1)
    print(server.getwelcome().decode('utf-8'))

    server.user(user)
    server.pass_(password)
    return server


def get_email_content(server):
    email_num, email_size = server.stat()
    rsp, msglines, msgsiz = server.retr(email_num)
    msg_content = b'\r\n'.join(msglines).decode()
    msg = Parser().parsestr(msg_content)
    server.close()
    return msg


def parse_subject(msg):
    subject = msg['Subject']
    value, charset = decode_header(subject)[0]
    if charset:
        value = value.decode(charset)
    return charset



def main():
    server = connect_email()
    msg = get_email_content(server)
    subject = parse_subject(msg)
    print(msg)
    print(subject)


main()
