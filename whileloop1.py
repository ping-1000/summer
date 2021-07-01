#whileloop1.py
d = 0
while d < 101:
	sqaured = d**2
	print(d,sqaured," ",end="")
	d += 1
	if d % 5 == 0:
		print()
