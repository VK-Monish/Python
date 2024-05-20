a=0
amount = 25000
if amount < 1000:
	a = amount-200
else:
	if amount > 5000:
		a = amount + 500
	else:
		if amount > 10000:
			a = amount / 100
		else:
			a = 100
print(a)

