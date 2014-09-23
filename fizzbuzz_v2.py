import sys
num_arg=len(sys.argv)
if num_arg == 1:
	while True:
		try: 
			n=int(raw_input("Enter the upper bound: "))
			break
		except ValueError:
			print("Not a valid integer! Please try again")	
else:
	while True:
		try: 
			n=int(sys.argv[1])
			break
		except ValueError:
			print("input arg is not a valid integer! Please try again")
			exit()
for i in range(n):
	i=i+1
	if (i%3)==0 and (i%5)==0:
		print "fizzbuzz"
	elif (i%3)==0:
		print "fizz"
	elif (i%5)==0:
		print "buzz"
	else:
		print str(i)