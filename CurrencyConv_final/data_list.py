index_nums = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33"
currency_codes = "Select,AUD,BGN,BRL,CAD,CHF,CNY,CZK,DKK,EUR,GBP,HKD,HRK,HUF,IDR,ILS,INR,ISK,JPY,KRW,MXN,MYR,NOK,NZD,PHP,PLN,RON,RUB,SEK,SGD,THB,TRY,USD,ZAR"
codes = currency_codes.split(",")
nums = index_nums.split(" ")
nums_and_codes = zip(nums,codes)

code_dict = dict(nums_and_codes)


#for cur_code in codes:
	#print(cur_code)
#print(codes)
#print(nums)
#print(currency_codes)
#print(code_dict)
#print(nums_and_codes)







