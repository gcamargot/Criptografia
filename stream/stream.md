# Cambio de bits en un cifrado de flujo
## Desafío
En este desafío, el servidor permite a un usuario registrarse con un correo electrónico y un conjunto de datos adicionales, y devuelve un perfil cifrado con un algoritmo de cifrado de flujo.

Si el usuario registró el correo usuario@example.com y puso como datos “Juan P. Usuario”, el perfil tendrá la forma:

``` user=usuario@example.com;data=Juan P. Usuario;role=user```

Es decir, está compuesto por un conjunto de pares atributo-valor, de la forma {atributo}={valor}, y separados por punto y coma.

El servidor devuelve el perfil cifrado, precedido por un nonce de 16 bytes, y codificado en base64.

El desafío es alterar el mensaje cifrado de manera tal que al descifrarlo incluya el par role=admin. Esta alteración es posible porque los cifradores de flujo son maleables. Es posible modificar el texto cifrado de manera tal que al descifrarlo el texto claro haya sido modificado de manera predecible.

Este tipo de ataque se denomina bit flipping, porque el cambio de un bit en el texto cifrado provoca un cambio del mismo bit en el texto claro.

Para obtener los textos cifrados, se debe hacer un requerimiento POST a una URL de la forma:

```https://cripto.iua.edu.ar/stream-bitflip/{email}/register```

dónde {email} debe ser reemplazado por una dirección de correo electrónico registrada.

### El contenido debe ser de tipo FORM, con dos campos:

Un campo email, con una dirección de correo a registrar. No es necesario que sea la misma dirección utilizada para acceder al desafío.
Un campo data, con datos arbitrarios, codificado en base64. Los datos no pueden contener el carácter ‘;’ ni el carácter ‘=’.
La respuesta será un perfil como el descripto, cifrado, concatenado con el nonce y codificado en base64.

Si en lugar de hacer un requerimiento POST se hace un requerimiento GET, muestra un formulario que permite cargar los campos requeridos.

## Respuesta
La respuesta debe ser enviada mediante un requerimiento POST a la URL

```https://cripto.iua.edu.ar/stream-bitflip/{email}/answer```
El contenido debe ser de tipo FORM, con un campo message con un nuevo mensaje cifrado codificado en base64. Al descifrarlo, debe contener el par atributo-valor role=admin.

## Ejemplo
El siguiente ejemplo muestra como conectarse con el servidor usando curl

```bash
curl -F email=juan@hotmail.com -F data=wr9RdcOpIGVzdMOhcyBidXNjYW5kbz8K https://cripto.iua.edu.ar/stream-bitflip/user@example.com/register
bL75mIW7M45acRnf6sGPFVajPHuUGZgDBkjV/b1MpyRximBNDuyRnyB71rovmJ6gCuYIxqBJNQ5n8Bhlk9Sf+HQeSFCWi8RGWW41h28=

$ curl -F message=@message https://cripto.iua.edu.ar/stream-bitflip/user@example.com/answer
Lo siento, siga participando.
$ cat message
VGhlc2UgYXJlIG5vdCB0aGUgZHJvaWRzIHlvdSdyZSBsb29raW5nIGZvci4gSGFicsOhIHF1ZSBi
dXNjYXIgcG9yIG90cm8gbGFkby4K
```
