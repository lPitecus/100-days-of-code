import smtplib
import random
import datetime as dt


def send_mail(who_will_receive: str, subject: str, message: str):
    """Sends an email to someone.

    :param who_will_receive: str - user who will receive the mail.
    :param subject: str - Title of the email.
    :param message: str - Message on the body of the mail
    """

    my_google_email = "pythontuzin@gmail.com"
    # noinspection SpellCheckingInspection
    password_google = "hmtypcsrtbhksmck"

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:       # conecta ao serviço de email desejado
        connection.starttls()       # cria uma criptografia para os emails enviados
        connection.login(user=my_google_email, password=password_google)        # entra na conta desejada
        connection.sendmail(
            from_addr=my_google_email,
            to_addrs=who_will_receive,
            msg=f"Subject: {subject}\n\n{message}".encode("utf8")
        )       # envia um email para uma conta específicada


current_date = dt.datetime.now()
day_of_week = current_date.weekday()
with open("quotes.txt", mode="r") as quotes:
    list_of_quotes = quotes.readlines()
    clean_list_of_quotes = [quote.strip("\n") for quote in list_of_quotes]

if day_of_week == 0:
    send_mail(
        who_will_receive="pythontuzin@yahoo.com",
        subject="Frase motivacional em inglês mano",
        message=random.choice(clean_list_of_quotes)
    )
