import requests
from base64 import b64decode

# Configuración
email = "gcamargo221@alumnos.iua.edu.ar"
challenge_url = f"https://cripto.iua.edu.ar/md5crypt/{email}/challenge"
answer_url = f"https://cripto.iua.edu.ar/md5crypt/{email}/answer"

# 1. Obtener texto cifrado
print("[DEBUG] Solicitando texto cifrado al servidor...")
response = requests.get(challenge_url)
print(f"[DEBUG] Código de respuesta HTTP: {response.status_code}")

if response.status_code != 200:
    print(f"[ERROR] Falló la solicitud. Código: {response.status_code}")
    exit()

try:
    ciphertext = b64decode(response.text)
    print(f"[DEBUG] Texto cifrado decodificado. Longitud: {len(ciphertext)} bytes")
except Exception as e:
    print(f"[ERROR] Error decodificando base64: {str(e)}")
    exit()

# 2. Generar C' (eliminar clave interna)
print("[DEBUG] Generando texto cifrado reducido C'...")
c_prime = bytearray()
for i in range(0, len(ciphertext), 2):
    if i + 1 >= len(ciphertext):
        print(f"[WARN] Byte impar omitido en posición {i}")
        break
    c_prime.append(ciphertext[i] ^ ciphertext[i+1])

print(f"[DEBUG] Longitud de C': {len(c_prime)} bytes")

# 3. Buscar la clave K usando texto conocido
known_plaintext = email.encode('ascii')
print(f"Known plaintext: {known_plaintext} vs {email}" )
print(f"[DEBUG] Texto conocido: {known_plaintext.decode()}")
print(f"[DEBUG] Buscando clave en {len(c_prime) - len(known_plaintext)} posiciones...")

found = False
for i in range(len(c_prime) - len(known_plaintext) + 1):
    # 4. Calcular clave candidata
    candidate_key = bytearray()
    for j in range(len(known_plaintext)):
        if i + j >= len(c_prime):
            break
        candidate_key.append(c_prime[i + j] ^ known_plaintext[j])
    
    # 5. Verificar periodicidad de 16 bytes
    key_length = 16
    valid = True
    for k in range(len(candidate_key)):
        if candidate_key[k] != candidate_key[k % key_length]:
            valid = False
            break
    
    if valid:
        print(f"[DEBUG] Clave candidata encontrada en posición {i}: {candidate_key[:key_length].hex()}")
        # 6. Descifrar todo C' con la clave
        full_key = candidate_key[:key_length]
        decrypted = bytearray()
        for k in range(len(c_prime)):
            decrypted.append(c_prime[k] ^ full_key[k % key_length])
        
        # Verificar presencia del texto conocido
        if known_plaintext in decrypted:
            print("[DEBUG] ¡Texto conocido encontrado en el mensaje descifrado!")
            try:
                with open("message.txt", "wb") as f:
                    f.write(decrypted)
                print("[DEBUG] Archivo message.txt creado correctamente")
                
                # 7. Enviar respuesta al servidor
                print("[DEBUG] Enviando solución al servidor...")
                files = {"message": open("message.txt", "rb")}
                response = requests.post(answer_url, files=files)
                print(f"[DEBUG] Respuesta del servidor: {response.text}")
                
                found = True
                break
            except Exception as e:
                print(f"[ERROR] Error al enviar: {str(e)}")
                exit()
    if found:
        break

if not found:
    print("[ERROR] No se encontró una clave válida. Posibles causas:")
    print("- El texto conocido no está en el mensaje")
    print("- La clave no tiene periodicidad de 16 bytes")
    print("- Error en el cálculo de C'")