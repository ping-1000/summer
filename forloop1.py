#forloop1.py
print("DEC\tHEX\tBIN\tCHAR")
for d in range(32,128):
	h=hex(d)
	h=h.replace("0x","$ ")
	
	# ~ o=oct(d)
	b=bin(d)
	b=b.replace("0b","- ")
	
	c=chr(d)
	# ~ print(str(d)+" "+h,end="")
	print(str(d)+"\t"+h+"\t"+b+"\t"+c)
