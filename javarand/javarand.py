import requests

MULTIPLICADOR = 25214903917

def check_sign(value):
    if(value & (1<<31)):
        value -= 1 << 32
    return value

server = "https://cripto.iua.edu.ar"

email = "gcamargo221@alumnos.iua.edu.ar"

response = requests.get(f"{server}/javarand/{email}/challenge")

number1 = int(response.text)

print(number1)

response = requests.get(f"{server}/javarand/{email}/challenge")

number2 = int(response.text)
print(number2)

for i in range(2**16):
    temp = number1 * 2**16 + i
    seed = (temp  * MULTIPLICADOR + 11) % 2**48 
    guess = check_sign(seed >> 16)
    
    if(guess == number2):
        break

next_value = (seed * MULTIPLICADOR + 11 ) % 2**48
next_value >>= 16

response = requests.post(
    f"{server}/javarand/{email}/answer",
    files = {"number": str(check_sign(next_value)).encode('ascii')}
)

print(f"Status code: { response.status_code}")
print(response.text)


