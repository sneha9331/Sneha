import math
key = input("Enter the key:")
plain_text = input("Enter the Plain text:")

len_key = len(key)
len_plain = len(plain_text)
row = math.ceil(len_plain/len_key)
matrix = [['X']*len_key for _ in range(row)]

t = 0
for r in range(row):
    for c in range(len_key):
        if t < len_plain:
            matrix[r][c] = plain_text[t]
            t +=1
            
sorted_key = sorted([ch,i] for i,ch in enumerate(key))

cipher_text = ''
for _,c in sorted_key:
    for r in range(row):
        cipher_text += matrix[r][c]
        
print("---Encryption---")
print("Plain Text:",plain_text)
print("Cipher Text:",cipher_text)

def decrypt(cipher_text,key):
    cols = len(key)
    rows = math.ceil(len(cipher_text)/cols)
    matrix = [['X']*cols for _ in range(rows)]
    key_order = sorted(range(len(key)),key = lambda k : key[k])
    
    t = 0
    for c in key_order:
        for r in range(rows) :
            if t < len(cipher_text):
                matrix[r][c] = cipher_text[t]
                t +=1 
    decrypt_text = ''.join(matrix[r][c] for r in range(rows) for c in range(cols)).replace('X','')
    return decrypt_text
    
print("--Decryption--")
print("Decrypted text:",decrypt(cipher_text,key))