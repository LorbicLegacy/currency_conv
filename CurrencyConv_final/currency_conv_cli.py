from forex_python.converter import CurrencyRates,CurrencyCodes
cr = CurrencyRates()
cd = CurrencyCodes()


def currency_rate(from_cd,to_cd,n = 1):
	return cr.get_rate(from_cd,to_cd)*n

def from_to_all(from_cd,n = 1):
	to_all = cr.get_rates(from_cd)
	return to_all*n

def oo():
	print(cr.get_rate('USD','INR'))
	print("Currency values for 1 USD")
	print("%5s  %20s  %10s"%("CODE","NAME","RATE"))
	for name, rate in sorted(usd_to_all.items()):
		print("%5s  %25s  %15f"%(name,cd.get_currency_name(name),rate))

#print(currency_rate("USD","INR"))