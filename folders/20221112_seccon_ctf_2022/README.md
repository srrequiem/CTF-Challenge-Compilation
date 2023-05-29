# SECCON CTF 2022

## Tabla de Contenidos

## Resumen de Vulnerabilidades

## Web

### bffcalc

#### Info

| Atributo | Valor |
|---|---|
| Descripción | There is a simple calculator! <br> http://bffcalc.seccon.games:3000 <br> http://bffcalc-2.seccon.games:3000 <br> Please confirm that you can get a dummy flag on your local server before you try your attack on the remote server. |
| Archivos | [bffcalc.tar.gz](files/web_bffcalc.tar.gz) |

#### Solución

### denobox

#### Info

| Atributo | Valor |
|---|---|
| Descripción | Your program runs in a sandbox! <br> http://denobox.seccon.games:3000 |
| Archivos | [denobox.tar.gz](files/web_denobox.tar.gz) |

#### Solución

### spanote

#### Info

| Atributo | Valor |
|---|---|
| Descripción | Single Page Application makes our note app simple. <br> http://spanote.seccon.games:3000 |
| Archivos | [spanote.tar.gz](files/web_spanote.tar.gz) |

#### Solución

### skipinx

#### Info

| Atributo | Valor |
|---|---|
| Descripción | ALL YOU HAVE TO DO IS SKIP NGINX <br> http://skipinx.seccon.games:8080 |
| Archivos | [skipinx.tar.gz](files/web_skipinx.tar.gz) |

#### Solución

### easylfi

#### Info

| Atributo | Valor |
|---|---|
| Descripción | Can you read my secret? <br> http://easylfi.seccon.games:3000 |
| Archivos | [easylfi.tar.gz](files/web_easylfi.tar.gz) |

#### Solución

### piyosay

#### Info

| Atributo | Valor |
|---|---|
| Descripción | I know the combination of DOMPurify and Trusted Types is a perfect defense for XSS attacks. <br> http://piyosay.seccon.games:3000 |
| Archivos | [piyosay.tar.gz](files/web_piyosay.tar.gz) |

#### Solución

## Crypto

### janken vs kurenaif

#### Info

| Atributo | Valor |
|---|---|
| Descripción | Do you know about the crypto witch? And about a her special cast too? server.py <br> `nc janken-vs-kurenaif.seccon.games 8080` |
| Archivos | [server.py](files/crypto_janken_vs_kurenaif_server.py) |

#### Solución

### pqpq

#### Info

| Atributo | Valor |
|---|---|
| Descripción | Warm your hands first. It's not obvious, right? |
| Archivos | [output.txt](files/crypto_pqpq_output.txt) [problem.py](files/crypto_pqpq_problem.py) |

#### Solución

### witches_symmetric_exam

#### Info

| Atributo | Valor |
|---|---|
| Descripción | crypto witch made a exam. The exam has to communicate with witch and saying secret spell correctly. Have fun ;) <br> `nc witches-symmetric-exam.seccon.games 8080` |
| Archivos | [problem.py](files/crypto_witches_symmetric_exam_problem.py) |

#### Solución

### this_is_not_lsb

#### Info

| Atributo | Valor |
|---|---|
| Descripción | Tired of difficult problems? Ok, I give you a simple LSB Padding Oracle problem. Ah, my magic has exploded... Sorry <br> `nc this-is-not-lsb.seccon.games 8080` |
| Archivos | [problem.py](files/crypto_this_is_not_lsb_problem.py) |

#### Solución

### insufficient

#### Info

| Atributo | Valor |
|---|---|
| Descripción | SUGOI SECRET SHARING SCHEME with insufficient shares |
| Archivos | [dist.tar.gz](files/crypto_insufficient_dist.tar.gz) |

#### Solución

### BBB

#### Info

| Atributo | Valor |
|---|---|
| Descripción | Sometimes I can't distinguish between "b" and "d" <br> `nc BBB.seccon.games 8080` |
| Archivos | [server.py](files/crypto_janken_vs_kurenaif_server.py) |

#### Solución

## Reversing

### eguite

#### Info

| Atributo | Valor |
|---|---|
| Descripción | Crack me. <br> The flag string inside "SECCON{...}" is all lowercase. <br> `* "eguite.exe" and "eguite.elf" are the same program. You can analyse whichever you prefer.` |
| Archivos | [eguite.exe](files/rev_eguite.exe) [eguite.elf](files/rev_eguite.elf) |

