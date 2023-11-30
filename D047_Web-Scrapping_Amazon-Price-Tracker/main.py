import time
import requests
from bs4 import BeautifulSoup
import smtplib

AMAZON_URL = ("https://www.amazon.com.br/Olympikus-43448165-T%C3%AAnis-Eros/dp/B0BCBXKMB4/ref=sr_1_12?crid"
              "=3IHK7ZEIVZRCW&keywords=tenis%2Bolympikus%2Bmasculino&qid=1697651888&sprefix=tenis%2Bol%2Caps%2C206&sr"
              "=8-12&ufe=app_do%3Aamzn1.fos.6121c6c4-c969-43ae-92f7-cc248fc6181d&th=1&psc=1")


def get_values() -> tuple:
    headers = {
        "User-Agent": "Defined"
    }
    response = requests.get(AMAZON_URL, headers=headers)
    response.encoding = "utf-8"
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    price_whole = soup.find(name="span", class_="a-price-whole")
    price_fraction = soup.find(name="span", class_="a-price-fraction")
    item_name = soup.find(name="span", id="productTitle")
    return price_whole, price_fraction, item_name


def send_mail(who_will_receive: str, subject: str, message: str):
    """Sends an email to someone.

    :param who_will_receive: str - user who will receive the mail.
    :param subject: str - Title of the email.
    :param message: str - Message on the body of the mail
    """

    my_google_email = "pythontuzin@gmail.com"
    # noinspection SpellCheckingInspection
    password_google = "hmtypcsrtbhksmck"

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_google_email, password=password_google)
        connection.sendmail(
            from_addr=my_google_email,
            to_addrs=who_will_receive,
            msg=f"Subject: {subject}\n\n{message}".encode("utf8")
        )  # envia um email para uma conta específicada


def main():
    product_info = get_values()
    price_whole = product_info[0]
    price_fraction = product_info[1]
    item = product_info[2]

    if price_whole is None or price_fraction is None:
        time.sleep(3)
        main()
    else:
        price = float(f"{price_whole.text[:-1]}.{price_fraction.text}")
        if price < 160.0:
            send_mail(
                who_will_receive="tuzaum.silva@gmail.com",
                subject="Alerta de preço baixo!",
                message=f"O valor do item {item.text.strip()} está por"
                        f" apenas R${round(price, 2)}\n\nLink para o produto: {AMAZON_URL}"
            )
        print(price)


if __name__ == '__main__':
    main()
