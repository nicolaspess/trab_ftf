import random

result = []

#for x in range (0, 50000):
#	num = random.randint(-50000, 50000)
#	while num in result:
#		num = random.randint(-50000, 50000)
#	result.append(num)

#outra forma:

result = random.sample(xrange(5000000),100000)

f = open("input_100000", "w")

for item in result:
	f.write("%s\n" % item)

f.close()
