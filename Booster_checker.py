import requests
import sys

telegram_token = sys.argv[1]
telegram_chat_id = sys.argv[2]
url_vaccination_center_Kassel = sys.argv[3]

year_of_interest = 2021
month_of_interest = 12
product = 'Booster mit BioNTech'

appointments = requests.get(url_vaccination_center_Kassel).json()

if appointments != None:
    if str(year_of_interest) in appointments.keys():
        appointments_year = appointments[str(year_of_interest)]
        if str(month_of_interest) in appointments_year.keys():
            appointments_year_month = appointments_year[str(month_of_interest)]
            message = f'{year_of_interest}_{month_of_interest} gibt es folgende freie Termine: {", ".join([str(a) for a in appointments_year_month])} für {product}. Jetzt aber schnell'
            requests.get(url=f'https://api.telegram.org/bot{telegram_token}/sendMessage', data={
                'chat_id': str(telegram_chat_id), 'text': str(message)})
