mark = int(input())
result =" "
if mark < 35:
	result = "failed"
elif mark > 75:
	result = "pass"
else:
	result = "passed"
print(result)

