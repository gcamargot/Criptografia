# Generador de números aleatorios de Java
## Desafío
El desafío consiste en adivinar el siguiente número de 32 bits a ser producido por un generador de números pseudoaleatorios compatibles con el utilizado en Java.

Para obtener un número producido por el generador se debe hacer un requerimiento GET a una URL de la forma:

https://cripto.iua.edu.ar/javarand/{email}/challenge
donde *{email}* debe ser reemplazado por una dirección de correo electrónico registrada.

El resultado será un número entero de 32 bits, con signo, expresado como valor decimal.

## Respuesta
La respuesta debe ser enviada mediante un requerimiento POST a la URL

https://cripto.iua.edu.ar/javarand/{email}/answer
El contenido debe ser de tipo FORM, con un campo number con el número correspondiente expresado como valor decimal.

## Ejemplo
El siguiente ejemplo muestra como obtener el desafío usando curl
```bash
$ curl https://cripto.iua.edu.ar/javarand/user@example.com/challenge
385117081
```
O usando Python:
```python
server = "https://cripto.iua.edu.ar"

email = "test.user@example.com"

import requests
response =  requests.get(f"{server}/javarand/{email}/challenge")
current_value = int(response.text)
print(current_value)
```

```328590446```
La respuesta puede enviarse del siguiente modo con curl:
```bash
$ curl -F number=798563412 https://cripto.iua.edu.ar/javarand/user@example.com/answer
Lo siento, siga participando.
```
O en el caso de Python:
```python
number = 798563412
response = requests.post(
    f"{server}/javarand/{email}/answer",
    files = { "number": str(number).encode('ascii')}
)
print(f"Status code: {response.status_code}")
print(response.text)
```
```
Status code: 200
Lo siento, siga participando.
```
En este caso, la respuesta enviada fue incorrecta.

### El generador de números aleatorios de Java
Java utiliza un generador congruencial lineal1. Estos generadores están definidos por la siguiente recurrencia:

Es decir, cada valor es el resultado de multiplicar el valor anterior por una constante 
 (el multiplicador), sumarle una constante 
 (el incremento) y calcular el resto de dividirlo por una tercera constante 
 (el módulo). El valor inicial 
 se llama semilla (seed).

En el caso de Java, las tres constantes son:
```
Constante	Valor
multiplicador	25214903917
incremento	11
módulo	2^48
```
La semilla se inicializa con el método setSeed(). El código siguiente es una versión simplificada del código real:
```java
public void setSeed(long seed) {
    this.seed = (seed ^ 0x5DEECE66DL) & ((1L << 48) - 1);
}
```
Como el módulo es una potencia de 2, la operación 
```
x  & ((1L << 48) - 1) 
equivale a 
x % (1L << 48) 
(es decir x mod 2^48).
```

Podemos observar que si bien se utiliza el tipo long, de 64 bits, todos los valores producidos son de 48 bits. Como este tipo de generador tiene el incoveniente de que los bits menos significativos tienen ciclos cortos, cuando se desea obtener un número de 32 bits se extraen los 32 bits más significativos.

El código siguiente es una versión simplificada del código real:
```java
int nextInt() {
    this.seed =  (this.seed * 0x5DEECE66DL + 0xBL) & ((1L << 48) - 1);
    return (int)(this.seed >>> 16);
}
```

Puede verse que si conocemos el estado del generador, es decir el valor de seed, es muy fácil saber cuál es el número siguiente. Pero al pedir un entero, no obtenemos el estado del generador, sino solo 32 bits de ese estado. Nos faltan 16 bits. Sin embargo, si tenemos la salida de dos números del generador, podemos probar todos los valores posibles de esos 16 bits en el primer número y verificar cuál produce un estado capaz de generar el segundo número.

https://docs.oracle.com/javase/8/docs/api/java/util/Random.html↩︎

### Ejemplo
El siguiente código muestra los diez primero números generados con la semilla 1234567890:
```bash
jshell> import java.util.Random

jshell> var random = new Random()
random ==> java.util.Random@5b6f7412

jshell> random.setSeed(1234567890)

jshell> for (int i = 0; i < 10; i++)
   ...>   System.out.println(random.nextInt())
-1210225942
-1908238811
-106137654
-1281935452
-235120565
-214157664
642760798
-803876832
-424719337
-67890154

jshell> 
```
