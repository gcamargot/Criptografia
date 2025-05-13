# Clave generada a partir de la fecha y hora
## Desafío
El desafío consiste en descifrar un mensaje cifrado con una clave generada a partir de la fecha y hora de creación del mensaje.

Para obtener el mensaje a descifrar se debe hacer un requerimiento GET a una URL de la forma:

https://cripto.iua.edu.ar/timerand/{email}/challenge
donde {email} debe ser reemplazado por una dirección de correo electrónico registrada.

El resultado será similar al siguiente:
```
From: mmontes@iua.edu.ar
Date: Sat Jan 29 19:15:45 UTC 2022
To: user@example.com

cJLPK7rt3EegpxZre4e7Sw2kncbwo2FuPjyiVn/cOLZ5wvZ3znoudW
YVGrVuWxP95Uc9aib0dUNMSBy+bJrdzFBqwb9M/6c9Z/7sy8RRcBOM
QH+5qAstqLqOAHeCwEFEiYUJt6q3++3RvHjRGkgA2Xu2LBdjr/B3sX
DmaFNF2QohmgzmrkyTxC3lH8rSN314I0qgDQWcDr0vSerrKWBFIMXh
0aezn9f+OHNjYOHBtCG0Pw/nnQLrjmFWLBo1AQ0we4oObutsWMak1O
+74GvBpOYLeNvIh8hL+uEEuFixxF8aTMUTsnZ13WxeZI2LH5ySf6QV
SFUDRWIKWryyv46KQZEFLidhoPR02blDMlty21TQc9spcl4Y2V5rKj
jsRosPzXDJr2qSSVoL7PVPoMB7WiS1rwzhgcPxFVk2aEF9YsMD1lfF
6azSNhEIfu028QYnuONG/Xof9Ni2+2coODD8CXSh7djCtw5Jex5HNu
RMY/9qWfk7u4RdR11kZhhUGfVH4r4Z5h5pAJHj8khZxlZ9AyFapO6F
Q6erUDIc4WEq6ns=
```
En el encabezado, además del emisor y el destinatario, aparece la hora de creación del mensaje. El cuerpo contiene una secuencia de bytes codificada en base64.

Los primeros 128 bytes de esa cadena contienen una clave simétrica que ha sido cifrada con RSA de 1024 bits.

El resto de la cadena, es el mensaje cifrado con AES-128 en modo CBC, utilizando relleno PKCS7, y con el IV colocado como primer bloque:



La clave simétrica ha sido generada mediante la aplicación del algoritmo MD5 a la hora de creación del mensaje, expresada como el tiempo Unix expresado en microsegundos (es decir, la cantidad de microsegundos segundos transcurridos desde las cero horas del 1 de enero de 1970 UTC). Como MD5 procesa secuencias de bytes, el número de microsegundos ha sido convertido en 8 bytes, utilizando la convención big endian.

El mensaje está compuesto únicamente por caracteres ASCII.

Es necesario observar que la fecha y hora que figuran en el mensaje se encuentran expresadas con una precisión de segundos, no de microsegundos, por lo que existen 1.000.000 de claves posibles asociadas con ella.

## Respuesta
La respuesta debe ser enviada mediante un requerimiento POST a la URL

https://cripto.iua.edu.ar/timerand/{email}/answer
El contenido debe ser de tipo FORM, con un campo message con el texto claro del mensaje.

## Ejemplo
El siguiente ejemplo muestra como obtener el desafío usando curl
```bash
$ curl https://cripto.iua.edu.ar/timerand/user@example.com/challenge
From: mmontes@iua.edu.ar
Date: Sat Jan 29 19:15:45 UTC 2022
To: user@example.com

aE8ZtSiJbv+A49oUQXpNdQ+BAbjtjOz4NQbm+JUxtGJpb6cfxbOBVN
0qMmapZDJfp9gqQwaSL4LnAkw1Dv0KFI2ANGMSM8TALDgfxdRoJvVC
zbfHLCmHYALN+3evQRdBtTaBuhDZyvAcH3zHLIkWMzalOWIFSoMLEE
4yaGIh0EbRnF+rt5OpFWcvEFBok7pEsTmL7ym2NGZa7P+QijGAVBuZ
MBj6YYtrB9vXsaR06b8dtIUgNJhzaWtiNvzV7iGQQoUG+HHXywjWTB
nROwG3Zz5/S/UUzwJ0h4lddHjVaH45tTMITGKgCwf+57JB5gmgti0J
YICQHjpX6Hh1ARtzUHVmzwSD7vl2skNBUhFbkRwvmlwJ2z51dA6dt0
ZXF2rO4weWD3e2GddqIvB9cwXmf2NOwveeAxkj/UsoDgNXuIesyR4P
P9hjkwt7TdlXMiOAr/Zb1LtyZQAy7nBG3Kh7wJV7BSXggmfOXLmB5Y
2uKMVC/SeuZCO0t0gNGFJIEfJRUhmVMsm7gybMbrFmI5wIqfObL0fS
Z3595wsoYqO4zUo=
```

Si la respuesta está en un archivo llamado message.txt puede enviarse de la siguiente forma:
```bash
$ curl -F message=@message.txt https://cripto.iua.edu.ar/timerand/user@example.com/answer
¡Ganaste!
$ cat message.txt
Brisk talkers are usually slow thinkers.  There is, indeed, no wild beast
more to be dreaded than a communicative man having nothing to communicate.
If you are civil to the voluble, they will abuse your patience; if
brusque, your character.
        -- Jonathan Swift
```
### Endianess
El término endianess hace referencia al orden de los bytes en la representación de un entero en una determinada arquitectura computacional. Los órdenes más comunes son big endian, en el cual el byte más significativo está en la posición más baja de memoria, y little endian, en el cual el byte más significativo está en la posición más alta de la memoria.

