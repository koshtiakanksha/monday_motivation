import datetime as dt
import smtplib
import random

now = dt.datetime.now()
current_day = now.weekday()

my_email = "----------@gmail.com"
my_password = "********"

if current_day == 0:
    with open("quotes.txt", "r") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="______________",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
