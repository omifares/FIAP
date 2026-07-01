from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Caso a string seja Base64:
ciphertext_b64 = "?A_@g*aK(auXntU4It^dkD!"

try:
    ciphertext = base64.b64decode(ciphertext_b64)
except Exception:
    ciphertext = ciphertext_b64.encode()  # fallback: ASCII bytes

    # Chave (tem que ter 16, 24 ou 32 bytes)
    key = b"FIAPandr0_h4ck!!"  # ajuste o tamanho e valor da chave aqui

    # IV (16 bytes) — se não souber, tenta zero ou parte da chave
    iv = b"\x00" * 16

    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
        print("FLAG POSSÍVEL:", plaintext.decode())
    except Exception as e:
        print("Erro na descriptografia:", e)
