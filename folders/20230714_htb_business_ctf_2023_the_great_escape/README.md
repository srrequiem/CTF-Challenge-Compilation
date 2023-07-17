# HTB Business CTF 2023: The Great Escape

## Scada

### Breach

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | Our relentless search led us to a secure testing site, a hub for concocting chemicals used in planet terraforming. Given its critical nature, a unique door system segregates the entire facility, allowing only a single door to open before a decontamination process ensues. Currently, the control sensors seem to be inoperative, keeping the system idle. Intriguingly, someone seems to have hardwired the sensor inputs to the output coils. Perhaps, this might be our entry point into the building. |
| File | [ics_breach.zip](./files/ics_breach.zip) |

#### Solution

### Intrusion

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | easy |
| Description | After gaining access to the enemy's infrastructure, we collected crucial network traffic data from their Modbus network. Our primary objective is to swiftly identify the specific registers containing highly sensitive information and extract that data. |
| File | [ics_intrusion.zip](./files/ics_intrusion.zip) |

#### Solution

### Watch Tower

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | very easy |
| Description | Our infrastructure monitoring system detected some abnormal behavior and initiated a network capture. We need to identify information the intruders collected and altered in the network. |
| File | [ics_watch_tower.zip](./files/ics_watch_tower.zip) |

#### Solution

Verificando la sección de `Reference Number` de los paquetes con función tipo Write Multiple Registers.

> Flag: HTB{m0d8u5_724ff1c_15_un3nc2yp73d!@^}

## Blockchain

### 2244 Elections

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | hard |
| Description | It's the year 2244 and it's Elections time between United Nations of Zenium (UNZ) and Board of Arodor (BoA) to establish the new world order. You, a skilled hacker aligned with the United Nations of Zenium, suspected the presence of a well-concealed backdoor in the e-voting system that could manipulate the outcome of the elections. The source code is not public, but nothing is secret on the block... |
| File | [blockchain_2244_elections.zip](./files/blockchain_2244_elections.zip) |

#### Solution

### Confidentiality

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | The Board of Arodor has implemented a program aimed at providing exclusive access to confidential resources through the use of non-fungible tokens (NFTs). These unique tokens, known as AccessTokens, can only be created by the general secretary or through the utilization of a pre-approved, digitally-signed authorization document endorsed by the general secretary. By acquiring an AccessToken, you gain privileged entry to the board of Arodor's confidential information. Your objective is to obtain one of these highly coveted AccessTokens and gain access to Arodor's the highly confidential documents. |
| File | [blockchain_confidentiality.zip](./files/blockchain_confidentiality.zip) |

#### Solution

### Funds Secured

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | easy |
| Description | In Arodor, a state-of-the-art crowdfunding program fueled groundbreaking research. Powered by a smart contract, the program aimed to raise funds. Overseeing this campaign was a council board, responsible for finalizing the program through a multi-signature wallet scheme. Your goal is to exploit the contract and steal the funds, posing a threat to Arodor's noble scientific mission.. |
| File | [blockchain_funds_secured.zip](./files/blockchain_funds_secured.zip) |

#### Solution

### Paid Contr-actor

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | very easy |
| Description | After a lifetime of preparation, the moment has arrived to enlist in the esteemed military of the United Nations of Zenium as an expert in blockchain security. Before embarking on your duties, there is a small matter of paperwork that requires your attention. |
| File | [blockchain_paid_contr-actor.zip](./files/blockchain_paid_contr-actor.zip) |

#### Solution

## Fullpwn

### Langmon

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | very easy |
| Description | N/A |
| File | - |

#### Solution

### Contempt

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | hard |
| Description | N/A |
| File | - |

#### Solution

### Isotope

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | N/A |
| File | - |

#### Solution

### Chaotic

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | N/A |
| File | - |

#### Solution

### Vanguard

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | easy |
| Description | N/A |
| File | - |

#### Solution

## Cloud

### Emit

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | N/A |
| File | - |

#### Solution

### Unveiled

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | easy |
| Description | N/A |
| File | - |

#### Solution

## Web

