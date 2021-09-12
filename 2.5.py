import requests
from tabulate import tabulate
import json

username = 'luceed_mb'
password = '7e5y2Uza'

urlTemplate = 'http://apidemo.luceed.hr/datasnap/rest/artikli/naziv/{query}'

while True:
	query = input("unesite pojam za pretragu: ")
	if query != '':
		break
	print('morate unijeti pojam za pretragu')

url = urlTemplate.format(
	query = query
)

request = requests.get(url, auth = (username, password))
response = request.json()

# response = json.load(open('response.json'))

if 'error' in response:
	print('')
	print(response['error'].strip())
	print('')
	exit()

stavke = response['result'][0]['artikli']

if len(stavke) == 0:
	print('')
	print('Nema stavki za prikazati')
	print('')
	exit()

stavke = list(map(lambda i: { 'artikl': i['artikl'], 'naziv': i['naziv']}, stavke))

header = stavke[0].keys()
rows =  [x.values() for x in stavke]

print(tabulate(rows, header))