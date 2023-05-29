# WPI CTF 2022

>Challenge files complete but missing challenge information.

## Misc

### Adversarial Machine Learning

#### Stats

| Attribute | Info |
|---|---|
| Description | The server seems to not like pictures of cats. How strange. Can you develop a patch to persuade the server that it is not looking at a cat? <br> Encode your patch image as base64 when sending it to the server. |
| Files | [adversarial_machine_learning_verification](files/misc_adversarial_machine_learning_verification.py) |

#### Solution

## Crypto

### I <3 Pie Salad

#### Stats

| Attribute | Info |
|---|---|
| Description | You should get the drift by now <br> Flag: V1BJe3tyduKAoH9vd295e3F7dOKAnnXCgeKAmn0= |
| Files |   |

#### Solution

## Forensics

### Ancient Noises

#### Stats

| Attribute | Info |
|---|---|
| Description | Upon searching The Archive, we found a strange recording from the year 2000. We think it's some sort of communication. Can you help us understand the contents of this file? <br> Author: UnknownSilicon (Jake) |
| Files | [forensics_ancient_noises_archive](files/forensics_ancient_noises_archive.wav) |

#### Solution

## Reversing

### NeedToCough

#### Stats

| Attribute | Info |
|---|---|
| Description | Our important file, flag.jpg, has been encrypted by the totally new ransomware NeedToCough. The group is claiming to be pentesters... but their attack kinda seems like criminal extortion to us. We were able to recover this PCAP from our IDS and it appears to be related to the attack. We nee you to investigate the attached files and recover our flag! Warning: The binary payload was created for CTF purposes but is arguably malware. It should be restricted to files named "flag.jpg" - though this cannot be guarenteed. As always: do your reversing in a VM and ask for help if you need it. |
| Files | [needtocough_flag](files/reversing_needtocough_flag.cough) <br> [reversing_needtocough_recovered](files/reversing_needtocough_recovered.pcap) |

#### Solution

## Web

### Muffin Hater

#### Stats

| Attribute | Info |
|---|---|
| Description | Muffinhater88 has encrypted your precious photos of Muffin! I found his c&c server, I have it on pretty good authority that his username is `muffinhater88`. It seems his site is designed using an old version of FastAPI (0.65.1), meaning it is possible to take advantage of this CVE: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-32677. Can you break-in to his site and recover the encryption keys? <br> I found a search page that may be useful, and he seems to have left his api documentation exposed at `/docs` on his C&C server. You can send him URLs at `/simulated-user`. <br> Main Server: http://muffin-hater.wpi-ctf-2022-codelab.kctf.cloud:8000 <br> Search Server: http://muffin-hater.wpi-ctf-2022-codelab.kctf.cloud:8080 |
| Files |  |

#### Solution

## Pwn

### Wargames

#### Stats

| Attribute | Info |
|---|---|
| Description | The only winning move is not to play. |
| Files | [pwn_wargames](files/pwn_wargames_wargames) <br> [pwn_wargames_dockerfile](files/pwn_wargames_dockerfile) <br> [pwn_wargames_build_docker.sh](files/pwn_wargames_build_docker.sh) |

#### Solution