### Lazy Ballot

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | very easy |
| Description | As a Zenium State hacker, your mission is to breach Arodor's secure election system, subtly manipulating the results to create political chaos and destabilize their government, ultimately giving Zenium State an advantage in the global power struggle. |
| File | [web_lazy_ballot.zip](./files/web_lazy_ballot.zip) |

#### Solution

### Watersnake

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | easy |
| Description | As the United Nations of Zenium and the Board of Arodor engage in a fierce competition to establish a colony on Mars using Vitalium. State hackers from UNZ identify an exposed instance of the critical facility water management software, Watersnakev3, in one of Arodor's main water treatment plants. The objective is to gain control over the water supply, and weaken the Arodor's infrastructure. |
| File | [web_watersnake.zip](./files/web_watersnake.zip) |

#### Solution

### Desynth Recruit

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | The Commonwealth of Arodor Maximus has seized control of the No #1 Desynth Recruit Agency and is currently employing it against the United Nations of Zenium. They are now attempting to recruit a significant number of bots for their war efforts. We require your assistance in safeguarding the agency and thwarting the sinister plans of Arodor Maximus. |
| File | [web_desynth_recruit.zip](./files/web_desynth_recruit.zip) |

#### Solution

### Polaris Control

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | During the Dark War, the Zenium State, facing resource scarcity, sought to hack into Arodor's notorious malware command and control system, Polaris Control, to gain an advantage in the Mars space race. State hackers have contacted you claiming to have spotted a small programming error by performing tedious enumeration, can you help them escalate it? |
| File | [web_polaris_control.zip](./files/web_polaris_control.zip) |

#### Solution

### Redwave

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | hard |
| Description | The Commonwealth of Arodor Maximus has deployed a satellite broadcast system to exert control over their forces. You have successfully infiltrated their internal network. Are you capable of hacking into the broadcasting service and exposing their secret plans? |
| File | [web_redwave.zip](./files/web_redwave.zip) |

#### Solution

## Pwn

### Snow Scan

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | very easy |
| Description | In a rapidly unfolding scenario, an ancient Sumerian virus has surfaced, rapidly proliferating and posing a grave threat. Snow Crash, a menacing presence within the metaverse, has ventured beyond virtual realms, unleashing tangible repercussions in real life. In response to this crisis, the Board of Arodor has devised a vital tool—a service designed to meticulously scan and identify potential samples of Snow Crash. Would you consider harnessing this service to counter their efforts? |
| File | [pwn_snowscan.zip](./files/pwn_snowscan.zip) |

#### Solution

### Device Control

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | easy |
| Description | You managed to successfully breach the enemy's device control server! With this accomplishment, you now possess a significant opportunity: to either mislead them through the creation of counterfeit devices or to delve deeper into the system and exploit it for complete system access. Choosing the former path allows you to manipulate their perceptions, potentially leading them astray and buying valuable time. However, should you opt for the latter, you can uncover hidden vulnerabilities and harness the system to your advantage, potentially neutralizing the enemy's capabilities entirely. The choice is yours |
| File | [pwn_device_control.zip](./files/pwn_device_control.zip) |

#### Solution

### Hackback

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | A critical breakthrough has occurred in our ongoing battle on the cyber front. Through an invaluable informant, we have obtained exclusive access to the enemy's Command and Control (C2) service, along with its complete source code. This unprecedented advantage demands immediate action to exploit weaknesses within their C2 infrastructure, effectively disrupt their operations, and secure a decisive advantage in this conflict. |
| File | [pwn_hackback.zip](./files/pwn_hackback.zip) |

#### Solution

### Sonic Infiltrator

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | Embark on a paramount mission as you tap into the formidable potential of the Martian Sound Kernel, a pivotal asset in the intense race for resources and dominion. Seize the opportunity to exploit vulnerabilities, deftly maneuver through treacherous cyber terrain, and unlock enigmatic auditory secrets that hold the key to securing an upper hand in this relentless struggle for survival. As the ultimate cyber warrior, your actions may shape the very fate of nations in this war-ravaged world. Are you prepared to rise to the challenge and emerge triumphant? |
| File | [pwn_sonic_infiltrator.zip](./files/pwn_sonic_infiltrator.zip) |

#### Solution

