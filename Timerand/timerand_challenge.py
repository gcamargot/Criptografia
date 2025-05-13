import base64
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from datetime import datetime
from email.utils import parsedate_to_datetime
from hashlib import md5

email = "gcamargo221@alumnos.iua.edu.ar"
challenge_url = f"https://cripto.iua.edu.ar/timerand/{email}/challenge"
answer_url = f"https://cripto.iua.edu.ar/timerand/{email}/answer"

response = requests.get(challenge_url)
if response.status_code != 200:
    print("Error al obtener el desafío")
    exit()

parts = response.text.split('\n\n', 1)
headers = parts[0]
body_b64 = parts[1].replace('\n', '')

date_line = next(line for line in headers.split('\n') if line.startswith('Date: '))
date_str = date_line[len('Date: '):]
dt = parsedate_to_datetime(date_str)
timestamp_seconds = int(dt.timestamp())

data = base64.b64decode(body_b64)
encrypted_key_rsa = data[:128]
aes_data = data[128:]
iv = aes_data[:16]
ciphertext = aes_data[16:]

found = False
plaintext = None
for us in range(1000000):
    full_time = timestamp_seconds * 1000000 + us
    time_bytes = full_time.to_bytes(8, 'big')
    key = md5(time_bytes).digest()

    try:
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        padded_plaintext = cipher.decrypt(ciphertext)
        unpadded = unpad(padded_plaintext, AES.block_size)

        if all(byte <= 127 for byte in unpadded):
            plaintext = unpadded.decode('ascii')
            found = True
            break
    except (ValueError, KeyError):
        continue

if not found:
    print("No se encontró el texto claro.")
    exit()

files = {'message': ('message.txt', plaintext)}
response = requests.post(answer_url, files=files)
print(response.text)
