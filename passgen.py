import random
import string

print('Strong Random Password Generator')

#input the type and total length for password
type_length = 4
total_length = 8

#define data types
upper = string.ascii_uppercase
num = string.digits

#combine the data
#all = upper + num

#use random
temp1 = random.sample(upper,type_length)
temp2 = random.sample(num,type_length)

#create the password
password = "".join(random.sample(temp1+temp2,total_length))

#print the password
print(password)

