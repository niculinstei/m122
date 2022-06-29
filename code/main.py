import requests
import json
from urllib.request import urlopen
import yagmail
from fpdf import FPDF
from datetime import date

API_KEY = "6612968d9b1f2c245fed7442ad724039"


def applicationStart():
    url2 = f'https://api.openweathermap.org/data/2.5/weather?q={getcity()}&appid={API_KEY}&units=metric'
    data = requests.get(url2).json()
    temperatur = data['main']['temp']
    humidity = data['main']['humidity']

    loc = getLoc().split(",")

    lat = loc[0]

    lon = loc[1]

    url3 = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
    data2 = requests.get(url3).json()
    weather = data2['weather'][0]['main']
    description = data2['weather'][0]['description']

    mail1 = 'steiner.niculin@gmail.com'
    mail2 = 'steiner.niculin@mail.ch'
    mail3 = 'larasara04@hotmail.com'

    user = 'steiner.niculin@gmail.com'
    app_password = 'ykrencifzjupppsx'  # a token for gmail
    to = mail3

    subject = 'Ihre Wetterdaten'

    # makePDF
    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=15, style='B')

    pdf.cell(200, 10, txt="The weather for " + getcity() + " is: ",
             ln=1, align='C')
    pdf.set_font("Arial", size=15)

    pdf.set_left_margin(77)

    pdf.cell(200, 10, txt=f'Temperatur: {temperatur}°',
             ln=2)
    pdf.cell(200, 10, txt=f'Humidity: {humidity}%',
             ln=3)
    pdf.cell(200, 10, txt=f'Weather: {weather}',
             ln=4)
    pdf.cell(200, 10, txt=f'Description: {description}',
             ln=5)

    pdf.set_left_margin(0, )
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, txt="Recommend Clothes: ",
             ln=1, align='C')

    clothes = getClothes(temperatur, weather)
    counter = 1
    x = 0
    for i in clothes:
        y = 50 * counter
        pdf.cell(0, 50, txt=f"{i.split('.')[0].split('/')[1]}", ln=1, align='C')
        pdf.image(i, 80, y, 40, 40)
        counter += 1

    pdf.output("Wetterdaten.pdf")

    with yagmail.SMTP(user, app_password) as yag:
        yag.send(to, subject, "Wetterdaten.pdf")
        print('Sent email successfully')


def getcity():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    city = json.load(response)['region']
    return city


def getLoc():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    loc = json.load(response)['loc']
    return loc


def getClothes(temperatur, weather):
    # weather = 'Rain'

    # temperatur = 15

    pullover = 'images/Pullover.jpg'
    tshirt = 'images/T-shirt.jpg'

    pants = ['images/Kurzehose.jpg', 'images/Langehose.jpg']

    shoes = ['images/Winterschuh.jpg', 'images/Schuh.jpg', 'images/Adilette.jpg']

    hat = ['images/Regenschirm.jpg', 'images/Sonnenbrille.jpg', 'images/Mütze.jpg', 'images/Kappie.jpg']

    jacket = [
        'images/Winterjacke.png',
        'images/Regenjacke.jpg', 'images/Jäckchen.jpg']

    if weather.__eq__('Rain'):
        return [hat[0], pullover, jacket[1], pants[1], shoes[1]]

    elif weather.__eq__('Clouds') and temperatur > 20:
        return [hat[3], pullover, tshirt, pants[0], shoes[1]]

    elif weather.__eq__('Clear') and temperatur > 25:
        return [hat[1], hat[3], pants[0], shoes[2], tshirt]

    elif temperatur < 10:
        return [pullover, hat[2], pants[1], shoes[0], jacket[0]]

    else:
        return [hat[3], pullover, tshirt, pants[0], shoes[1]]


applicationStart()
