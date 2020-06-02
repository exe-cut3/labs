from Crypto.Util import number


n_length = 8

primeNum1 = number.getPrime(n_length)
primeNum2 = number.getPrime(n_length)

print(primeNum1)
print(primeNum2)

n = primeNum1 * primeNum2

eiler = (primeNum1 - 1)*(primeNum2 - 1)

e = 257 
print("E: {}".format(e))

def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1


def public_key_gen():
	if is_coprime(e,eiler) == True:
		public_key = [e,n]		
	return public_key

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi


def private_key_gen():
	private_key = [multiplicative_inverse(e,eiler),n]
	return private_key


print("Public key: {}".format(public_key_gen()))
print("Private key: {}".format(private_key_gen()))


def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher


def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)



# print(type(public_key_gen()))


print("Enter text to encrypt:")
text = input()
asd = encrypt(public_key_gen(),str(text))
print("Result of the encrypt: {}".format(asd))
print("Result of the decrypt: {}".format(decrypt(private_key_gen(),asd)))


# print(result)

# b = 595
# n = 703
# m = 991


# def one_way(b,n,m):
# 	result = pow(b,n) % m
# 	return(result)

# print(one_way(b,n,m))


