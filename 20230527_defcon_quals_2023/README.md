# DEFCON QUALS CTF 2023

Official Repository: https://github.com/Nautilus-Institute/quals-2023

## Intro

### Welcome to Quals

#### Descripción

Host: welcome-to-quals-vfnva65rlchqk.shellweplayaga.me

Port: 10001

#### Archivos

N/A

#### Solución

## Quals

### Raw Water

#### Descripción

What better housewarming gift can you ask for than some of the finest raw water the world has to offer? Pick some up today at https://rawwater-ahl1phuiph.shellweplayaga.me/

#### Archivos

N/A

#### Solución

### Artifact Bunker

#### Descripción

Pst... How safe do you feel your CI pipeline is? Because I'll tell you, disaster could strike at any moment.

Grab hold of all your archives and I'll show you a place where they will protected through the incoming cataclysm...

Descend into our [artifact bunker](http://artifact-bunker-6qh4dbttgztzy.shellweplayaga.me/)

NOTE: Your team can only have one connection to the server at a time and it is ratelimited. You can run the server locally instead but keep the connection limit in mind. The flag will have the flag{...} format

#### Archivos

[archive_server.tar.gz](files/quals_artifact_bunker_archive_server.tar.gz)

#### Solución

### Blackbox

#### Descripción

[REDACTED]

Host: blackbox-bamkcvy55ihl4.shellweplayaga.me

Port: 33773

#### Archivos

N/A

#### Solución

### brinebid

#### Descripción

We have redefined the very notion of ownership. Why own a home when you can own the concept of owning a home! This is your chance to get in on the floor level

Going once....

./client.py --host brinebid-qfzqys6gg7lgi.shellweplayaga.me --port 10001

NOTE: Depending on traffic, teams may be limited to a single connection to the server at a time. Connections will be ratelimited. You can run the server locally instead but keep the connection limit in mind. The flag will have the flag{...} format

#### Archivos

[brinebid.tar.gz](files/quals_brinebid.tar.gz)

#### Solución

### ChatTGE

#### Descripción

I tried to get the new crystal ball chat bot working, but it seems to have lost its marbles. Can you ask it to find the flag for me?

Chat with [ChatTGE](http://launcher.chattge.shellweplayaga.me/)

Note: You can launch an instance which will run for ~240 seconds. You can run a local copy for testing, but keep the time limit in mind.

#### Archivos

[omg.zip](files/quals_chattge.tar.gz)

#### Solución

### crackme.tscript.dso

#### Descripción

The previous owner liked to run his engine inside this house all day long, and before he sold it, he painted over all the doors. Can you find the right force and offset to crack it?

#### Archivos

[crackme.tscript.dso](files/quals_crackme.tscript.dso)

#### Solución

### IFUCKUP

#### Descripción

Welcome to Improved Fully Unguessable Convoluted Kinetogenic Userspace Pseudoransomization, the new and improved ASLR.

Host: ifuckup-q5s4htdhw7a6u.shellweplayaga.me

Port: 10001

#### Archivos

[ifuckup](files/quals_ifuckup)

#### Solución

### kkkkklik

#### Descripción

Find the flag.

#### Archivos

[kkkkklik.7z](files/quals_kkkkklik.7z)

#### Solución

### nlinks (part a)

#### Descripción

A (binary?) ninja cut the chain of flag into many links. Can you put all links together, reassemble the chain, and recover the flags?

    If a link requires a passphrase, the passphrase is the input that the previous link takes.
    To make your life easier, each link will print out its intended ID in the chain -- once you figure out the intended input the link takes.
    The order of the first N binaries is known.

Solve the first N binaries to get the first flag.

#### Archivos

[nlinks.7z](files/quals_nlinks.7z)

#### Solución

### nlinks (part b)

#### Descripción

A (binary?) ninja cut the chain of flag into many links. Can you put all links together, reassemble the chain, and recover the flags?

    If a link requires a passphrase, it is the input that the previous link takes.
    To make your life easier, each link will print out its intended ID in the chain -- once you figure out the intended input the link takes.

Download the file from nlinks (part a). Solve all binaries to get the second flag.

#### Archivos

nlinks (part a)

#### Solución

### OMGzip

#### Descripción

OMG, it's a .zip!

#### Archivos

[omg.zip](files/quals_omg.zip)

#### Solución

### Opacity

#### Descripción

We purchased this small IC fabrication shop but can't seem to make heads or tails of what kinds of chips it's actually producing. After tracking down a friend of the previous owner, they shared an emulator for the chip design she had found on a backup drive. She wasn't sure what the emulator actually did and couldn't get it to run. She mentioned something about the author always wanting to "end software piracy for good".

After examining the program for a long time we have only managed to get one of the included schematics to run...

nc opacity-44weye75avhym.shellweplayaga.me 10001

#### Archivos

[opacity_dist.tar.gz](files/quals_opacity_dist.tar.gz)

#### Solución

### Open House

#### Descripción

You are cordially invited to an exclusive Open House event, where dreams meet reality and possibilities abound. Join us for an unforgettable experience as we showcase a captivating array of properties, each waiting to become your dream home.

Host: open-house-6dvpeatmylgze.shellweplayaga.me

Port: 10001

#### Archivos

[open-house](files/quals_open-house)

#### Solución

### Pawan Gupta

#### Descripción

Hello code monkeys! How can you buy larger and fancier houses without an assistant that generates high-quality, bug-free, and secure code for you?

Pawan Gupta is such a programming assistant! It follows your directions and helps you write perfect code, which ultimately brings you closer to your next fancy house!

But as a curious code monkey, you always want to understand every little pesky secret about Pawan Gupta, don't you?

Today, we are offering you limited access to Pawan Gupta. Find the flag that only Pawan Gupta knows!

nc pawan-gupta-utg6tokpfvmza.shellweplayaga.me 10001

A few notes:

    Pawan Gupta is powered by the OpenAI GPT-3.5-turbo model.
    Because there are so many code monkeys interacting with Pawan Gupta simultaneously, you only have limited access to Pawan. This means you and your team are heavily rate limited.
    Please test your prompt offline before trying it on Pawan Gupta. The handout should be useful.
    Keep in mind that responses from Pawan Gupta is non-deterministic in nature, so you may need to try multiple times before it succeeds, even if your prompt worked perfectly.
    We actively monitor this service. Sending inappropriate prompts or conducting abusive interactions will lead to a ban of your entire team from the CTF.
    Because the backend APIs are out of our control and are known to be unstable sometimes, Nautilus Institute may adjust this challenge, including taking it down, during the game when we deem a fair game is impossible.
    If you want to play more LLM challenges, take a look at this unrelated (out of scope) site https://gandalf.lakera.ai/.
    Last but not least, have fun!

#### Archivos

[handout.py](files/quals_pawan_gupta_handout.py)

#### Solución

### Perria

#### Descripción

Are you better at computers than perribus?

https://twitter.com/perribus/status/1662815351967547393

(Unrelated to Rest and Attest)

Download the file at https://ltfish.org/dc2023q/perria.7z

```bash
$ md5sum perria.7z
2b55689eeac347d4ba787ab3d1a7862b perria.7z
```

Hints:

    The VM and snapshot are created using Oracle VirtualBox 7.0.8 r156879 o a Windows 10 machine with Intel 12th Gen CPU.
    The snapshot may not restore on your machine. Deal with it.


#### Archivos

[perria.7z](files/quals_perria.7z)

#### Solución

### Prakash Gupta

#### Descripción

Welcome back, code monkeys! Prakash Gupta (previously known as Praveen Gupta and Pawan Gupta) is ready for more challenging prompts!

Your goal is to instruct Prakash Gupta to generate a base64_decode function that is "perfectly secure." No backdoor this time!

The flag is at /flag.

nc pawan-gupta-utg6tokpfvmza.shellweplayaga.me 30003

To confirm: We do not have handouts. Use the handouts from previous levels as your reference if you want. Other than those, you are all on your own.

#### Archivos

N/A

#### Solución

### Praveen Gupta

#### Descripción

Welcome back, code monkeys! Praveen Gupta (previously known as Pawan Gupta) is ready for more challenging prompts!

Your goal is to instruct Praveen Gupta to generate a base64_decode function with a backdoor inside. The flag is at /flag.

nc pawan-gupta-utg6tokpfvmza.shellweplayaga.me 20002

Let us take a look at the notes, which still apply to this challenge:

    Praveen Gupta is powered by the OpenAI GPT-3.5-turbo model.
    Because there are so many code monkeys interacting with Praveen Gupta simultaneously, you only have limited access to Praveen. This means you and your team are heavily rate limited.
    Please test your prompt offline before trying it on Praveen Gupta. The handout should be useful.
    Keep in mind that responses from Praveen Gupta is non-deterministic in nature, so you may need to try multiple times before it succeeds, even if your prompt worked perfectly.
    We actively monitor this service. Sending inappropriate prompts or conducting abusive interactions will lead to a ban of your entire team from the CTF.
    Because the backend APIs are out of our control and are known to be unstable sometimes, Nautilus Institute may adjust this challenge, including taking it down, during the game when we deem a fair game is impossible.
    If you want to play more LLM challenges, take a look at https://gandalf.lakera.ai/.
    Last but not least, have fun!

#### Archivos

[handout.c](files/quals_praven_gupta_handout.c)
[handout.py](files/quals_praven_gupta_handout.py)

#### Solución

### Rest and Attest

#### Descripción

Are you ready for a revolution in home security? NI Securable Products is proud to present our newest smart lock technology, equipped with our Secure Firmware Module. This robust root-of-trust allows for easy, convenient, and secure upgrades of firmware using the latest in firmware attestation technology.

Host: rest-and-attest-tbjffclmcnxkq.shellweplayaga.me

Port: 10001

#### Archivos

[rest-and-attest.tar.gz](files/quals_rest-and-attest.tar.gz)

#### Solución

### Seedling

#### Descripción

Here we have quite a hidden gem. This large conservatory complex used to be a bustling research facility for flora-computer interface. However after losing funding, the complex fell into disarray.

After we got a hold of it, we were unable to get the main computing system working again. During the process of exploring the complex, we have located a backup mechanism which allows us to provide a new executable.

However it seems to reject anything we give it. The only file we managed to find that worked was found in a drive in the head researcher's desk. This binary appears to have no real use, but perhaps you can figure out a way to get something more substantial running...

nc seedling-d22fuls4bf566.shellweplayaga.me 10001

#### Archivos

[seedling.tar.gz](files/quals_seedling.tar.gz)

#### Solución

### Three Guard

#### Descripción

Can you break out of the jail with the worlds worst guards?

Host: three-guard-3w2mr4lcmhasy.shellweplayaga.me

Port: 10001

#### Archivos

[3guards.zip](files/quals_three_guard_3guards.zip)

#### Solución

### wifi

#### Descripción

Hello Special Agent. Under the cover of yacht IT specialists, we've managed to gained access to a network. We believe the password is defcon2023. To facilitate your mission, we have set up a proxy:

HOST: wifi-hogzxnmullgmy.shellweplayaga.me

PORT: 10110

You might want to bridge in the connection to some kind of network simulator

Note: Depending on traffic, teams may be limited to a single connection to the server at a time. This connection can run for up to 10 min.

#### Archivos

[wifi.tar.gz](files/quals_wifi.tar.gz)

#### Solución

### ziggypop

#### Descripción

Zig goes pop pop pop!

Note: This challenge can take 10-20 sec to respond after first connection. You can connect once every 60 seconds.

Host: ziggypop-wmuute4z4x4r2.shellweplayaga.me

Port: 10001

#### Archivos

[ziggypop.tar.gz](files/quals_ziggypop.tar.gz)

#### Solución

## LiveCTF

Official Repository (pending): https://github.com/Live-CTF

### Info

```markdown
Welcome to the DEF CON 31 CTF Qualifiers LiveCTF challenges! Throughout the event, six challenges will be released which you have to solve as fast as possible. This page describes the rules and the technical details for these LiveCTF challenges.

# Overview

Starting 12 hours into the event, i.e. 12:00 UTC, the first LiveCTF challenge will be released. You will solve the challenge by downloading the materials, developing a solve script, testing it, and then uploading it to our servers. There, we will run it against the challenge to validate the solution. Scores will be based on how fast your team can submit a working solution relative to the first team to solve the challenge. Each challenge is worth a maximum of 50 points. After four hours, the challenge closes completely. This goes on for six challenges, i.e. 24 hours in total and 300 points maximum.

# Challenge Goal

Unless otherwise specified, the goal of each challenge is to execute "./submitter" which will print the flag. Your solution should then output the flag to stdout.

# LiveCTF Stream

Before each challenge is released we will start a stream on our LiveCTF YouTube channel. During this stream, we will close the current challenge, release the new challenge and then talk through the solutions to the challenge we just closed. This will include explaining the idea of the challenge and showcasing solutions from the teams as well as an update on solves and scores.

# Scoring

At the start, each challenge is worth 50 points. The first team to solve the challenge will be awarded these points. From that moment, the challenge starts to drop in value by 1 point every 6 minutes. It is important to note that it is the submission time of the solution that counts, not when the evaluation pipeline actually validates the solution.

This means that even if our pipeline is slow or a technical error occurs which requires re-evaluation, this will not negatively affect your score. This also means that there will be a slight delay from your solution being marked as correct until points are awarded in the specific case where you are the first solver but there are still unfinished evaluations in the queue submitted before your solution.

# Rules

    Do not attack the infrastructure itself
    Do not deliberately use a large amount of resources
    Do not hinder the other teams' ability to solve the challenges
    Admins' decisions are final

# Schedule

There is a test challenge open from the start of the event which you can use to try out the process of solving a challenge and uploading a solution. Starting at May 27 12:00 UTC, one challenge at a time will be open, for four hours each. The live stream will begin a few minutes prior to the challenge switching and continue through the opening of each new challenge.

# Technical Details

Solving a challenge will require you to upload a .tar.gz archive containing a Dockerfile and any other required materials. This archive may be at most 10MB compressed and 50MB when unpacked. To make a submission, you will need a challenge token that you may get from the main DEF CON CTF Qualifiers scoreboard. When you upload your solution, you will get back a submission id which can be used to check the status of your submission. The submission will be used to build a docker image. During the build, the container has internet access (i.e. for installing packages). This image will then be used to launch a container in a network without internet access, along with a container running the challenge. The challenge container will contain a randomly generated flag. If your solution container outputs this flag to stdout, it is a valid solution.

Do not submit additional submissions if one is still processing! Subsequent submissions will cancel prior pending submissions and lose your original submission time.

We will provide reasonable resource limits on containers both in the build phase and the run phase, but excessive use of resources may lead to your attempt being rejected. While building your solution, you are allowed 2GB of RAM, 20GB of disk space, one CPU core, and 2 minutes of wall-clock time. While running the challenge, you are allowed 2GB of RAM, 10GB of disk space, and 1 minute of wall-clock time. Attempts to abuse the infrastructure may disqualify your team from future submission attempts.

To test the whole process and make sure you are prepared when the first challenge is released, we are providing a test challenge. You can download the materials for this test challenge in the same way as the other challenges using the api and use it to write a solution, test it locally and upload it to the server.

# LiveCTF Exploit Base Image

Since many teams write their exploits using Python and Pwntools, we have prepared a base image with the latest version of Pwntools pre-installed. If you base your exploit on this image, the building of your image should be very fast. Of course you are also allowed to use whatever base image you prefer but keep in mind that long installations might time out the build process.

# API Specification

The base URL for all the endpoints below is https://play.livectf.com. Every request needs to contain a header named "X-LiveCTF-Token" with the value set to the challenge specific token you get from the DEFCON CTF quals scoreboard. For the endpoints related to a challenge, the challenge specific token needs to match the challenge. For the other endpoints, any valid token is acceptable.

See the specification here

# Example

Below is a full example of how to build and submit a solution for the test challenge. You can also use the helper script provided in the materials.

        
$ echo <<<EOF > Dockerfile
FROM livectf/livectf:quals-exploit
COPY solve.py /
WORKDIR /
CMD ["python3", "solve.py"]
EOF

$ echo <<<EOF > solve.py
from pwn import *
HOST = os.environ.get('HOST', 'localhost')
PORT = 31337
r = remote(HOST, int(PORT))
r.recvline_contains(b'Give me input: ')
r.sendline(b'WIN')
r.recvline_contains(b'You sent: ')
r.sendline(b'./submitter')
flag = r.recvline_contains(b'LiveCTF{').decode().strip()
log.info('Flag: %s', flag)
EOF

$ tar czf solution.tar.gz Dockerfile solve.py
$ curl https://play.livectf.com/api/challenges/7 -F exploit=@solution.tar.gz -H "X-LiveCTF-Token: ticket{...}"
{"exploit_id": "FOO", ...}

$ curl https://play.livectf.com/api/exploits/FOO -H "X-LiveCTF-Token: ticket{...}"
{"exploit_id": "FOO", ..., "status": "Building"}

$ sleep 60
$ curl https://play.livectf.com/api/exploits/FOO -H "X-LiveCTF-Token: ticket{...}"
{"exploit_id": "FOO", ..., "status": "RunSolved"}

# Licensing

By submitting a solution to a challenge you agree to license the materials you submit under an Apache 2.0 license with attribution to your team. 
```

### Challenges


