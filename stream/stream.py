import requests
import base64
from itertools import combinations

def main():
    email = "gcamargo221@alumnos.iua.edu.ar"  # Replace with your registered email
    response = requests.get(f"https://cripto.iua.edu.ar/stream/{email}/challenge")
    if response.status_code != 200:
        print("Failed to fetch challenge")
        return
    lines = response.text.splitlines()
    if len(lines) != 5:
        print("Unexpected number of ciphertexts")
        return
    ciphertexts = [base64.b64decode(line) for line in lines]
    length = len(ciphertexts[0])
    if any(len(ct) != length for ct in ciphertexts):
        print("Ciphertexts have different lengths")
        return
    for i, j in combinations(range(5), 2):
        cx = ciphertexts[i]
        cy = ciphertexts[j]
        xor = bytes([a ^ b for a, b in zip(cx, cy)])
        if len(set(xor)) == 1:
            x = xor[0]
            possible_ab = []
            for a in range(33, 127):
                b = a ^ x
                if 33 <= b <= 126:
                    possible_ab.append((a, b))
            for a, b in possible_ab:
                ks = bytes([c ^ a for c in cx])
                decrypted_cy = bytes([c ^ k for c, k in zip(cy, ks)])
                if all(byte == b for byte in decrypted_cy):
                    for k in range(5):
                        if k == i or k == j:
                            continue
                        cz = ciphertexts[k]
                        decrypted_cz = bytes([c ^ ksc for c, ksc in zip(cz, ks)])
                        if len(decrypted_cz) == 0:
                            continue
                        all_digits = all(48 <= c <= 57 for c in decrypted_cz)
                        if all_digits:
                            last_digit = decrypted_cz[-1]
                            if last_digit in {48, 50, 52, 54, 56}:
                                keystream_b64 = base64.b64encode(ks).decode()
                                print(f"Found keystream: {keystream_b64}")
                                response = requests.post(
                                    f"https://cripto.iua.edu.ar/stream/{email}/answer",
                                    files={'keystream': (None, keystream_b64)}
                                )
                                print(response.text)
                                return
    print("No keystream found")

if __name__ == "__main__":
    main()
