import pandas
import random
import smtplib
import datetime as dt

data = pandas.read_csv("birthdays.csv")
list_data = data.to_dict(orient="records")

now = dt.datetime.now()
year = now.year
day = now.day
month = now.month

my_email = "nirupamsur10@gmail.com"
password = "zxcvbnm@1"


for data in list_data:
    placeholder = "[NAME]"
    if day == data['day'] and month == data['month']:
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
            letter_contents = letter_file.read()
            new_letter = letter_contents.replace(placeholder, data['name'])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=data['email'], msg=f"Subject:Birthday Wish\n\n{new_letter}")
