# CSAW

## misc

### Quantum Leap 

#### Stats

| Attribute | Info |
|---|---|
| Description | My friend took the quantum leap and purchased a quantum computer with two qubits. They mentioned using a quantum logic gate to input the flag and they gave me the computers output. I have been stuck and Can NOT figure out the flag. |
| Files | [output](./files/misc_quantum_leap_output) |

#### Solution

### Donate-More

#### Stats

| Attribute | Info |
|---|---|
| Description | You wanted to donate more amount than once to the CSAW community, but this smart contract (contract address: 0xAcA533Ba3F6339706cd8A68C66Dd3323331E3BC6, Network: Ropsten) allows you to donate only once. Can you break it and donate more?\n Note: To get your flag, get your token from the netcat server and check whether you got flag or not after completing the getFlag() transaction successfully. For any doubts DM admins in Discord. <br> `nc misc.chal.csaw.io 5004` |
| Files | [blockchainchallenge.sol](./files/misc_donate-more_blockchainchallenge.sol) |

#### Solution

### CatTheFlag

#### Stats

| Attribute | Info |
|---|---|
| Description | This is an intro to Neural Networks and Data Analysis challenge. <br> http://misc.chal.csaw.io:5000 |
| Files | [inputs.zip](./files/misc_cattheflag_inputs.zip) |

#### Solution

### ezMaze

#### Stats

| Attribute | Info |
|---|---|
| Description | Pytorch is a widely used AI framework. I use it as a carrier to provide a simple and interesting game. I hope you like it. The flag is md5(the shortest path of the maze). Author: member of r3kapig |
| Files | [maze.pt](./files/misc_ezmaze_maze.pt) |

#### Solution

## web

### Good Intentions

#### Stats

| Attribute | Info |
|---|---|
| Description | We're an in development public platform for labeling images captured with deep-space telescopes! These images will be used to assist machine learning models for identifying space objects. Still have a lot of work to do... right now we just have the API exposed, still working on a full front end to help less technical people contribute! For anyone interested in the project send them the api_doc.txt and api_client.py to help get them started. <br> http://web.chal.csaw.io:5012 |
| Files | [dist.zip](./files/web_good_intentions_dist.zip) |

#### Solution

### Smuggling Mail

#### Stats

| Attribute | Info |
|---|---|
| Description | Join our waitlist and we'll let you know about apartment vacancies! <br> https://web.chal.csaw.io:5009 |
| Files | [dist.zip](./files/web_smuggling_mail_smuggling-mail.tar.gz) |

#### Solution

## rev

### DockREleakage

#### Stats

| Attribute | Info |
|---|---|
| Description | A breach occurred and some files have been leaked. One of the leaked files named `dockREleakage.tar.gz` contains an image of one of the company's components. An anonymous hacker has reached out to me and beware me that there is some serious mistake in my build image process. The hacker implies that sensitive information should be handled carefully. However, I couldn't find the mistake by myself. Please help me! |
| Files | [dockREleakage.tar.gz](./files/rev_dockreleakage_dockreleakage.tar.gz)  |

#### Solution

### Anya Gacha

#### Stats

| Attribute | Info |
|---|---|
| Description | It is a Gacha game where the player spend coins to do lucky draw. If they can get the rare character Anya, she will tell the player our flag! <br> NOTE: Flag needs to be in standard format. |
| Files | [win.zip](./files/rev_anya_gacha_win.zip) [linux.zip](./files/rev_anya_gacha_linux.zip) [mac.app.zip](./files/rev_anya_gacha_mac.app.zip) |

#### Solution

### game

#### Stats

| Attribute | Info |
|---|---|
| Description | I found this game and it has a Patreon page. There are some easter eggs hidden behind a paywall. Can you get the easter eggs for me without paying for them? <br> `nc rev.chal.csaw.io 5003` |
| Files | [game](./files/rev_game_game) |

#### Solution

### The Big Bang

#### Stats

| Attribute | Info |
|---|---|
| Description | Do you have a favourite number? I do! `nc rev.chal.csaw.io 5004` |
| Files | [challenge.py](./files/rev_the_big_bang_challenge.py) |

#### Solution

### Conti

#### Stats

| Attribute | Info |
|---|---|
| Description | Can you recover my files :( my grandson downloaded a binary from a .pcap to send to a consultant... |
| Files | [Conti.exe](./files/rev_conti_conti.exe) [encryptedfiles.zip](./files/rev_conti_encryptedfiles.zip) |

#### Solution

## forensics

### Android x86

#### Stats

| Attribute | Info |
|---|---|
| Description | There are some secrets on this phone image. Please find the flag! |
| Files | [android_easy.zip](./files/forensics_android_easy.zip)  |

#### Solution

### encrypted disk

#### Stats

| Attribute | Info |
|---|---|
| Description | th31nk encrypted his disk and forgot the password, can you help him? Flag is what you find, no need to wrap. <br> HINT: Custom Profile? |
| Files | [encrypted_disk.zip](./files/forensics_encrypted_disk.zip)  |

#### Solution

### noir

#### Stats

| Attribute | Info |
|---|---|
| Description | I am a forest, and a night of dark trees: but he who is not afraid of my darkness, will find banks full of roses under my cypresses. <br> (A flag submission note for hacking serenity: Please put the flag in standard format.) |
| Files | [noir.png](./files/forensics_noir_noir.png)  |

#### Solution

## crypto

### Gotta Crack Them All

#### Stats

| Attribute | Info |
|---|---|
| Description | As an intern in the security department, you want to show the admin what a major security issue there is by having all passwords being from a wordlist (even if it is one the admin created) as well as potential issues with stream ciphers. Here's the list of encrypted passwords (including the admin's), the encryption algorithm and your password. Can you crack them all and get the admin's password? Here is the web service that the admin made to encrypt a password: `nc crypto.chal.csaw.io 5002` <br> NOTE: The flag is just the admin's password. |
| Files | [encrypt.py](./files/crypto_gotta_crack_them_all_encrypt.py) [leaked_password.txt](files/crypto_gotta_crack_them_all_leaked_password.txt) [encrypted_passwords.txt](./files/crypto_gotta_crack_them_all_encrypted_passwords.txt) |

