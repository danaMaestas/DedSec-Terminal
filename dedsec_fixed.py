import os
import csv
import random
import time
import sys
glitch_running = False
os.system("color 0F")


GLITCH_CHARS = "@#$%&/\\|=+<>:;*?"


def make_glitch_frame(art, intensity=0.025):
    result = []

    for line in art.splitlines():
        new_line = ""

        for char in line:
            if char != " " and random.random() < intensity:
                new_line += random.choice(GLITCH_CHARS)
            else:
                new_line += char

        result.append(new_line)

    return "\n".join(result)




    for _ in range(12):
        os.system("cls")
        print(make_glitch_frame(art, intensity=0.035))
        time.sleep(0.06)

    os.system("cls")
    print(art)
    time.sleep(0.3)    

def play_intro(art):
    print(art)

def print_centered_block(block):
    terminal_width = os.get_terminal_size().columns

    lines = block.splitlines()

    if not lines:
        return

    block_width = max(len(line) for line in lines)
    padding = max(0, (terminal_width - block_width) // 2)

    for line in lines:
        print(" " * padding + line)    

  
 
def play_death_intro():
    for i in range(1, 10):
        path = os.path.join("animation", f"{i}.txt")

        with open(path, "r", encoding="utf-8") as file:
            frame = file.read()

        os.system("cls")
        print_centered_block(frame)
        time.sleep(0.18)

    os.system("cls")
def center_text(text):
    width = os.get_terminal_size().columns
    for line in text.splitlines():
        print(line.center(width))

def center_type_text(text, speed=0.04):
    width = os.get_terminal_size().columns
    spaces = (width - len(text)) // 2

    print(" " * spaces, end="")

    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(speed)

    print()
art = r"""          
                                                                                                                                                                             ,,:,,,,::,::::,:,,:::,:,:.:.'      -               - ` --css8&&8s=        
                                                                                                                                                                         `   .,,::::::,,:,:,::::::,',,::`:.      `       -     .``-.`:====c:-----` --..-
                                                                                                                                                                         ` `.:,:,::':::,.::':::''::',,,,^`...`-        -=sss,.::::::,,,:::::,:,::::::'::
                                                                                                                                                                          `  `:''::,':,,~_~,,,,::-__~~=_,':-.':,,.:::::::'-.-`.,:,:::'',:..-:',::,'::`':,
                                                                                                                                                                            .,:::::',,:,,,:,'::':::.-:-=~s`':::,'`,,,,:::::,::.-,:_=ccccc=c`:,::.:::.':,
                                                                                                                                                                            ,.:':,:,::~s~=::::,:',:',,:-':>s==,,~_=ccc===cssssssssssssssss\~`=====**,`_~
                                                                                                                                                                            .,:::::,,,:8\88&s:-```-:,,,:,::`:~=ssssssssss=ss=ss=_=~::^,::,:==_=s=cs==-::,
                                                                                                                                                                           .,  =``:^- ,s8&>* '- -`<``:,::::::::::::.:,:::`-.``::`:_:,,:::,::',::,-  -,:_
                                                                                                                                                                            `. ^8sc=-c8j%X@8``-:c8&@c .:..--.--::::``::,,,:.`:.::``,,,,::,::':.,..::::,:
                                                                                                                                                                            -`.s===8@@/c\@@@=cs/_s,`--.,.--.:_:_:::::::::_:````::-.::_::,-,-.,:_::_:,:_
                                                                                                                                                                               -.-\!:(&&s&s8sss'.--...--:,__:::__:~::::::::::::` `:. :,:,-..,.,:_,:::,   
                                                                                                                                                                         -csss@`cccs#8sssc======c__,:::,:,:,::::::-:,,,,,:``..-`'`:`:::::::_:~_==cccc_-`
                                                                                                                                                                   `,ccsss88ssscc::------:::___===ss=s=ss_-:::::,:,.`:::::.`-.::``.:<cc=sscccc==c,__: -`
                                                                                                                                                       .,.`---:s#s88oscssc-'-------.-----------.:,=~~~:=ss=sss=_::,,.`:,:--' -..,'.%,   `.::,^,_~~~~_'-.
                                                                                                                                             `- s~``:...--``-___:cc::::::,,:::--:::::,',:::,:,,,:,,,=s=======sss=sss===csssss===sc,,: ,,-.:~~,:..:~\:--
                                                                                                                                       :c=~`-`-T\`=c'.,,::-`::::,::.--`.:-``:::,:::.:.::::::::,'.`..--::,::=s========s=sscc:,,:` .ccccc,    `::`   ```:-
                                                                                                                                    -<c8<<vc*oM^c (c ,,:::: .:,::::`-:`.``',:-:::_:::_`::::,,:::::,'::`--:,,,:::_=s==s==s==ssssss<,.:,,       ---`     -
                                                                                                                                  -,o<s,,/7@|osc'- \``_,:,`,:_,,:::,:-::::-`::::,_:,:::,:``:_:_:::::,:::::,_,,::,::::,`-:`.::::::..:,.           ..-`   
                                                                                                                                c88!s&%~s!88/,X-:/ --.::::::::,::ccccssssssss=sss===cccc=====_:::::::,:::_:,,:::::.:....:..:,-,:::':.`               ```
                                                                                                                               -sc<!=*/@(s8ccs,   - -ccssssssssssscccc_:-,c=c_:=s==cs=sc====c==ss=s===s=~~::::::::,:,,:.::`,,:::,:..:                   
                                                                                                                        `--:cs8@@8,8:/s8~os/,.-:csssscc::::``::::~^~~:::::`::::`-:,::_:_==s=====s==ss=ssss=====s=ss=======-~>~-:,::`:'    - ` -         
                                                                                                                      co&&@@@@@@8ssM'(8<,%sccscc_:::::::,:,.  .:::,,::,:,,:`:::,::`.:::,.-:,,:,,:`:,::_cc==ss=ssssssssssss=csss=sc=s=_`'-.-'`',         
                                                                                                              ``--s+\`X@@@@@@8s<<&<=#&sscs,`..,::,---`    ..:,,::,:,,,:,-.' ``-`:::,`-`::::`-::::,:::::,:,,,,,,:,:-,.,_,:,.',::.::``..                  
                                                                                                            -=s`\&\\``~>&8scc=-sc,  `-    .::,:          .,:::,:,:,,`             `..-.`.-`::`..-``.`:::,::::::.,,:,,,:::::'::::::,:.^'     `           
                                                                                                       `,cs8@@@X~W\o<`--'scs_-_- `       `.-----_:________:=*~^~,:'.                           -    ``--`---.'::,:,,::,:'::'',,:,.::,:``                
                                                                                             -,ccs8#s=8@@@@@@@@@ssscss=______=_=___==_c__=sc=____-_------:-:__=cccssc_:=_c_:--. '`               ....::.-.`..,:,',,,!!:,'',:.::::::,!'.``               
                                                                                           .)<8@@@@@@@@@@@@8cc:-           --`____-----_:-_==:-------:-_--------  `-                           '.  -`-`.`::`.`::,,:::,:,''::.',::,::'':.`               
                                                                            -              '!s@@@@@@@@@@@8-                                  -.-``                  :`                         .:`` `-```-`..-`---.-.::,::::,.`::::::,:.::`             
                                                                            so=====_ss=====s%@@@@@@@@@@@@<                           -   `  `  `-`:.              ` ```             `         .:``:`. ` ` -`-`::::::`.``.:::,::`:::,,^:::,.          `  
                                                                             `=s=@&&8s8=@@@@@@@@@@8&s@@@@&s``    `          `                     -`--``-             ::.                    `,::.`:.`-```` :``-`-`::,::`--:,,::,:::,^:::.         `    
                                                                                 `s&@@@s888@@@@@@@@@s8s8@@@@===-                     `               ``-_:-:-`        `-`.                  -   `^::`--```-````:--`-`::::_.`::__:__:::::::`-`-          
                                                                                   `=8@@@@8s8=s=@@@@@@@==s===@=8,--         -      `                     `---::`         .:```              ::`-..-  `::.-`.``.``-:::`-`:::-``-::.--.  -`. -```-   `    
                                                                                      `=s8sss=ss8s=sssssss88s==ss=@=s=~-                                      `-``       `-.:-:..:.        ,,__:.---.``-'-:::````--`:::_..'::,-              ```:. :`.--
                                                                                          -_==s@@@@@s8&ss@@@@@@@==s=ss&&s=`        `   `             `                                -  .::::,:::::-`.`` .,.,:_:=c=c=c=sc_~~~~~--`         `     `.--::
                                                                                               -_===&@@@@8ss===&ss888o_=c:ss8s=_                                   ..-                  ,:::,:,,_:~~=:____--::,~~-_--::~<ccc==:=scs=ccc=_____.- .       
                                                                                                    -_==sss&==ss==s=@@@@&=s==sss&===sc==`--             ---:__c==s=s=ssc=======_-     .::::,::~,,~:::::,:~_~:___----`` :.-``',,.---_`_--__________-----.
                                                                                                    `---~===s&=&@@===&&s&&=s==8s==s=ss=====s=_=======ss=====:=_:-.-._-.--___=___=_==c=ssssssss====csc=cc____=cc~c:_:~- `..`.:.,,`.,::..                 
                                                                                                            `  `_=s==&@&===ss===@&ss==-`.=ss===_-  ````--```                  --_==c=s=ssssss=s==ss=sssssssc==____:_:,`....``---.:`-`--  -````          
                                                                                                                     `-_=====@=============__===s=====_-                          `.:::,:,:,,:::::::,,::,_,:,::::.`-.::::::::,::,::::,:.`            .-`
                                                                                                                             --=====&@@===8ssss===___==========_---               .:,_*c=s~=*cs~:~_^~,cccc,c~~~::::,,,:_::::,,,:,::::::_:^.`-        ``-"""   
        
       
       
play_death_intro()
play_intro(art)

center_type_text("[+] INITIALIZING DEDSEC...")
time.sleep(0.5)

center_type_text("[+] LOADING MODULES...")
time.sleep(0.5)

center_type_text("[+] ESTABLISHING CONNECTION...")
time.sleep(0.5)

center_type_text("[+] ACCESS GRANTED.", 0.08)

alias = "dana_maestas"

print("")
print("by dana_maestas")
print("Welcome, " + alias + ".")
print("System started.")
print("")



if not os.path.exists("user.txt"):
    user_file = open("user.txt", "w", encoding="utf-8")
    user_file.write("dana_maestas")
    user_file.close()

user_file = open("user.txt", "r", encoding="utf-8")
username = user_file.read().strip()
user_file.close()








while True:
    command = input("DEDSEC > ").lower()
  
    if command == "help":
        print("Available commands:")
        print("help - command list")
        print("about - information")
        print("clear - clear screen")
        print("exit - exit")
        print("johnny - chat")
        print("setname - change username")
        print("showname - show current username")
        print("dedsec//scan")


         
    elif command.startswith("scan"):
        print("DEDSEC // SCAN")
        print("[+] Scanning running processes...")

        import subprocess

        result = subprocess.run(
            ["tasklist", "/FO", "CSV", "/NH"],
            capture_output=True,
            text=True,
            encoding="cp866",
            errors="ignore"
    )

        lines = result.stdout.splitlines()

        print("[+] PROCESS SCAN COMPLETE")
        print(f"[+] FOUND: {len(lines)} PROCESSES")
        print("-" * 60)

        reader = csv.reader(lines)

        processes = []

        for row in reader:
            name = row[0]
            pid = row[1]
            memory_text = row[4]

            memory_number = (
                memory_text
                .replace("КБ", "")
                .replace("KB", "")
                .replace("\xa0", "")
                .replace(" ", "")
           )

            if memory_number.isdigit():
                memory_kb = int(memory_number)
            else:
                memory_kb = 0

            processes.append((name, pid, memory_kb))

        processes.sort(key=lambda process: process[2], reverse=True)

        print("[+] TOP RAM PROCESSES")
        print("-" * 60)

        for name, pid, memory_kb in processes[:10]:
            memory_mb = memory_kb / 1024

            print(
                f"[PROC] {name:<25} "
                f"PID: {pid:<8} "
                f"RAM: {memory_mb:.1f} MB"
        
            )
        parts = command.split(maxsplit=1)
        
        if len(parts) == 1:
            print("[+] TOP 10 RAM PROCESSES")
            print("-" * 60)

            for name, pid, memory_kb in processes[:10]:
                memory_mb = memory_kb / 1024
                print(f"[PROC] {name:<25} PID: {pid:<8} RAM: {memory_mb:.1f} MB")

        elif parts[1] == "all":
            print("[+] ALL PROCESSES")
            print("-" * 60)

            for name, pid, memory_kb in processes:
                memory_mb = memory_kb / 1024
                print(f"[PROC] {name:<25} PID: {pid:<8} RAM: {memory_mb:.1f} MB")
                
        elif parts[1] == "net":
            print("DEDSEC // NETWORK SCAN")
            print("[+] Scanning active network connections...")
            print("-" * 80)

            net_result = subprocess.run(
                ["netstat", "-ano"],
                capture_output=True,
                text=True,
                encoding="cp866",
                errors="ignore"
            )

            net_lines = net_result.stdout.splitlines()

            for line in net_lines:
                line = line.strip()

                if line.startswith("TCP"):
                    columns = line.split()

                    if len(columns) >= 5:
                        protocol = columns[0]
                        local_address = columns[1]
                        remote_address = columns[2]
                        state = columns[3]
                        pid = columns[4]

                    if state == "ESTABLISHED":
                        print(
                            f"[NET] {protocol:<5} "
                            f"PID: {pid:<7} "
                            f"STATE: {state}"
                        )
                        print(f"      LOCAL:  {local_address}")
                        print(f"      REMOTE: {remote_address}")
                        print("-" * 80)
        else:
            search_name = parts[1]

            print(f"[+] SEARCHING FOR: {search_name}")
            print("-" * 60)

            found = False

            for name, pid, memory_kb in processes:
                if search_name in name.lower():
                    memory_mb = memory_kb / 1024
                    print(f"[FOUND] {name:<25} PID: {pid:<8} RAM: {memory_mb:.1f} MB")
                    found = True

            if not found:
                print("[!] PROCESS NOT FOUND")

            print("-" * 60)  
     
      


      
    elif command == "about":
        print("DEDSEC TERMINAL v0.1")
        print("Created by " + alias + ".")
        print("johnny:online")
        print("setname") 
        
    elif command == "setname":
        username = input("enter username: ")
        
        user_file = open("user.txt", "w")
        user_file.write(username)
        user_file.close()
    
    elif command == "showname":
        print(username)   
     
        
    
    
        
    elif command == "clear":
        import os
        os.system("cls")

    elif command == "exit":
        print("Connection closed.")
        break
        
    elif command == "johnny":
        print("JOHNNY: Я здесь, dana_maestas.")
        
    
        
    
       
    
        
        
     
        
    else:
        print("Unknown command: " + command)
        print("Type 'help' for available commands.")
while True:
    message = input("dana_maestas > ")

    if message.lower() == "привет":
        print("JOHNNY: Привет, dana_maestas.")

    elif message.lower() == "как дела":
        print("JOHNNY: Лучше не бывает.")

    elif message.lower() == "exit":
        print("JOHNNY: Ещё увидимся.")
        break

    else:
        print("DEDSEC: Type 'help' for available commands..")