### PAC Breaker

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | hard |
| Description | Welcome to Operation PACbreaker, where your skills as a highly trained operative from the United Nations of Zenium are crucial. Your mission is of utmost importance: infiltrate the oppressive surveillance system maintained by the Board of Arodor and bypass their formidable Persistent Access Control (PAC) mechanisms. By leveraging your expertise, you must navigate their intricate defenses, uncover their hidden agendas, gather vital intelligence, and ultimately secure the survival of the democratic colony. The United Nations of Zenium places its trust in your abilities. Are you prepared to embrace the challenge and liberate the colony from the shackles of control? |
| File | [pwn_pac_breaker.zip](./files/pwn_pac_breaker.zip) |

#### Solution

## Crypto

### I'm gRoot

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | easy |
| Description | After decrypting the communication, you uncover the identity of the mole as the senior blockchain developer. Shockingly, the developer had embedded a backdoor in the government's decentralized blockchain network, originally designed to prevent corruption. You report this critical finding to the government council and are assigned with the task of detecting and fixing the backdoor, ensuring the integrity and security of the network. |
| File | [crypto_im_groot.zip](./files/crypto_im_groot.zip) |

#### Solution

### PRaNsomG

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | Following the mole's dismissal, the nation suffered from an onslaught of relentless phishing campaigns. With little time to spare during this chaotic and tense period, warnings and safeguards for staff members were inadequate. A few individuals fell victim to the phishing attempts, leading to the encryption of sensitive documents by ransomware. You were assigned the mission of reverse engineering the ransomware and ultimately recovering the classified files, restoring order and safeguarding the nation's sensitive information. |
| File | [crypto_pransomg.zip](./files/crypto_pransomg.zip) |

#### Solution

### Interception

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | In the midst of escalating conflict between the nations of Luson and Oumara, a recent invasion by Oumara has sparked suspicions about the existence of an internal communication channel. Fearing further strikes, the Luson government takes proactive measures to counter Oumara's attacks. You were assigned the task of investigating their secure channel and determining whether you can obtain any sensitive information. Eventually, you gain access to the channel and even manage to send encrypted messages of your own. Can you reveal Oumara's secret plans to safeguard your nation from potential future invasions? |
| File | [crypto_interception.zip](./files/crypto_interception.zip) |

#### Solution

### Vitrium Stash

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | hard |
| Description | As the war comes to an end, your contributions in safeguarding your nation from cyberattacks and uncovering enemy plans have been significant. However, your mission is not yet complete. While enumerating the enemy government's infrastructure, you discover an old signing panel rumored to contain crucial information regarding valuable resources' locations. Your final objective is to successfully bypass this signing panel and expose the whereabouts of these assets. |
| File | [crypto_vitrium_stash.zip](./files/crypto_vitrium_stash.zip) |

#### Solution

### Initialization

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | very easy |
| Description | During a cyber security audit of your government's infrastructure, you discover log entries showing traffic directed towards an IP address within the enemy territory of "Oumara". This alarming revelation triggers suspicion of a mole within Lusons' government. Determined to unveil the truth, you analyze the encryption scheme with the goal of breaking it and decrypting the suspicious communication. Your objective is to extract vital information and gather intelligence, ultimately protecting your nation from potential threats. |
| File | [crypto_initialization.zip](./files/crypto_initialization.zip) |

#### Solution

## Reversing

### DrillingPlatform

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | very easy |
| Description | Welcome to the latest and greatest in Vitralium mining technology. Our newest rig can penetrate depths never before reached! Unfortunately, we haven't yet been able to locate any. Can you get into the workings of the machine and find out where we need to drill? |
| File | [rev_drillingplatform.zip](./files/rev_drillingplatform.zip) |

#### Solution

### Intelligence Service

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | easy |
| Description | We've received some powerful intelligence gathering software from intercepting Arodor communications. Unfortunately, it requires a license key. Can you try and crack the keychecker? |
| File | [rev_intelligence_service.zip](./files/rev_intelligence_service.zip) |

#### Solution

### SEPC

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | We've extracted an embedded operating system running on an intercepted deep-space satellitle launched by Arodor. If we can breach the secure enclave and extract their security mechanisms, we can crack their encrypted communications |
| File | [rev_sepc.zip](./files/rev_sepc.zip) |