#### Solution

### Not Too Taxing

#### Stats

| Attribute | Info |
|---|---|
| Description | We intercepted some email communications between a tax consultant and his client that contained some important tax documents. We were able to successfully extract two of the documents, but we can't figure out the password to the file in order to extract the data. Attached are the two extracted files, Tax_Ret_Form_Blank.pdf and Tax_Ret_Form_Nov_2021.zip, and a transcript of the emails we found, SPBlock_Email.pdf. <br> Can you figure out the password so we can get this guy's info? |
| Files | [tax_ret_form_blank.pdf](./files/crypto_not_too_taxing_tax_ret_form_blank.pdf) [tax_ret_form_nov_2021.zip](./files/crypto_not_too_taxing_tax_ret_form_nov_2021.zip) [spblock_email.pdf](files/crypto_not_too_taxing_spblock_email.pdf) |

#### Solution

### Poodle Gift Shop

#### Stats

| Attribute | Info |
|---|---|
| Description | Why not buy some poodle companions at our canine gift shop? Every order is celebrated with a plane flying overhead bearing a banner. Wait! is there something hidden in that banner? <br> `nc crypto.chal.csaw.io 5004` |
| Files | [server.py](./files/crypto_poodle_gift_shop_server.py) |

#### Solution

### Beyond_Quantum

#### Stats

| Attribute | Info |
|---|---|
| Description | New crypto systems like NTRU can help us stay safe in the post-quantum era! Also in the post-quantum era: errore umano. <br> `nc crypto.chal.csaw.io 5003` |
| Files | [server.py](./files/crypto_beyond_quantum_server.py) [cipher.py](./files/crypto_beyond_quantum_cipher.py) [mathutils.py](files/crypto_beyond_quantum_mathutils.py) |

#### Solution

## pwn

### ezROP

#### Stats

| Attribute | Info |
|---|---|
| Description | Pwn your first Windows binary! We made it easy and are providing all the code so you can get points for learning to use a new set of tools. <br> `nc win.chal.csaw.io 7777` |
| Files | [share.zip](./files/pwn_ezrop_share.zip) |

#### Solution

### baby windows

#### Stats

| Attribute | Info |
|---|---|
| Description | This is a simple buffer overflow challenge, but I wrote it in a reversed way :) <br> `nc pwn.chal.csaw.io 5002` |
| Files | [BabyWindows.c](./files/pwn_baby_windows_babywindows.c) [BabyWindowsLib.c](./files/pwn_baby_windows_babywindowslib.c) [BabyWindowsLib.dll](./files/pwn_baby_windows_babywindowslib.dll) [BabyWindows.exe](./files/pwn_baby_windows_babywindows.exe) [BabyWindowsLib.h](./files/pwn_baby_windows_babywindowslib.h) [Dockerfile](./files/pwn_baby_windows_dockerfile) [socat-1.7.3.0-windows-master.zip](./files/pwn_shello_world_socat-1.7.3.0-windows-master.zip) |

#### Solution


### how2pwn

#### Stats

| Attribute | Info |
|---|---|
| Description | how2pwn is a series of beginner-friendly pwn challenges to make pwning and shellcoding more approachable. <br> Servers: <br> `nc how2pwn.chal.csaw.io 60001` <br> `nc how2pwn.chal.csaw.io 60002` <br> `nc how2pwn.chal.csaw.io 60003` <br> `nc how2pwn.chal.csaw.io 60004` |
| Files | [pwn_how2pwn](./files/pwn_how2pwn) |

#### Solution


### shello world 

#### Stats

| Attribute | Info |
|---|---|
| Description | Write your first Windows shellcode! `nc win.chal.csaw.io 7778` |
| Files | [ShelloWorld.exe](./files/pwn_shello_world_shelloworld.exe) [ShelloWorldLib.dll](./files/pwn_baby_windows_babywindowslib.dll) [Dockerfile](./files/pwn_shello_world_dockerfile) [socat-1.7.3.0-windows-master.zip](./files/pwn_shello_world_socat-1.7.3.0-windows-master.zip) |

#### Solution


### unsafe-linking 

#### Stats

| Attribute | Info |
|---|---|
| Description | You have found a mysterious notebook program running on a server. Unfortunately, the notebook program is faulty and has an issue with improperly handling memory allocation/deallocation. The notebook uses GLIBC-2.35 which implemented safelinking. Find a way to capture the flag by recovering leaked safelinking data! `nc pwn.chal.csaw.io 5003` |
| Files | [share.zip](./files/pwn_unsafe-linking_share.zip) |

#### Solution

