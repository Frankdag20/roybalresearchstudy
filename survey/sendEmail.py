import datetime
import calendar
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(participant):
    now = datetime.datetime.now()

    today_date = datetime.date.today()  # today's date

    cy = now.year  # current year
    cm = now.month  # current month
    cd = now.day # current day
    participant = participant + 1
    FROM = "fdagostinoj@gmail.com"
    #TO = ["frankdag20@gmail.com"]  # must be a list
    TO = ["frankdag20@gmail.com"]  # must be a list

    SUBJECT = "Hello!"
    TEXT = """Hello,
    
     This is an automatic email notifying you that Participant 1 has not yet filled out the survey for today."""

    # Prepare actual message
    #message = """From: %s To: %s Subject: %s
    #
    # %s
    # """ % (FROM, ", ".join(TO), "Hello", TEXT)

    # Prepare actual message
    message = """Subject: %s
    
    %s
     """ % ("Research Notification", TEXT)

    # Send the mail
    username = str("fdagostinoj@gmail.com")
    password = str("dagostino1")

    server = smtplib.SMTP("smtp.gmail.com", 587, timeout=30)
    server.set_debuglevel(1)

    try:
        server.starttls()
        server.login(username, password)
        server.sendmail(FROM, TO, message)
        print("The reminder e-mail for WK-2 was sent !")
    except:
        print("Couldn't send e-mail regarding WK-2")
    finally:
        server.quit()
    # input("Press any key to exit..")