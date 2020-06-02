import hashlib
import random
import string

for x in range(100000000):
	random_string = ''.join([random.choice(string.ascii_uppercase + string.digits) for n in range(5)])
	m = hashlib.md5()
	# print(random_string)
	m.update(random_string.encode())
	hash_result = m.hexdigest()
	if hash_result[0:5] == '12345':
		print('String: {}, Hash: {}'.format(random_string, hash_result))