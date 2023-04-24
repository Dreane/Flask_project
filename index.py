from flask import Flask, render_template, request
import requests
import sqlite3

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    con_service = sqlite3.connect('db/service.sqlite')
    cur_service = con_service.cursor()
    con_staffer = sqlite3.connect('db/staffers.sqlite')
    cur_staffer = con_staffer.cursor()
    services = [i for i in cur_service.execute("""SELECT * FROM services""").fetchall()]
    subservices = [i for i in cur_service.execute("""SELECT * FROM subservices""").fetchall()]
    staffers = [list(i) for i in cur_staffer.execute("""SELECT * FROM staffers""").fetchall()]
    for staffer in staffers:
        year = str(staffer[3])
        if year[-1] == '1' and year != '11':
            staffer[3] = str(staffer[3]) + ' год'
        elif (year[-1] == '2' and year != '12') or (year[-1] == '3' and year != '13') or (
                year[-1] == '4' and year != '14'):
            staffer[3] = str(staffer[3]) + ' года'
        else:
            staffer[3] = str(staffer[3]) + ' лет'

    return render_template('index.html', services=services, subservices=subservices, staffers=staffers)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return '1'


@app.route('/read-form', methods=['POST'])
def read_form():
    data = request.form
    name = data['name']
    phone_number = data['phone_number']
    add_info = data['text']
    send_message((name, phone_number, add_info))
    return render_template('base.html')


def send_message(data):
    name, phone_number, add_info = data
    message = f'Новая заявка:\nИмя: {name}\nНомер телефона: {phone_number}\n Дополнительная информация: {add_info}'.replace(
        ' ', '%20')
    token = "6213433237:AAE0I83JDZOPGypuXKvlJWv2vnWfgrtw7sc"
    chat_id = '-834333581'
    send = requests.get(
        f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=html&text={message}')


if __name__ == "__main__":
    app.debug = True
    app.run(port=8080, host='127.0.0.1')
