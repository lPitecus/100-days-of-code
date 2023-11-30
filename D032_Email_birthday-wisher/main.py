"""oi"""
import smtplib
import random
import datetime as dt
from tkinter import messagebox
import os
import pandas


def send_mail(who_will_receive: str, subject: str, message: str):
    """Sends an email to someone.

    :param who_will_receive: str - user who will receive the mail.
    :param subject: str - Title of the email.
    :param message: str - Message on the body of the mail
    """

    my_google_email = os.environ.get('EMAIL')
    # noinspection SpellCheckingInspection
    password_google = os.environ.get('PASSWORD')

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_google_email, password=password_google)
        connection.sendmail(
            from_addr=my_google_email,
            to_addrs=who_will_receive,
            msg=f"Subject: {subject}\n\n{message}".encode("utf8")
        )       # envia um email para uma conta específicada


# 1. Update the birthdays.csv

# 2. Check if today matches a birthdays_today in the birthdays.csv
current_date = dt.datetime.now()
current_day = float(current_date.day)
current_month = float(current_date.month)

df = pandas.read_csv("birthdays.csv")
# dataframe with all birthdays on today's date.
birthdays_on_day = df[df["day"] == current_day]
# dataframe with all birthdays on today's date and today's month.
birthdays_today = birthdays_on_day[birthdays_on_day["month"] == current_month]

# transforming the data into a dict with all the person's information.
birthday_persons_info = birthdays_today.to_dict(orient="records")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the
# person's actual name from birthdays.csv
letters = [
    "letter_templates/letter_1.txt",
    "letter_templates/letter_2.txt",
    "letter_templates/letter_3.txt"
]

# reading one of the base letters and saving into the variable letter_content.
with open(random.choice(letters), mode="r", encoding="utf8") as base_letter:
    letter_content = base_letter.read()

# create a letter for each birthday person.
for person in birthday_persons_info:
    with open(f"Outputs/birthday_letter_for_{person['name']}",
              mode="w",
              encoding="utf8") as birthday_letter:
        new_letter = letter_content.replace("[NAME]", person["name"])
        birthday_letter.write(new_letter)

# 4. Send the letter generated in step 3 to that person's email address.
    with open(f"Outputs/birthday_letter_for_{person['name']}", mode="r", encoding="utf8") as letter:
        complete_letter = letter.read()
        send_mail(
            who_will_receive=person["email"],
            subject="Feliz Aniversário!!",
            message=complete_letter
        )

# inform to the user that the emails have been sent.
birthday_names = [person["name"] for person in birthday_persons_info]
messagebox.showinfo(title="Success!",
                    message=f"E-mail for {', '.join(birthday_names)} sent successfully")
