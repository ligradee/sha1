import random
import sha1


def preimage(Y0, n):
    string = "qwertyuiop[]asdfghjkl;'zxcvbnm,./1234567890-"
    Y=[]
    Y.append(0)
    step1 = 0
    i = 0 
    while  Y[i] != Y0:
        i+=1
        new_word = ""
        for j in range(random.randint(10,50)):
            new_word += random.choice(string)
        hash_add = (sha1.sha1(new_word))
        hash_bin = ' '.join(format(ord(x), 'b') for x in hash_add)

        if n == 8:
        	Y.append(hash_bin[:9])
        if n == 12:
        	Y.append(hash_bin[:13])
        if n == 16:
        	Y.append(hash_bin[:17])
        if n == 20:
        	Y.append(hash_bin[:21])
        if n == 24:
        	Y.append(hash_bin[:25])
        if (Y[i] == Y0):
            step1 = i
            break
        
    return step1

def collision(n):
	string = "qwertyuiop[]asdfghjkl;'zxcvbnm,./1234567890-"
	Y=[]
	step1 = 0

	for i in range(300):
		new_word = ""
		for j in range(random.randint(10,50)):
			new_word += random.choice(string)
		hash_add = (sha1.sha1(new_word))
		hash_bin = ' '.join(format(ord(x), 'b') for x in hash_add)

		if n == 8:
			if  hash_bin[:9] in Y:
				step1 = i
				return step1

			Y.append(hash_bin[:9])

		if n == 12:
			if  hash_bin[:13] in Y:
				step1 = i
				return step1

			Y.append(hash_bin[:13])

		if n == 16:
			if  hash_bin[:17] in Y:
				step1 = i
				return step1

			Y.append(hash_bin[:17])

		if n == 20:
			if  hash_bin[:21] in Y:
				step1 = i
				return step1
			Y.append(hash_bin[:21])

		if n == 24:
	
			if  hash_bin[:25] in Y:
				step1 = i
				return step1
			Y.append(hash_bin[:25])


password = "meow"
hash = (sha1.sha1(password))
Y0=' '.join(format(ord(x), 'b') for x in hash)
Y0 = Y0[:9]
out = ' '.join(format(ord(x), 'b') for x in hash)


#8 bit
sum_preimage = 0
sum_collision = 0

for i in range(1000):
    sum_preimage = sum_preimage + preimage(Y0, 8)
    sum_collision += collision(8)

complexity_preimage = sum_preimage // 1000
complexity_collision = sum_collision // 1000
print("Difficulty of finding the second preimage 8 bit= ", complexity_preimage)
print("Difficulty of finding collisions 8 bit = ", complexity_collision)

#12 bit
Y0 = out[:13]
sum_preimage = 0
sum_collision = 0


for i in range(1000):
    sum_preimage = sum_preimage + preimage(Y0, 12)
    sum_collision += collision(12)

complexity_preimage = sum_preimage // 1000
complexity_collision = sum_collision // 1000
print("Difficulty of finding the second preimage 12 bit = ", complexity_preimage)
print("Difficulty of finding collisions 12 bit  = ", complexity_collision)


#16 bit
Y0 =out[:17]
sum_preimage = 0
sum_collision = 0

for i in range(1000):
    sum_preimage = sum_preimage + preimage(Y0, 16)
    sum_collision += collision(16)

complexity_preimage = sum_preimage // 1000
complexity_collision = sum_collision // 1000
print("Difficulty of finding the second preimage 16 bit = ", complexity_preimage)
print("Difficulty of finding collisions 16 bit = ", complexity_collision)

#20 bit
Y0 =out[:21]
sum_preimage = 0
sum_collision = 0

for i in range(300):
    sum_preimage = sum_preimage + preimage(Y0, 20)
    sum_collision = sum_collision + collision(20)

complexity_preimage = sum_preimage // 300
complexity_collision = sum_collision // 300
print("Difficulty of finding the second preimage 20 bit = ", complexity_preimage)
print("Difficulty of finding collisions 20 bit = ", complexity_collision)

#24 bit
Y0 =out[:25]
sum_preimage = 0
sum_collision = 0

for i in range(100):
    sum_preimage = sum_preimage + preimage(Y0, 24)
    sum_collision += collision(24)

complexity_preimage = sum_preimage // 100
complexity_collision = sum_collision // 100
print("Difficulty of finding the second preimage 24 bit = ", complexity_preimage)
print("Difficulty of finding collisions 24 bit = ", complexity_collision)

