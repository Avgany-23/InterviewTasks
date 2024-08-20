from email.message import Message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import email
import smtplib
import imaplib
from typing import Optional


class EmailSession:
    def __new__(cls, login: str, password: str) -> Optional['EmailSession']:
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.ehlo(), smtp.starttls(), smtp.ehlo()
        try:
            smtp.login(login, password)
        except smtplib.SMTPAuthenticationError:
            print('Неверные данные для входа. Объект класса не создан')
            return None
        else:
            return super().__new__(cls)
        finally:
            smtp.quit()

    def __init__(self, login: str, password: str) -> None:
        self.login = login
        self.password = password

    def send_message(self, to: list, message: str, subject: str) -> None:
        msg = MIMEMultipart()
        msg['From'], msg['To'], msg['Subject'] = [self.login, ', '.join(to), subject]
        msg.attach(MIMEText(message))
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.ehlo(), smtp.starttls(), smtp.ehlo()
        smtp.login(self.login, self.password)
        smtp.sendmail(self.login, to, msg.as_string())
        smtp.quit()

    def get_message(self, header=None) -> Message:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(self.login, self.password), mail.list(), mail.select("inbox")
        result, data = mail.uid('search', '(HEADER Subject "%s")' % header if header else 'ALL')
        if data[0]:
            raise AssertionError('There are no letters with current header')

        result, data = mail.uid('fetch', data[0].split()[-1], '(RFC822)')
        result = email.message_from_string(data[0][1])
        mail.logout()

        return result


if __name__ == '__main__':
    from dotenv import load_dotenv
    import os

    load_dotenv()

    session = EmailSession(login=str(os.getenv('LOGIN_GOOGLE')),
                           password=str(os.getenv('PASSWORD_GOOGLE')))
    if session:
        session.send_message(to=['vasya@email.com', 'petya@email.com'],
                             message='Message',
                             subject='Subject')
        session.get_message()