import pyaes
file_name= "ctfoto.pyransom"
file= open(file_name, "rb")
file_data= file.read()
file.close()
key= f"0143256879fravtr"
aes= pyaes.AESModeOfOperationCTR(key)
decrypt_data= aes.decrypt(file_data)
new_file_name= "ctfoto.png"
new_file= open(new_file_name, "wb")
new_file.write(decrypt_data)
new_file.close()
