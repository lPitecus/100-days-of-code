import time
import os
import requests
from datetime import datetime, timezone
import smtplib


MY_LAT = -5.794560
MY_LONG = -35.210400


def send_mail(who_will_receive: str, subject: str, message: str) -> None:
    """Sends an email to someone.

    :param who_will_receive: str - user who will receive the mail.
    :param subject: str - Title of the email.
    :param message: str - Message on the body of the mail
    """

    my_google_email = os.environ.get('NAME')
    # noinspection SpellCheckingInspection
    password_google = os.environ.get('PASSWORD')

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:       # conecta ao serviço de email desejado
        connection.starttls()       # cria uma criptografia para os emails enviados
        connection.login(user=my_google_email, password=password_google)        # entra na conta desejada
        connection.sendmail(
            from_addr=my_google_email,
            to_addrs=who_will_receive,
            msg=f"Subject: {subject}\n\n{message}".encode("utf8")
        )       # envia um email para uma conta específicada


# getting the iss position
def is_iss_overhead() -> bool:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5) and (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5)


def is_night() -> bool:
    # getting the hour of sunset and sunrise of my location
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now(timezone.utc)
    return time_now.hour > sunset or time_now.hour < sunrise


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        send_mail(who_will_receive="arthurxboxelite@hotmail.com",
                  subject="OLHE PRA CIMA",
                  message="A ISS ESTÁ PASSANDO POR NOS!!")