#### Solution

### LicenseGenerator

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | insane |
| Description | Arodor has been distributing promotional license keys to users across the world. We suspect that there could be some backdoor in this 'special gift' - can you investigate? |
| File | [rev_license_generator.zip](./files/rev_license_generator.zip) |

#### Solution

### Cobalt COBOL

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | hard |
| Description | When intercepting a delivery towards a quite old Asteroid Cobalt Mining Facility we got our hands on a stack of punch cards, it looks like these are some kind of code update? Since the last COBOL programmer died over a century ago we hoped that maybe you can analyze this ancient relic. |
| File | [rev_cobaltcobol.zip](./files/rev_cobaltcobol.zip) |

#### Solution

## Forensics

### Red Miners

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | very easy |
| Description | In the race for Vitalium on Mars, the villainous Board of Arodor resorted to desperate measures, needing funds for their mining attempts. They devised a botnet specifically crafted to mine cryptocurrency covertly. We stumbled upon a sample of Arodor's miner's installer on our server. Recognizing the gravity of the situation, we launched a thorough investigation. With you as its leader, you need to unravel the inner workings of the installation mechanism. The discovery served as a turning point, revealing the extent of Arodor's desperation. However, the battle for Vitalium continued, urging us to remain vigilant and adapt our cyber defences to counter future threats. |
| File | [forensics_red_miners.zip](./files/forensics_red_miners.zip) |

#### Solution

### Scripts and Formulas

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | easy |
| Description | After the last site UNZ used to rely on for the majority of Vitalium mining ran dry, the UNZ hired a local geologist to examine possible sites that were used in the past for secondary mining operations. However, after finishing the examinations, and the geologist was ready to hand in his reports, he mysteriously went missing! After months, a mysterious invoice regarding his examinations was brought up to the Department. Being new to the job, the clerk wasn't aware of the past situation and opened the Invoice. Now all of a sudden, the Arodor faction is really close to taking the lead on Vitalium mining! Given some Logs from the Clerk's Computer and the Invoice, pinpoint the intrusion methods used and how the Arodor faction gained access! To get the flag you need to answer the questions from the docker instance. |
| File | [forensics_scripts_and_formulas.zip](./files/forensics_scripts_and_formulas.zip) |

#### Solution

### Hypercraft

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | This email seems to have come from one of our agents, Axel Knight, but Axel has been missing for weeks, and we believe him to be compromised. The email claims to have information that could be vital to our winning this war, but before we use it, we want to make sure it is safe to open. Analyze the given email and see if it's real, or if it's just the Arodorians trying to phish us, and find the flag. |
| File | [forensics_hypercraft.zip](./files/forensics_hypercraft.zip) |

#### Solution

### No Start Where

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | hard |
| Description | As echoes of the Dark War lingered in UNZ's cyber-warfare HQ, a beacon blinked ominously. An analyst turned a wary eye to the screen. The alarm signal originated from the main system that controls the mining machinery! It was an attack from the Board of Arodor, aimed at crippling the mining infrastructure. Initial investigation of the network traffic revealed that the system has been compromised! Your task is to disinfect the system by uncovering the infiltration method and potential post-exploitation steps! |
| File | [forensics_no_start_where.zip](./files/forensics_no_start_where.zip) |

#### Solution

### Project Redline

#### Stats

| Attribute | Info |
|---|---|
| Difficulty | medium |
| Description | In the aftermath of a mysterious death in the United Nations of Zenium colony on Mars, during the Autopsy, the doctor uncovers a peculiar secret. Traces of a cyber attack are discovered on the victim's cybernetic implants, pointing to a covert infiltration by the Board of Arodor. Determined to reveal the truth, the doctor joins forces with a cyber forensics expert, tracing the attack's origins. As they delve deeper, they uncover a startling revelation. In the implant factory, a worker examined what they thought was leaked footage from Arodors cyber implant research. Unbeknownst to him, the intel was infected with malware, infecting the whole production line. Now, they must race against time to expose cybercriminals and prevent Mars's fragile peace from shattering again. |
| File | [forensics_project_redline.zip](./files/forensics_project_redline.zip) |

#### Solution

