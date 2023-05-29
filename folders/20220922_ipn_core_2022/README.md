# IPN Core 2022 CTF

## Web

### Pentest web Parte 1

#### Stats

| Attribute | Info |
|---|---|
| Description | Uhmm no necesitas contexto... |
| Files | [web_pentest_web_1.zip](files/web_pentest_web_1.zip) |

#### Solution

### Pentest web Parte 2

#### Stats

| Attribute | Info |
|---|---|
| Description | Uhmm nop, no necesitas descripción... ¿o sí? |
| Files | [web_pentest_web_2.zip](files/web_pentest_web_2.zip) |

#### Solution

### Pentest web Parte 3

#### Stats

| Attribute | Info |
|---|---|
| Description | Es divertido el pentest web desde Blackbox ¿no? :) |
| Files | [web_pentest_web_3.zip](files/web_pentest_web_3.zip) |

#### Solution

### CIC Blog

#### Stats

| Attribute | Info |
|---|---|
| Description | ¿Qué tal? Estoy por terminar mi blog y un colega de {\|4_p4nd1\|\|4_m4nt3q1\|\|4}  me hizo favor de revisar el sitio, había encontrado algo pero aún no termina.  Mientras tanto me gustaría saber que encontró, ¿me ayudas también a revisarlo? |
| Files | [web_cic_blog.zip](files/web_cic_blog.zip) |

#### Solution

### Tacos Don Chano

#### Stats

| Attribute | Info |
|---|---|
| Description | Me hice la promesa de ya entrar a mis clases de desarrollo web y le hice a mi tío Chano un sitio para que que pueda gestionar sus órdenes de tacos, pero de un momento a otro se ha estado comportando medio raro... y estoy teniendo errores inesperados, ¿qué crees que pueda estar mal? |
| Files | [web_tacos_don_chano.zip](files/web_tacos_don_chano.zip) |

#### Solution

## Crypto

### Encoding

#### Stats

| Attribute | Info |
|---|---|
| Description | ¿Qué tanto sabes de encoding? |
| Files | [crypto_encoding.txt](files/crypto_encoding.txt) |

#### Solution

### Esoteric0

#### Stats

| Attribute | Info |
|---|---|
| Description | ¡¡Esto es del diablo!! ¿puedes recuperar la flag? |
| Files | [crypto_esoteric.txt](files/crypto_esoteric.txt) |

#### Solution

### AESy

#### Stats

| Attribute | Info |
|---|---|
| Description | ¿Podrás romper la cookie y obtener acceso como admin? |
| Files | [crypto_aesy_chall.py](files/crypto_aesy_chall.py) |

#### Solution

### RealBabyRSA

#### Stats

| Attribute | Info |
|---|---|
| Description | RSA... ¡que común! |
| Files | [crypto_real_baby_rsa_output.txt](files/crypto_real_baby_rsa_output.txt) [crypto_real_baby_rsa_reto.py](files/crypto_real_baby_rsa_reto.py) |

#### Solution

### Baby-FA

#### Stats

| Attribute | Info |
|---|---|
| Description | ¿Seguirás el camino fácil?<br>La flag es en minúsculas |
| Files | [crypto_baby_fa.txt](files/crypto_baby_fa.txt) |

#### Solution

## Reversing

### T3SLA

#### Stats

| Attribute | Info |
|---|---|
| Description | Cadena fue de visita a la ESCOM en su nuevo Tsl4. Pero olvidó sus llaves en el laboratorio de redes y estará cerrado hasta mañana por el paro :( . Por suerte tu eres su amigo y le ayudarás a abrir el auto. Lo primero será revisar el firmware buscando la función encargada de validar la llave. |
| Files | [reversing_t3sla_chall](files/reversing_t3sla_chall) |

#### Solution

### T3SLA - Parte 2

#### Stats

| Attribute | Info |
|---|---|
| Description | Cuando la llave se comunica con el auto lo primero que hace es enviar una clave de 4 dígitos (que llegan a la función de chequeo como los primeros 4 parámetros).  ¿Cuáles son esos 4 dígitos correctos? <br> La flag es: flag{EncontrasteMiPin=PIN} Reemplazando PIN por los 4 dígitos correctos. <br> **NOTA: Para este reto deberás utilizar los mismo archivos del reto T3SLA** |
| Files | - |

#### Solution

### T3SLA - Parte 3

#### Stats

| Attribute | Info |
|---|---|
| Description | Ahora que conocemos el PIN, lo único que nos resta para poder abrir el auto es conocer el password que se envía junto a la clave de 4 dígitos. Esta password la lee la misma función de chequeo. La flag es la password. <br> ej.  flag{PASSWORD} <br> **NOTA: Para este reto deberás utilizar los mismo archivos del reto T3SLA** |
| Files | - |

#### Solution

## Pwning

### BabyPWN

#### Stats

| Attribute | Info |
|---|---|
| Description | Este es otro reto de PWN más, pero no te apures te estaré guiando :) <br> El primer paso para conseguir RCE es buscar algún bug de corrupción de memoria que nos permita tomar control del flujo de ejecución. <br> ¡Suerte! |
| Files | [pwn_babypwn_chall](files/pwn_babypwn_chall) [pwn_babypwn_chall.c](files/pwn_babypwn_chall.c) |

#### Solution

### BabyPWN - Parte 2

#### Stats

| Attribute | Info |
|---|---|
| Description | Para mala suerte la función cuenta con un mecanismo de seguridad conocido como stack canary que es una variable en la pila con un valor que si se modifica entonces el programa sabe que esta bajo un posible ataque. La buena noticia es que este stack canary tiene siempre el mismo valor.  Esta vez, cuando hagas el overflow asegúrate de escribir sobre el stack canary el valor correcto. <br> **NOTA: Para este reto deberás utilizar los mismo archivos del reto BabyPWN** |
| Files | - |

#### Solution

### BabyPWN - Parte 3

#### Stats

| Attribute | Info |
|---|---|
| Description | Como último paso necesitamos controlar ese flujo de ejecución;  por suerte, el programa imprime la cadena que le dimos usando la función system y como parámetro le pasa una cadena que almacena... ¡¡¡EN LA PILA!!!,  por lo que con nuestro overflow podremos modificar ese argumento para ejecutar system con lo que nosotros queramos ¡Suerte! :) <br> **NOTA: Para este reto deberás utilizar los mismo archivos del reto BabyPWN** |
| Files | - |

#### Solution

## Misc

### Bot Calculadora

#### Stats

| Attribute | Info |
|---|---|
| Description | Acabamos de descubrir e implementar una característica de Node.js del módulo vm y creamos una calculadora para usarlo, échale un lente crack. <br> ***NOTA: ÉSTE RETO TIENE PUNTAJE DINÁMICO,  MIENTRAS MÁS PERSONAS LO RESUELVAN EL PUNTAJE IRÁ DISMINUYENDO*** <br> https://t.me/node_vm_bot |
| Files | [misc_bot_bot_calculadora.zip](files/misc_bot_bot_calculadora.zip) |

#### Solution