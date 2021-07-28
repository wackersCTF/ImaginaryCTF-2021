# documentation: https://docs.pwntools.com/en/stable/tubes.html
from time import sleep
from pwn import *
t = remote('chal.imaginaryctf.org', 42015) # connects to it
for i in range(310): # 300 addition problems but i increased it a bit
	data = str(t.recv(numb = None, timeout = 2))
	# reads the data and converts it to string
	print(data)
	if not("import" in data):
	# to prevent people from using eval(), the challenge randomly (about 2% of the time) outputs 
	# __import__['os'].system('{n}(){{ {n}|{n} & }};{{{n}}}') where n is a letter 
	# you just need to press enter or send a new line to skip it
		if i == 0:
		# the first problem has a lot of unnecessary text, it would require special removal
		# since i dont want to do that, i just compute the first problem manually
			t.send(input("Sum: "))
		else:
			data = data.replace(chr(92), "") # replaces instances of backslash (\)
			data = data.replace("b'Correct!n", "") # removes unnecessary text
			data = data.replace("n> '", "")
			data = data.replace("'", "") # pretty sure this is redundant 
			# you can also replace the addition symbol (i think its unnecessary. i havent tried it)
			data = data.split(" ") # splits the numbers and the addition/subtraction symbols
			realSum = 0
			imaginarySum = 0
			negative = False 
			for number in data: # number such as (10+2i) or addition/subtraction symbol +/-
				if "(" in number: # if its a number
					summ = number # i didnt want to mess with the variable number since its in the for loop
					summ = summ.replace("(", "")
					summ = summ.replace(")", "")
					summ = summ.replace("i", "")
					summ = summ.split("+") # splits the real and imaginary part of the number
					if negative == False: # when there is no subtraction symbol in front
						realSum = realSum + int(summ[0])
						imaginarySum = imaginarySum + int(summ[1])
					else: # when there is subtraction symbol in front
						realSum = realSum - int(summ[0])
						imaginarySum = imaginarySum - int(summ[1])
						negative = False # resets the negative
				elif number == "-":
					negative = True
					# negative is a variable that indicates whether there is a negative symbol in front of a number
			if imaginarySum > 0: # if the imaginary part is positive, 
				t.sendline(str(realSum) + "+" + str(imaginarySum) + "i")
			elif imaginarySum < 0: # if the imaginary part is negative
				t.sendline(str(realSum) + str(imaginarySum) + "i")
				# if you have the addition symbol, it would become 2+-3i instead of 2-3i
			# chances of it equaling 0 is very low and i dont know if it should be 10 or 10+0i
	else:
		t.sendline("") # just sends a new line (basically equal to a return/enter)
	sleep(0.05)
p.close()