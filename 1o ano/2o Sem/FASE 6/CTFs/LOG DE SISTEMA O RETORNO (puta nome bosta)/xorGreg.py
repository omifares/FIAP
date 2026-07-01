def xor_hex(hex1, hex2):
    # Converter as strings hexadecimais para bytes
    bytes1 = bytes.fromhex(hex1)
    bytes2 = bytes.fromhex(hex2)
    
    # Repetir a segunda string para ter o mesmo comprimento da primeira
    repeated_bytes2 = bytes2 * (len(bytes1) // len(bytes2)) + bytes2[:len(bytes1) % len(bytes2)]
    
    # Fazer a operação XOR byte a byte
    result = bytes(a ^ b for a, b in zip(bytes1, repeated_bytes2))
    
    # Converter o resultado de volta para uma string hexadecimal
    result_hex = result.hex()
    
    # Converter o resultado hexadecimal de volta para ASCII
    ascii_result = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in result)
    
    return result_hex, ascii_result

# Exemplo de uso com suas strings
hex1 = "2C28223109164B431E040E3E00105B5E0E0E14120F"
hex2 = "4a61636172653230"
result_hex, ascii_result = xor_hex(hex1, hex2)
print("Resultado XOR (Hex):", result_hex)
print("Resultado XOR (ASCII):", ascii_result)