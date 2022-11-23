import requests
order_currency = 'BTC' 
payment_currency = 'KRW' 
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
response = requests.get(URL)
data = response.json() # 데이터는 리스폰스를 제이슨 형식으로 읽은 것.
print(data.get('data').get('prev_closing_price')) 