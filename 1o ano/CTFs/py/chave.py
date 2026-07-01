import hashlib,binascii
nome = input('Insira a chave: ')
hash = hashlib.new('md5', nome.encode('utf-8')).digest()
print("O hash gerado é: ", binascii.hexlify(hash))