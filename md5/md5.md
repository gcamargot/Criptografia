# MD5crypt
## Desafío
En este desafío, el servidor proporciona un texto cifrado con el algoritmo md5crypt utilizado en la biblioteca ADOdb:

```https://github.com/ADOdb/ADOdb/blob/master/session/crypt.inc.php```

El desafío es descifrarlo.

El texto claro está codificado en ASCII, y es un correo electrónico dirigido al correo electrónico declarado. Para obtener el texto cifrado, se debe hacer un requerimiento GET a una URL de la forma:

`https://cripto.iua.edu.ar/md5crypt/<email>/challenge           
dónde <email> debe ser reemplazado por una dirección de correo electrónico registrada.`

La respuesta será una secuencia de bytes codificada en base64.

## Respuesta
La respuesta debe ser enviada mediante un requerimiento POST a la URL

```https://cripto.iua.edu.ar/md5crypt/<email>/answer```
El contenido debe ser de tipo FORM, con un campo message con el mensaje descifrado. Si en vez de utilizar un requerimiento POST se utiliza un GET, se mostrará un formulario que permite subir un archivo con el mensaje descifrado.

## Ejemplo
El siguiente ejemplo muestra como conectarse con el servidor usando curl
```bash
$ curl https://cripto.iua.edu.ar/md5crypt/user@example.com/challenge
BhNUIFE8CWYDald9ATtSNAViDC9QNQNrB3wBPQZsATgBJgdkVCVTEQEnBGBSZgMiAmcGNAB1Ayk
MOAEiU1wAFAY6VDxRJwluAz5XKQF7UikFfAwqUDUDPQdyASQGZgEuASYHLlQmUz0BMwRnUmsDIA
IiBjMAaANmDCsBI1MzACMGaFQnUScJbQN9V2UBXFIOBXAMOFA6A2IHMQEkBjkBdgEUB25UJFMlA
ScEYFJgAwYCVgY/ADoDJww0ATlTMQAiBjBUPlF9CWYDP1czASJSOAV2DBpQJQNpBzEBfgZmATIB
JwcvVDdTIwFYBARSDANYAkoGFQAgA0sMHAEDUwUAEgYHVH9RGAlFAx9XCgEYUn0FVQwIUB8DQAc
AAREGTgEbARsHT1QRU3EBHgRPUksDSwJXBhEARwNCDAoBcFN1AGYGbVRoUXMJTQMZVxsBAlIVBQ
8MUFAWA04HFAEEBksBdgE7B3JUdlMwAXIEflJ3A2kCYQY5AHMDbgw2AT5TdgA6BjRUJlE7CW4DP
Vc8ASJSNAVmDDtQPAMnBz4BMQZtATEBJwdgVDFTNAFyBGdSawMsAnUGOABpA2QMMQFwUyIAPwYw
VHJRNwlqAyRXPAF2UikFfAwqUDUDdAdYASIGZgEwATcHc1R2UyUBPQQuUnQDeQJjBj4AdANuDC0
BKVN4AHcGdVQGUTsJbgNwVzkBN1IpBWQMelAkA34HIgE1BnABdgEgB2BUOFM2ATcELlJjA34CbQ
Y9ACADRAwaAXxTdgAYBgBUHFEQCU4DfFd9AQVSFQVKDA5QfAMnBzMBPgZnAVwBGAdIVBFTFgEXB
FxSJQN4Am0GcABGA04MHwEEUx4AdwZ9VDpRNgllAzNXOAF2UikFbQw/UHADaQczAT0GZgF2AT0H
Z1R2UyUBOgRrUiUDYAJjBj4AZwNyDDgBN1MzAH4GeVRyUR8JQgMEVxgBBFJxBSUMF1ARA0AHHAE
FBk4BdgEzB29UMlNbARAEQlJKA1gCVgYfAC4DJwx5ARNTOQA6BjhUM1E9CW8DI1d9ASRSOAVjDD
9QIgMnByYBPwYjAT8BPAdmVCRTNAE2BGdSYANiAnYGIwAgA3QMLAEzUz4AdwY0VCFRcwlIAxhXH
AEUUhEFTAwJUHwDJwcRARgGQgEEARYHTlQYUx8BEwRXUikDBgJBBhEAQgNCDAsBHlMTAAMGeVRy
URQJQgMeV3EBdlILBUAMCFAdA0gHBwEEBksBegFyB1dUGVMVARkET1IpAywCUQYTAE8DUwwaARh
TegB3BjRUPFE3CSsDB1cVARdSCQVADAxQFQNVBwEBEQZRARkBBwdPVBJTfwFYBARSUQNkAmcGcA
BtA2YMNwEpU3YAIQYwVCBRIAliAz9XMwElUn0Fagw8UHADcwc6ATUGIwEQARsHR1QCUxkBcgRiU
mQDYgJlBiUAYQNgDDwBcFMkADIGM1Q+UTYJaAMkV30BIlI1BWAMelAjA2gHIgE4BmoBJQEmB2hU
NVMwASYEZ1JqA2ICIgYxAG4DYwxTATZTPwA5BjRUPFEwCWIDMVcxAXZSLgVxDDtQJANyByEBcAZ
sATABcgdoVCJTIgFyBHtSdgNpAnAGIwAuAycMeQETUzkAOgY4VDNRPQlvAyNXfQE/UjMFJQwuUD
gDYgdyARUGTwEfAQYHRFR2UzUBOwRvUmkDaQJhBiQAIANuDDcBM1M6ACIGMVQ3UVkJXQMDVxIBB
lJ9BWQMNFA0AycHHgERBkUBHwEGB0RUelNxASUEZlJsA2ACZwZwAGMDaAw0AT1TNwA5BjFUIVFz
CWIDPld9ASJSNQVgDHpQFwNSBwYBBAZGAQQBcgdlVD9TMAE+BGtSZgN4AiIGOQBuA2QMNQElUzI
AMgZ1VBpRHAlEAwRXHgEeUlcFZAw0UDQDJwcAARkGUwEGAR4HRFR4U3EBBgRmUmADLAJuBjEAdA
NzDDwBIlN2AD4GJlRyUTIJKwM2VzwBIFIyBXcMM1AkA2IHcgE/BmUBdgE0B3NUI1MiASYEfFJkA
3gCZwY0ACADQQwWAQJTAgAfBnVUIlEhCWQDN1cvATdSMAVoDD9QIgN0B1gBJwZrATkBcgdkVDhT
NQFyBHtSdQMsAncGIwBpA2kMPgFwUyIAPwY8VCFRcwlnAzFXMwExUigFZAw9UDUDKQdY
```
Si el resultado de descifrar el mensaje se encuentra en el archivo message.txt, se puede enviar al servidor con el siguiente comando:
```bash
$ curl -F message=@message.txt https://cripto.iua.edu.ar/md5crypt/user@example.com/answer
¡Ganaste!
```
### El algoritmo
La función utilizada para cifrar corresponde al código siguiente:
```php
La función Encrypt()
function Encrypt($txt,$key)
{
  $encrypt_key = md5(rand(0,32000));
  $ctr=0;
  $tmp = "";
  for ($i=0;$i<strlen($txt);$i++)
  {
     if ($ctr==strlen($encrypt_key)) $ctr=0;
     $tmp.= substr($encrypt_key,$ctr,1) . (substr($txt,$i,1) ^ substr($encrypt_key,$ctr,1));
     $ctr++;
  }
  return base64_encode($this->keyED($tmp,$key));
}
```

