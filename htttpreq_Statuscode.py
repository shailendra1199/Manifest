#import lib for Python Script to check if the website is up using Requests, BeautifulSoup4 & send email if its down
import requests
import bs4
import smtplib
import os

nginx_page= #website_url or ip_address

#export env for mail
email_add = os.environ.get('EMAIL_ADD')
password = os.environ.get('EMAIL_PASS')
#creating function for email

def send_email():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email_add, password)
    subject = "Nginx status "
    body = "Checking the availabilty of Nginx-website"
    message = f'Subject: {subject}\n\n {body}'
    s.sendmail(email_add, email_add, message)
    s.quit()

#getting req from webpage
getreq= requests.get(nginx_page,timeout=5)

print(getreq)
#printing status code 200 OK       
print(getreq.status_code)
#using condition if 
if getreq.status_code != 200:
    send_email()

soup = bs4.BeautifulSoup(getreq.text,'html.parser')
elements = soup.select("body > h1")
try:
    print(elements[0].text)
    if elements[0].text != "welcome to nginx on Amazon Linux!":
        send_email()

except Exception as e:
        send_email()
