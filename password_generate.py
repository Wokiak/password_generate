import random
# symbols_list = [
# 			'@',
# 			'!',
# 			'$']
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

Letter1=chr(random.randint(65,90)) 
Letter2=chr(random.randint(65,90))
Letter3=chr(random.randint(65,90))
Letter4=chr(random.randint(65,90))
number5=chr(random.randint(48,57))
number6=chr(random.randint(48,57))
number7=chr(random.randint(48,57))
symbols1=chr(random.randint(35,38))
symbols1=chr(random.randint(35,38))

password = Letter1 + Letter2 + Letter3 + Letter4 + number5 + number6 + number7 + symbols1
password = shuffle(password)


print(password)
