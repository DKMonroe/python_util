fahrenheit = int(raw_input('Enter the temperature in Fahrenheit and I will convert it to Celsius: '))
try:
	fahrenheit = float(inp)
	celsius = (fahrenheit - 32) * 5 / 9
	print "It is ", celsius, "degrees Celsius!"
except:
	print 'Please enter a number'