```
La función recibe dos argumentos de tipo string: el texto claro $txt y la clave $key, y realiza los siguientes pasos:

Calcula una $encrypt_key como el resultado de aplicar la función md5 sobre la representación decimal de un número entre 0 y 32000 (inclusive).
Inicializa un contador $ctr en 0, y una variable $tmp con la cadena vacía.
Para cada $i entre 0 y la longitud del texto claro:
Si el contador es igual a la longitud de $encrypt_key, lo manda a cero.
Concatena a $tmp el carácter de la clave que está en la posición $ctr, y el resultado de realizar un or-exlusivo entre ese carácter y el carácter del texto claro que está en la posición $i.
Incrementa el contador.
Invoca la función keyED() con $tmp y $key como argumentos
Devuelve el valor de retorno de keyED() codificado en base64
Observaciones
La función md5 devuelve la representación hexadecimal del hash, es decir, una cadena de 32 caracteres del conjunto {0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f}
Por lo tanto la longitud de $encrypt_key es siempre 32.
El or exclusivo entre caracteres se realiza entre los códigos ASCII correspondientes. Por ejemplo
    'A' ^ 'b' = 65 ^ 98 = 35 = '#'
La longitud del texto cifrado (antes de codificarlo en base64) es siempre el doble que la longitud del texto claro.
```
### La función keyED()
```php
function keyED($txt,$encrypt_key)
{
  $encrypt_key = md5($encrypt_key);
  $ctr=0;
  $tmp = "";
  for ($i=0;$i<strlen($txt);$i++){
    if ($ctr==strlen($encrypt_key)) $ctr=0;
    $tmp.= substr($txt,$i,1) ^ substr($encrypt_key,$ctr,1);
    $ctr++;
  }
  return $tmp;
}
```
```
La función recibe dos argumentos de tipo string: el texto claro $txt y la clave $encrypt_key, y realiza los siguientes pasos:

Transforma $encrypt_key aplicando la función md5.
Inicializa un contador $ctr en 0, y una variable $tmp con la cadena vacía.
Para cada $i entre 0 y la longitud del texto claro:
Si el contador es igual a la longitud de $encrypt_key, lo manda a cero.
Concatena a $tmp el resultado de realizar un or-exlusivo entre el carácter de la clave que está en la posición $ctr y el carácter del texto claro que está en la posición $i.
Incrementa el contador.
Devuelve $tmp
Observaciones
El argumento $encrypt_key es el argumento $key de la función Encrypt(), es decir, la clave provista por el usuario.
Esa clave se procesa con md5, por lo que se transforma en una cadena de 32 dígitos hexadecimales.
Análisis
El algoritmo equivale a aplicar el cifrado de Vigenère dos veces, con claves de 32 caracteres compuestas por dígitos hexadecimales.

En la primera aplicación, la aplicación interna, se utiliza una clave aleatoria, y se produce un nuevo texto que consiste en preceder cada carácter del texto cifrado por el carácter correspondiente de la clave.

En la segunda aplicación, la aplicación externa, se utiliza la clave elegida por el usuario, previamente procesada por md5.
```

#### Este esquema tiene un número de problemas.

1. El espacio de claves interno es muy pequeño. Hay solamente 32001 claves posible, lo cual hace perfectamente posible un ataque de fuerza bruta.
2. Los posibles valores de los bytes de las claves no están distribuidos de manera uniforme, sino que hay 16 valores posibles, los que corresponden a dígitos hexadecimales.
3. La clave interna se puede eliminar fácilmente, haciendo un or-exclusivo de los caracteres pares con los impares. De esta forma obtenemos un nuevo texto cifrado, que resulta de aplicar un cifrado de Vigenère con una clave de 16 caracteres.
4. Los valores de esa clave (desconocida) de 16 caracteres, tampoco tienen distribución uniforme, sino que se corresponden al or-exclusivo de dos dígitos hexadecimales.
5. Si no se conoce nada del texto claro, se puede resolver como un Vigenère con longitud de clave conocida.
6. Si se conoce parte del texto claro, basta con hacer el xor del texto claro conocido con la porción adecuada del texto cifrado para recuperar esa parte de la clave.