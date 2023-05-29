# HTB Business CTF 2022:  Dirty Money

## Fullpwn

### Nimble

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | easy |
| Description | A Ransomware as a Service website has been found and seems to be targeting online users and encrypting their files. You are tasked with taking down this malicious website and restoring the users files. |
| File | - |

#### Solution

### MonkeyLab

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | easy |
| Description | We received a phishing email masquerading as a well known company and it is asking us to upload documents and check them for viruses. We believe that these documents are then reviewed by the APT operatives in order to leak confidential information and possibly get access to company resources. |
| File | - |

#### Solution

### Certification

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | A Certification Authority has declined our requests to access their data in order to identify a well known APT group. Unfortunately we do not have the juristiction to force them to cooperate. For this reason you are tasked with hacking their infrastructure in order to gather information. |
| File | - |

#### Solution

### Commercial

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | hard |
| Description | We have identified a dark net market by indexing the web and searching for favicons that belong to similar marketplaces. You are tasked with breaking into this marketplace and taking it down. |
| File | - |

#### Solution

## Web

### Debugger Unchained

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | easy |
| Description | Our SOC team has discovered a new strain of malware in one of the workstations. They extracted what looked like a C2 profile from the infected machine's memory and exported a network capture of the C2 traffic for further analysis. To discover the culprits, we need you to study the C2 infrastructure and check for potential weaknesses that can get us access to the server. |
| File | [web_debugger_unchained.zip](./files/web_debugger_unchained.zip) |

#### Solution

### Letter Dispair

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | easy |
| Description | A high-profile political individual was a victim of a spear-phishing attack. The email came from a legitimate government entity in a nation we don't have jurisdiction. However, we have traced the originating mail to a government webserver. Further enumeration revealed an open directory index containing a PHP mailer script we think was used to send the email. We need access to the server to read the logs and find out the actual perpetrator. Can you help? |
| File | - |

#### Solution

### Felonious Forums

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | Our threat intelligence has traced a reseller of the GrandMonty Ransomware linked with the Monkey Business group to this illegal forums platform. We need you to investigate the platform to find any security loopholes that can provide us access to the platform. |
| File | [web_felonious_forums.zip](./files/web_felonious_forums.zip) |

#### Solution

### PhishTale

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | Recently we identified a host matching a threat actor's TLS certificate facing the public internet. It contains an open-source phishing kit builder, so we have the source of the application at hand. We need you to get access to their server so that we can uncover their campaigns. Note: The host uses an HTTP/2 protocol with a self-signed certificate, so you must visit the host with the https:// protocol and accept the self-signed certificate to access. |
| File | [web_phishtale.zip](./files/web_phishtale.zip) |

#### Solution

### GrandMonty

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | hard |
| Description | Our investigation of an infected machine with the encryption ID "1f81b076-fffc-45cd-b7c3-c686b73aa6af" on the ransom note left by the GrandMonty Gang revealed that it was deployed to cover up the trace of Monkey Business to make the attack look like a typical ransomware attack. We need you to investigate their ransomware portal and reveal any sensitive information that may help us uncover their identity. |
| File | - |

#### Solution

## Pwn

### Superfast

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | easy |
| Description | We've tracked connections made from an infected workstation back to this server. We believe it is running a C2 checkin interface, the source code of which we aquired from a temporarily exposed Git repository several months ago. Apparently the engineers behind it are obsessed with speed, extending their programs with low-level code. We think in their search for speed they might have cut some corners - can you find a way in? |
| File | [pwn_superfast.zip](./files/pwn_superfast.zip) |

#### Solution

### Payback

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | easy |
| Description | A disgruntled member of the APT has leaked a popular DDoSaaS botnet tool and its source code, which is currently being sold in invite-only deep web forums. The Zoldyck-botnet program was used by extortionists in the recent DNS attacks, but the tor service panel has since been taken down. Intelligence has shown an identical SSH fingerprinted server operating on clearnet, we believe the tool is in use there. Can you pwn the server? |
| File | [pwn_payback.zip](./files/pwn_payback.zip) |

#### Solution

### Insider

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | While running routine updates, our deployment service alerted us of a hash mismatch on an FTP server installed in our network perimeter. While investigating, our SOC team notified us of breach attempts inside the network. We believe a threat actor has compromised the version control system and has inserted a backdoor to try and pivot throughout the network. We got locked from logging into the server, leaving only the FTP exposed. Can you find a way back inside before the attacker owns the network? |
| File | [pwn_insider.zip](./files/pwn_insider.zip) |

#### Solution

### OpenDoor

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | Via a database breach we've managed to obtain credentials for a malicious developer, and located a workstation they have previously used to develop their kernel backdoors. <br>Luckily, they forgot to uninstall it from their own system - can you use their own tools against them and uncover their secrets?<br>user: Dev<br>password: developer |
| File | [pwn_opendoor.zip](./files/pwn_opendoor.zip) |

#### Solution

