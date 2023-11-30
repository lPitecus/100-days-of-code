import smtplib
import os


def send_mail(who_will_receive: str, subject: str, message: str):
    """Sends an email to someone.

    :param who_will_receive: str - user who will receive the mail.
    :param subject: str - Title of the email.
    :param message: str - Message on the body of the mail
    """

    my_google_email = os.environ.get('EMAIL')
    # noinspection SpellCheckingInspection
    password_google = os.environ.get('PASSWORD')

    with smtplib.SMTP(host="smtp.gmail.com", port=587, timeout=120) as connection:
        connection.starttls()
        connection.login(user=my_google_email, password=password_google)
        connection.sendmail(
            from_addr=my_google_email,
            to_addrs=who_will_receive,
            msg=f"Subject: {subject}\n\n{message}".encode("utf8")
        )       # envia um email para uma conta específicada


send_mail("tuzaum.silva@gmail.com", "testes", "oieee")

