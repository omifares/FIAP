import binascii
import base64
import re

def decode_possible_encoding(data):
    try:
        # Tentar decodificar base64
        decoded = base64.b64decode(data)
        if b'FIAP{' in decoded or b'VOL4TiliTy' in decoded:
            return f"Base64 decoded: {decoded}"
    except:
        pass
    
    try:
        # Tentar decodificar hex
        decoded = binascii.unhexlify(data.strip())
        if b'FIAP{' in decoded or b'VOL4TiliTy' in decoded:
            return f"Hex decoded: {decoded}"
    except:
        pass
    
    return None

def scan_memory_file(filename):
    print(f"Analisando arquivo: {filename}")
    
    # Padrões para procurar (em bytes)
    patterns = [
        b"FIAP{",
        b"CTF{",
        b"FLAG{",
        b"Vol4tility",
        b"VOL4TiliTy",
        b"Volatility",
        b"FTK",
        b"Imager",
        b"flag",
        b"ctf"
    ]
    
    # Padrões regex para possíveis codificações
    hex_pattern = re.compile(b'[0-9a-fA-F]{24,}')  # Sequências hex longas
    base64_pattern = re.compile(b'[A-Za-z0-9+/]{20,}={0,2}')  # Padrão base64
    
    chunk_size = 1024 * 1024  # 1MB chunks
    overlap = 100  # Sobreposição entre chunks
    
    print("\nProcurando por padrões conhecidos e dados codificados...")
    with open(filename, 'rb') as f:
        position = 0
        while True:
            if position > 0:
                f.seek(position - overlap)
            
            chunk = f.read(chunk_size)
            if not chunk:
                break
            
            # Procurar por padrões diretos
            for pattern in patterns:
                matches = [m.start() for m in re.finditer(pattern, chunk)]
                for start_idx in matches:
                    context_start = max(0, start_idx-100)
                    context_end = min(len(chunk), start_idx+200)
                    context = chunk[context_start:context_end]
                    print(f"\nEncontrado padrão '{pattern}' no offset {position + start_idx}")
                    print(f"Contexto: {context}")
            
            # Procurar por possíveis dados codificados
            for hex_match in hex_pattern.finditer(chunk):
                decoded = decode_possible_encoding(hex_match.group())
                if decoded:
                    print(f"\nEncontrado possível dado codificado no offset {position + hex_match.start()}")
                    print(decoded)
            
            for b64_match in base64_pattern.finditer(chunk):
                decoded = decode_possible_encoding(b64_match.group())
                if decoded:
                    print(f"\nEncontrado possível dado codificado no offset {position + b64_match.start()}")
                    print(decoded)
            
            position += chunk_size - overlap
            
            if position % (10 * chunk_size) < chunk_size:
                print(f"Progresso: analisados aproximadamente {position // (1024*1024)}MB")
    
    print("\nAnálise concluída!")

if __name__ == "__main__":
    try:
        scan_memory_file("pid-1124.dmp")
    except Exception as e:
        print(f"Erro ao analisar arquivo: {str(e)}")