### Midenios

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | hard |
| Description | We've identified an XSS vulnerability on a new RaaS product advertised in Felonious Forums. As we suspected, MonkeyBusiness operatives use Tor Browser to communicate with potential customers, and the exfiltrated IPs are proven ineffective. After a sting operation, we've managed to push some malicious commits in the tor browser repository. While not as notorious as V8, Tor Browser's JS engine is less hardened than its competitor, and bugs as simple as relative ArrayBuffer OOBs can be catastrophic. Can you find a way to gain RCE and identify the threat actors? |
| File | [pwn_midenios.zip](./files/pwn_midenios.zip) |

#### Solution

## Crypto

### ElElGamal

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | easy |
| Description | After some minor warnings from IDS, you decide to check the logs to see if anything suspicious is happening. Surprised by what you see, you realise that one of your honeypots has been compromised with a cryptominer. As you look at the processes, you discover a backdoor attached to one of them. The backdoor retrieves the private key from the /key route of a C2. It establishes a session by sending an encrypted initilazation sequence. After the session is established, it waits for commands. The commands are encrypted and executed by the source code you found. Unfortunately, the IDS could not detect the request to /key and the machine was rebooted after the compromise, so the key cannot be found on the stack. Can you find out if any data was exfiltrated from the honeypot to mitigate future attacks? |
| File | [crypto_elelgamal.zip](./files/crypto_elelgamal.zip) |

#### Solution

### BBGun06

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | easy |
| Description | We have received reports from CloudCompany that resources are involved in malicious activity similar to attempting unauthorized access to remote hosts on the Internet. We have since shut down the server and locked the SA. While we were trying to investigate what the entry point was, we discovered a phishing email from CloudCompany's IT department. You've since notified the vendor, and they've provided the source code of the email signing server for a security assessment. We've identified an outdated RSA verification code implementation, which we believe could be the cause of why the threat actors were able to impersonate the vendor. Can you replicate the attack and notify them of any possible misuse? |
| File | [crypto_bbgun06.zip](./files/crypto_bbgun06.zip) |

#### Solution

### Homomurphy's Law

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | After a sophisticated ransomware attack, the operational integrity of the country's critical maritime infrastructure has suffered a severe disruption, resulting in a force majeure declaration at several key container terminals. The Department of Public Enterprises has asked for our help to restore the shipping infrastructure's functionality. During the investigation, we uncovered a complex rootkit that, among other things, hides IPv4/IPv6 packets, the kernel module location, and the process itself. Subsequently, we cannot recover the C2 communication from the network capture taken during the incident. The ransomware note specified a payment portal. During the web application security assessment, an open directory on /backups was found, and two files were recovered. They appear to be part of a benchmarking utility for various encryption libraries used during the ransomware's development, and the TCP service is still up. Despite our warnings, officials decided to pay the ransom and haven't heard anything since, which confirms our suspicions that this originated as a wiper attack. We now have two days before the wiper deletes everything. We believe the encryption keys of the benchmarking service are the same as those used for the malware's encryption routine. Are you going to be able to prevent an economic meltdown and recover the encrypted files?  |
| File | [crypto_homomurphys_law.zip](./files/crypto_homomurphys_law.zip) |

#### Solution

### 400Curves

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | After the takeover of Felonious Forums, we've managed to identify and apprehend a low-level MonkeyBusiness APT operative. The developer was in charge of reselling components of the Zoid malware family. During a forensics investigation of the operative's computer, we obtained the prototype source code of the TLS-based proxy service, which was used to obfuscate C2 traffic between the compromised machines to evade interception/detection. The remote host is still up, but the ssh keys we found have since been invalidated. During an assessment of the component's source code, it looks like the key for the TLS-encrypted traffic is generated using the ECDH protocol with the P-256 curve, which is the most common curve on the Internet. Can you find a way to retrieve the proxy service's private key? |
| File | [crypto_400curves.zip](./files/crypto_400curves.zip) |

#### Solution

### Hash the Filesystem

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | hard |
| Description | Our investigations have led us to the file server of the APT group. Each member of the group uploads their artifacts and operational documents. A trusted source within our network provided us with the source code of the service. Can you get the flag? |
| File | [crypto_hash_the_filesystem.zip](./files/crypto_hash_the_filesystem.zip) |

#### Solution

## Reversing

### ChromeMiner

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | easy |
| Description | Discurd has filed a DMCA violation regarding a popular browser extension claiming to be conducting VIP giveaways on the company's product. The addon store has since taken down the extension to prevent any potential browser cryptomining malware from being distributed in the marketplace. Could you investigate what the 'Discurd Nitro Giveaway' addon does exactly? |
| File | [rev_chromeminer.zip](./files/rev_chromeminer.zip) |

#### Solution

### Breakout

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | easy |
| Description | The CCSS suffered a ransomware attack that compromised the Unique Digital Medical File (EDUS) and the National Prescriptions System for the public pharmacies. They've reported that their infrastructure has been compromised, and they cannot regain access. The APT left their implant interface exposed, though, and you'll need to break into it and find out how it works. NOTE: This challenge is intended to be solved before 'Breakin'. |
| File | - |

