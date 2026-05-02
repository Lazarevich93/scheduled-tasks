import smtplib
import random
import datetime as dt
import pandas

MY_PYTHON_MAIL = "slobodanpy@gmail.com"
MY_PYTHON_MAIL_PASSWORD = "ohutiuvvuvupwdge"

csv = pandas.read_csv("birthdays.csv")


def send_email(to, subject, body):
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=MY_PYTHON_MAIL, password=MY_PYTHON_MAIL_PASSWORD)
        connection.sendmail(from_addr=MY_PYTHON_MAIL, to_addrs=to,msg=f"Subject: {subject} \n\n{body}")

now = dt.datetime.now()
today = (now.month,now.day)

# birthday_dict = {(csv_row.month,csv_row.day):csv_row for (index,csv_row) in csv.iterrows()}

birthday_dict = {}

for (index, row) in csv.iterrows():
    key = (row.month, row.day)
    if key not in birthday_dict:
        birthday_dict[key] = []
    birthday_dict[key].append(row)
print(birthday_dict)
#{(Mesec,Dan):[Objekat Ime1, Objekat Ime2...]}


if today in birthday_dict:
    for birthday_person in birthday_dict[today]:
        file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"

        with open(file_path) as letter_file:
            content = letter_file.read()
            content = content.replace("[NAME]", birthday_person["name"])

        send_email(to=birthday_person["email"], subject="Happy Birthday!",body= content)
