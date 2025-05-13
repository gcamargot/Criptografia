import requests
from base64 import b64decode

email = "gcamargo221@alumnos.iua.edu.ar"
challenge_url = f"https://cripto.iua.edu.ar/md5crypt/{email}/challenge"
answer_url = f"https://cripto.iua.edu.ar/md5crypt/{email}/answer"

response = requests.get(challenge_url)

if response.status_code != 200:
    exit()

try:
    ciphertext = b64decode(response.text)
except Exception as e:
    print(f"[ERROR] Error decodificando base64: {str(e)}")
    exit()

# 2. Generar C' (eliminar clave interna)
c_prime = bytearray()
for i in range(0, len(ciphertext), 2):
    if i + 1 >= len(ciphertext):
        print(f"[WARN] Byte impar omitido en posición {i}")
        break
    c_prime.append(ciphertext[i] ^ ciphertext[i+1])

known_plaintext = email.encode('ascii')
print(f"Known plaintext: {known_plaintext} vs {email}" )

found = False
for i in range(len(c_prime) - len(known_plaintext) + 1):
    candidate_key = bytearray()
    for j in range(len(known_plaintext)):
        if i + j >= len(c_prime):
            break
        candidate_key.append(c_prime[i + j] ^ known_plaintext[j])
    
    key_length = 16
    valid = True
    for k in range(len(candidate_key)):
        if candidate_key[k] != candidate_key[k % key_length]:
            valid = False
            break
    
    if valid:
        full_key = candidate_key[:key_length]
        decrypted = bytearray()
        for k in range(len(c_prime)):
            decrypted.append(c_prime[k] ^ full_key[k % key_length])
        
        if known_plaintext in decrypted:
            try:
                with open("message.txt", "wb") as f:
                    f.write(decrypted)
                
                # 7. Enviar respuesta al servidor
                files = {"message": open("message.txt", "rb")}
                response = requests.post(answer_url, files=files)
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