#### Solution

### Mr. Abilgate

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | Mr. Abilgate, the CFO of a Fortune 500 company, has reportedly been the victim of a recent spree of ransomware attacks. The behavior of the malware seems consistent with our current APT target's tactics, but the ransom note makes us think it's a targeted attack. We suspect bad faith from corporate espionage gone wrong. Could you investigate? |
| File | [rev_mr_abilgate.zip](./files/rev_mr_abilgate.zip) |

#### Solution

### Breakin

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | Previous state-hacking campaigns from these APT actors indicate that they regularly change cryptographic keys, and we believe this server is being used to coordinate them. If you can discover how the keys are being derived, then we'll be able to decrypt all their past worm communication in the network! NOTE: This challenge is intended to be solved after 'Breakout'. |
| File | - |

#### Solution

### Convoluted Boot

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | hard |
| Description | Some nodes in our data center have been producing unexpected errors and crash for a while now. When analyzing the systems offline, we couldn't find anything wrong with them. After a very throurough investigation, we think we have it nailed down to the netboot server handling the distributions on the PXE network. Can you maybe figure out what is happening? |
| File | [rev_convolutedboot.zip](./files/rev_convolutedboot.zip) |

#### Solution

## Forensics

### Perseverance

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | easy |
| Description | During a recent security assessment of a well-known consulting company, the competent team found some employees' credentials in publicly available breach databases. Thus, they called us to trace down the actions performed by these users. During the investigation, it turned out that one of them had been compromised. Although their security engineers took the necessary steps to remediate and secure the user and the internal infrastructure, the user was getting compromised repeatedly. Narrowing down our investigation to find possible persistence mechanisms, we are confident that the malicious actors use WMI to establish persistence. You are given the WMI repository of the user's workstation. Can you analyze and expose their technique? |
| File | [forensics_perseverance.zip](./files/forensics_perseverance.zip) |

#### Solution

### Lina's Invitation

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | easy |
| Description | A CEO of a startup company reported that he could no longer access his Password Vault. It seems the password has been changed, but he states not to have done so. He reports receiving a birthday invitation to a Paintball party the last week. A few days later, his Italian friend told him that her email had been hacked and never sent out those birthday invites. He fears his lost password might have something to do with that birthday invite. Their SOC team confirmed their assumptions by admitting that this document escaped their attention and did not trigger any alert. Now they want us, ENIGMA, to analyze the provided network capture they took on the day and the document sent via his friends' email. |
| File | [forensics_linas_invitation.zip](./files/forensics_linas_invitation.zip) |

#### Solution

### Rogue

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | SecCorp has reached us about a recent cyber security incident. They are confident that a malicious entity has managed to access a shared folder that stores confidential files. Our threat intel informed us about an active dark web forum where disgruntled employees offer to give access to their employer's internal network for a financial reward. In this forum, one of SecCorp's employees offers to provide access to a low-privileged domain-joined user for 10K in cryptocurrency. Your task is to find out how they managed to gain access to the folder and what corporate secrets did they steal.  |
| File | [forensics_rogue.zip](./files/forensics_rogue.zip) |

#### Solution

### MBCoin

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | We have been actively monitoring the most extensive spear-phishing campaign in recent history for the last two months. This campaign abuses the current crypto market crash to target disappointed crypto owners. A company's SOC team detected and provided us with a malicious email and some network traffic assessed to be associated with a user opening the document. Analyze the supplied files and figure out what happened. |
| File | [forensics_mbcoin.zip](./files/forensics_mbcoin.zip) |

#### Solution

### SquatBot

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | hard |
| Description | An AWS development company that provides full-scale cloud consulting and AWS application development services has recently been compromised. They try to maintain cyber hygiene by applying numerous procedures and safe development practices. To this day, they are unaware of how malware could penetrate their defenses. We have managed to obtain a memory dump and isolate the compromised server. Can you analyze the dump and examine the malware's behavior? |
| File | [forensics_squatbot.zip](./files/forensics_squatbot.zip) |

#### Solution

## Hardware

### State of Emergency

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | A DDoS attack is ongoing against our capital city's water management system. Every facility in this system appears to be infected by malware that rendered the HMI interfaces unusable, thus locking out every system administrator out of the SCADA infrastructure. The incident response team has managed to pinpoint the organization's objective which is to contaminate the public water supply system with toxic chemicals from the water treatment facility. We need to neutralize the threat before it's too late! We have also prepared a brief for you with all the information you might need. |
| File | [hw_state_of_emergency.zip](./files/hw_state_of_emergency.zip) |

#### Solution

## Cloud

### Operator

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | We have located Monkey Business operator blog where they are leaking personal informations. We would like you to break into their system and figure out a way to gain full control. |
| File | - |

#### Solution

### Trade

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | easy |
| Description | With increasing breaches there has been equal increased demand for exploits and compromised hosts. Dark APT group has released an online store to sell such digital equipment. Being part of defense operations can you help disrupting their service ? |
| File | - |

#### Solution

