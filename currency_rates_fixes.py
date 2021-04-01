from requests import get

def currency_rates(car):
	response = get('http://www.cbr.ru/scripts/XML_daily.asp')
	content = response.text
	istart = content.find(car.upper())
	if istart == -1:
		print('None')
	else:
		content_istart = content[istart + 3:]
		iend = content_istart.find('Value')
		end = iend +13

		while content_istart[end].isdigit():  # на случай если цифр больше чем в большистве валют
			end += 1

		res = content_istart[iend + 6: end].replace(',','.')

		return print(f'{content[60:70]} {content[istart: istart + 3]} - {float(res)} RUB')


currency_rates(car = 'usd')
currency_rates(car = 'eur')
currency_rates(car = input('Input your currency - '))