Veamos un ejemplo en Python:
```python
i = 1
# El método `to_bytes` convierte un entero en una secuencia de bytes 
# de una determinada longitud y endianess
big_endian = i.to_bytes(8,"big")
little_endian = i.to_bytes(8, "little")
print(f"Big endian:    {big_endian}")
print(f"Little endian: {little_endian}")
```
Big endian:    b'\x00\x00\x00\x00\x00\x00\x00\x01'
Little endian: b'\x01\x00\x00\x00\x00\x00\x00\x00'
La arquitectura Intel utiliza la convención little endian, al igual que el protocolo SMB. En el conjunto de protocolos de Internet se utiliza lo que se conoce como network order, que es big endian. La máquina virtual Java también utiliza big endian.

La especificación de la endianess es muy importante en protocolos y algoritmos criptográficos. Por ejemplo el algoritmo de hash MD5 utiliza la convención little endian, mientras que SHA-2 utiliza big endian.

Muchos lenguajes de programación proveen funciones de biblioteca que permiten convertir enteros en un arreglo de bytes y viceversa y especificar la endianess deseada, como vimos en el ejemplo de Python más arriba. Si no, no es complejo escribir una función utilizando operaciones sobre bits. Por ejemplo, el siguiente código java convierte un long en un array de bytes, utilizando la convención big endian.
```python
public static byte[] longToBytes(long value) {
    byte[] result = new byte[Long.BYTES];
    for (int i = Long.BYTES - 1; i >= 0; i--) {
        result[i] = (byte)(value & 0xFF);
        value >>= Byte.SIZE;
    }
    return result;
}
```
### MD5
MD5 es una función de hash diseñada por Ron Rivest1. Procesa secuencias de bytes de longitud arbitraria y produce una salida de 128 bits (16 bytes). El siguiente es un ejemplo de la invocación de MD5 utilizando el lenguaje Python:
```python
from hashlib import md5

# El mensaje es una secuencia de bytes, no una string
message = b'Este es el mensaje' 
h = md5(message)
print(f"md5({message}) = {h.digest()}")
# En este caso no nos interesa la representación hexadecimal.
print(f"Esta es la representación hexadecimal: {h.hexdigest()}")
```
md5(b'Este es el mensaje') = b'^6\xb9\x9aRF\xb0\xb4K#\xbe(?\x91(\xd5'
Esta es la representación hexadecimal: 5e36b99a5246b0b44b23be283f9128d5
### AES-128-CBC
El algoritmo utilizado para cifrar el mensaje es AES, con clave de 128 bits, y en el modo de operación CBC.

Este modo requiere la utilización de un IV (initialization vector). El IV es un bloque de 128 bits (el tamaño de bloque de AES), con un valor que no requiere ser secreto pero no debe ser predecible por el adversario. En este caso, el IV se ha colocado como primer bloque del mensaje.

CBC también requiere la utilización de un mecanismo de relleno (padding) para que el mensaje tenga una longitud que sea múltiplo del tamaño del bloque. En este caso se utilizó el estándar PKCS7.

### Ejemplos de código
Los siguientes ejemplos muestran posibles implementaciones del desafío, aunque el comportamiento no es idéntico al utilizado en el servidor. En particular, el mecanismo de selección del IV es diferente. Por simplicidad, en los ejemplos se genera el IV con un mecanismo similar al utilizado para la generación de la clave. En el servidor el mecanismo es distinto, y el IV es realmente aleatorio.

#### Python
El siguiente código Python es análogo al que se usó para generar el desafío:
```python
import time
import base64
from hashlib import md5
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asymmetric_padding
from cryptography.hazmat.primitives import serialization, hashes, padding as symmetric_padding
from cryptography.hazmat.backends import default_backend  

def generate_challenge(message, public_key):
    # Obtenemos el tiempo en microsegundos
    now = int(time.time()*1000000)
    # Este es un mal mecanismo para generar una clave
    key_seed = now.to_bytes(8,"big")
    key = md5(key_seed).digest()
    # Este es un mal mecanismo para generar un IV
    iv_seed = (now+1).to_bytes(8,"big")
    iv = md5(iv_seed).digest()
    # Ciframos el mensaje con AES-128 usando la clave `key`
    # Obtenemos una instancia del cifrador
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    # Usamos PKCS7 como mecanismo de relleno
    padder = symmetric_padding.PKCS7(128).padder()
    padded = padder.update(message) + padder.finalize()
    # Ciframos
    ciphertext = encryptor.update(padded) + encryptor.finalize()
    # Ciframos la clave secreta con la clave pública del destinatario
    encrypted_key = public_key.encrypt(
        key,
        asymmetric_padding.OAEP(
            mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    assert(len(encrypted_key) == 128)
    # El desafío está compuesto por la clave cifrada, el iv y el texto cifrado
    return base64.b64encode(encrypted_key + iv + ciphertext)

# Clave pública serializada
pem = b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDIgCvlphhRoOt39+rBUxdqrivb\nxVdYmlGXkT/5mO6/fwYzA/yXeg1aKEIj1f1l1yXWecN0iYrDUflwyN5aMj6nH+zW\nYfMOVhp2seFya10vXA24UX5o5Ei7JLcnf1ubO3VfH4Fttcvvy27Qmkii3uedOTFi\nZtZn/U1dhm1rYhtrPwIDAQAB\n-----END PUBLIC KEY-----\n'
message = b"Este es el texto claro del mensaje"
# Deserializamos la clave pública
public_key = serialization.load_pem_public_key(pem)

generate_challenge(message, public_key)
```