import smtplib
import random
my_email = "programmerjapanese@gmail.com"
password ="tobukuvxjwqhkiga"


with open("quotes.txt", "r") as file:
    c = file.read()
    #you can also use this -- c = file.readlines()  instead of c.split("\n")
    random_line = c.split("\n")

quote = random.choice(random_line)


import datetime as dt
now =dt.datetime.now()
year = now.year
month = now.month
day = now.day
weekDay= now.weekday()
if weekDay == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="saurabhjha3890@gmail.com",

                            msg=f"Subject:Monday Motivation\n\n {quote}"
                            )