#### Solución

### DoroboH

#### Info

| Atributo | Valor |
|---|---|
| Descripción | I found a suspicious process named "araiguma.exe" running on my computer. Before removing it, I captured my network and dumped the process memory. Could you investigate what the malware is doing? <br> **The program is a malware. Do not run it unless you understand its behavior.** |
| Archivos | [doroboh.tar.gz](files/rev_doroboh.tar.gz) |

#### Solución

### babycmp

#### Info

| Atributo | Valor |
|---|---|
| Descripción | `baby_mode = 1` 👶 |
| Archivos | [chall.baby](files/rev_chall.baby) |

#### Solución

### eldercmp

#### Info

| Atributo | Valor |
|---|---|
| Descripción | `baby_mode = 0` 👴 <br> **The program is tested on Ubuntu 20.04 and 22.04 LTS (host machine). It might not run correctly on the other platforms such as WSL.* |
| Archivos | [chall.elder](files/rev_chall.elder) |

#### Solución

### Devil Hunter

#### Info

| Atributo | Valor |
|---|---|
| Descripción | Clam Devil; Asari no Akuma |
| Archivos | [devil_hunter.tar.gz](files/rev_devil_hunter.tar.gz) |

#### Solución

## Pwning

### lslice

#### Info

| Atributo | Valor |
|---|---|
| Descripción | Pull Request: Add `slice` method for Lua table <br> `nc lslice.seccon.games 9876` |
| Archivos | [lslice.tar.gz](files/pwn_lslice.tar.gz) |

#### Solución

### babyfile

#### Info

| Atributo | Valor |
|---|---|
| Descripción | Play with FILE structure!! <br> `nc babyfile.seccon.games 3157` |
| Archivos | [babyfile.tar.gz](files/pwn_babyfile.tar.gz) |

#### Solución

### babypf

#### Info

| Atributo | Valor |
|---|---|
| Descripción | Introduction to eBPF exploitation in 2022 :) <br> `nc babypf.seccon.games 9009` |
| Archivos | [babypf.tar.gz](files/pwn_babypf.tar.gz) |

#### Solución

### koncha

#### Info

| Atributo | Valor |
|---|---|
| Descripción | This is the first SECCON Finals competition in 2 years, so I want to know about the participants. <br> `nc koncha.seccon.games 9001` |
| Archivos | [koncha.tar.gz](files/pwn_koncha.tar.gz) |

#### Solución

### simplemod

#### Info

| Atributo | Valor |
|---|---|
| Descripción | Which bytes do you want to modify? <br> `nc simplemod.seccon.games 7250` <br> *NOTICE:* <br> This challenge is running with home-built glibc-2.3x. Excessive bruteforce is not required. Attacks that overload the server are prohibited. |
| Archivos | [simplemod.tar.gz](files/pwn_simplemod.tar.gz) |

#### Solución

## Misc

### latexipy

#### Info

| Atributo | Valor |
|---|---|
| Descripción | Latexify as a Service <br> `nc latexipy.seccon.games 2337`|
| Archivos | [latexipy.tar.gz](files/misc_latexipy.tar.gz) |

#### Solución

### find flag

#### Info

| Atributo | Valor |
|---|---|
| Descripción | Where is the flag? <br> `nc find-flag.seccon.games 10042` |
| Archivos | [findflag.tar.gz](files/misc_findflag.tar.gz) |

#### Solución

### noiseccon

#### Info

| Atributo | Valor |
|---|---|
| Descripción | Noise! Noise! Noise! <br> `nc noiseccon.seccon.games 1337` |
| Archivos | [noiseccon.tar.gz](files/misc_noiseccon.tar.gz) |

#### Solución

### txtchecker

#### Info

| Atributo | Valor |
|---|---|
| Descripción | I'm creating a text file checker. It still in the process of implementation... <br> `sshpass -p ctf ssh -oStrictHostKeyChecking=no -oCheckHostIP=no ctf@txtchecker.seccon.games -p 2022` |
| Archivos | [txtchecker.tar.gz](files/misc_txtchecker.tar.gz) |

#### Solución


