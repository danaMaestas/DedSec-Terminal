import os
import time
import csv
os.system("color 0F")

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
        
        
       

art = r"""                                                                              '- ``- '' . - '' - ````'` -`--'' -`- `' - - - '' . - '' - ..-  `(:^*'''`.  !':^  _^:-~*:*/!'__~~='-:   :, ` '  . - `' . -`- '' .```.'`- ` ` '' '''-'.:-''-'.'-'.-''''':'':'
                                                                                        ..-'-'-'':`-'-''``-'-'``'-'-.-'':'-.-''`'-'-.-''-'-`-''.`-'-'``'':>!!'''`  ,.:'  .    -:**:-`      '''.*~' `''.`-'-''`--'-.-'','-.-''``-'-'`''-`--:':::::_-:'::::::'::_::_'
                                                                                        '-.-.------:-.`..-`-``''`.---.`'.-.-`-''-.-.-:'--': `-'.-`-.-''`.!!!*` .- ''''`  '     :!'__         .!,,' `` .-:--`''.`-.-''-'-`-``'.-'-.-''-.-.-.-:::::_-'-_-::-:':_::::'
                                                                                        '`-`-':--'-''''''`--'`''`'-'-'''``'-' `''-._`:,-,!-  `'` '-'`''``*_>*'`-` .!'    -':'..-`--* .--'.   ',-~- `:-~_''-'.' '--`''`'-'-' ''`'-'`''`'`-'''':--'-'-':''-:'''::':-'
                                                                                        '',''::''-'':':'''-:--'''.--'.''-`-.--'.-'''-_'.-''''`'.``'`''''-!=*\,``:':!'    ::/*r!`~^-**=**_.    .-.  '-.:_:,.-'::''.-.''-'.-.''.'-:._''.''':''''''--:':':::_':'_::,':
                                                                                         '--.-'----':_.':_'-'``'` - - '' -  -'-'-'-'-''~-:---- `- - ` '` -_!\, --'!*'    :---:_:'-.~~__-:~    .'  '-'':_'-.-'--_:,- ' -'-:-'''-''--'':_'':'''-''::-'':-'::-'---''-'
                                                                                        ''-.-`-`'-_~~-''-.::':`''--:.`''-.-.-''`--.-:,'--'-'--'`'-'-'`''-'~!!!'-. !*''   `' .\*~,!!:,-'  -    `! -'',,:'':_'':--::_:',:::__::::::_~':___::::_:_:-_:''_::-::''`-::_'
                                                                                        '''-'-''-:-':_-.'-`-':''-.-.-'``'-':-`''-'-''::-'-':'''--`-``''-.-__+*! - !!'^    ! ^.:-,*,-^_- '     '!-= -:`,-'~_:`._:,:_,-:_:::_'::'::,~':'_::_':',:::_:''-_:'::-:-.:::-
                                                                                        '`-'--':-'----`'--'-'-''`--'`''`'--`.``.`-''.'.--'-`-..- -`- ''`-``'~!!'- !!'!'   ' !--*:~**_=_`~  `--~!-_ `'-::''-----:''-''''-':'''`-`--:'''-:::''::'-'-:':-:.''''-'-'':'
                                                                                        '_''--''.----'::':.':'''.-''.'''--'-::.':,_-`'-'-'_'_''_.```-''.-.','!!( '!!:''     !!*:,:':~,:``  --~~'`,`..-,::_''''''':-.'`:'._'''.`:,:':':-__-:':'_:::':'__::'''':::_:'
                                                                                         -''-_:,__'-'--'-'--'''`'`--'`''`'---'``-''''':_--'-------' `''`-.-:*\)!' !!'''     ---.`'`.-^,    _:**+~c- ` `:'--''`-''`-'.`-.--'`''---'''':_':_'-:-:'--:'---''-''-''-'-'
                                                                                        -.-`--:::-'-_:-._`-`-.-'.-'-.-''-.---''-`'--.``:---_-''-.-.-.`'.-'-'/**+'-:  ''                   :~``-_~^`- -:.-.-.':.--':'-:----''-'-.---':----.-.---'---':-::::'-,::::_'
                                                                                        '-.-.-'' .-'-``''-`-'.''-.-'-''`.-'-`.'.-`-`.''-.-':'':'-.-.`''-'-' !***,'''''!''                `,`  -'~ '     .`'`'-:'--:'-::'::::':`_'-''''---`':''`:_:''::,::-'-:__:_::
                                                                                        '`-'. '' - -`' '` -.- '' .`- '' -`. ```` ` ` ''`'`` '. ``- -     '' '!!(^- ',`:''              `,_:,,,'*'^`~' .' - -``.''-:''':'''':'--''::'':-''-:'`.''.'.'''..''''-'-':-'
                                                                                        '.`.'_''.'.`.''''_''`-''.`-'-''' `'.`'''-'` `''```'-''.` '``  ._*!:''**!*!''*)'!!:             :'~~~!*!^',!!*:' .:.- - -`--'':-'-'-'''_':~''':--'-:''':'_:'''_'':'':'_:'_':
                                                                                        `-`'_-'''`-'--'------`''`----  ```--``--'`---''`--'-`''-`-`-''-+=r_' ,!\*\'''\'':~!--         --'-_+=cc===**=!'`-*,'.`'''     -.--:`'--.--:'':_::-'-.-'-:--'-_-'':''-:--:-'
                                                                                        ``-`::-:.---.:-'_:-.-.`'`-.-    -.-..''`~''-'' .-':-```-'-`-''`!!:'' '!'!!''''*'!:,*''       .:-:-!~,>*~!~~~'  .^!'!'--!'!:_!'.--:_:-'_'-::'':_-:::':'---_:-:_'-:---:_:::_:
                                                                                        '-.-''':'..'`':'':'-``''-`-' '' `-'-```'-''''``''-'-''`'-'-'`''!!-    '-~\)`''-!-~!.-      `-'-'-'~+~=:+==_- `__==~~  :(^(!!*!~' '::':','-:.-',:'`':'_:':'_'':_'--''--,:::'
                                                                                        ' . . '''''' ``'` - . '' ` -    ` .`-  . -''`''`- .    ` ` - :+*_.    -^~c+'-``'~-:~+:-*:----`  :==r__=c+=~`-=c=ccc+,'!!!!^!,' ' .''''-''-:''-  ``.'.--''-'''.'''.-'.''''-`
                                                                                        ': `'-''.`''-`.''-````''.`-' '''`-  ` `'-'.`-'':`-`-''.'-'-~=~~!~:' `  ':!*,  -'-~^:_*>-   -`.-_~~:-_~!:--:--!!=!~!+~~,!!!~**'   '-''`_-:--`` -`'-'''-'::_':':-:::''`-'',`'
                                                                                        -'-'`- '--- '`''---`-`'-'-'--`''-`.'-''-'-`-````-`--`   -'!'*~.-:'   ` '*!!!'  '''_!+*+'`''``-~='-_~_,''_!:::''!!!!!!*~*!(r)!,':`---''-'`-.  ```------:-':-:----:--'-'-' -'
                                                                                        -`-`-'`''---.-''-`:`-.`:-_.::`-.-----''-'-`-`` `-`--`-`:~`:*~c\o8ucc-   *'!!:  `:/!-~r+>,-..----':__-:!cccs#o/s,='~!!!!!^r**^</^:--'':--'-.-`-''.'''--_-'''-'_''-```'-'- .-
                                                                                        '-:-'.''``-`-`.''-'-:'-'-'-'~'``'-'-:`''-'- `' ``-` -~=.=)vcosscs8osoo,.'!!*!'` :~!*:-!**,---:---`-_'=sos7sscssos){*.,==^!!!*!\!!-:'':-' `'. '''.''-`:''' ,':-,:'  ''`''-`'
                                                                                        :::.. '' - - - '` ``.'''`-`.'.''``--::'` `   ` :,c7'/o8~s_sncocrcoo8oososT-:^','''-,^,~''----```'-csosusXs8s=cocos_s!soc'sc\*_=*='.''`-`'-'.':`.`'`'.''''''.':- - .'-`'' .'
                                                                                        ':,::-''--`'-`'''-'-'-'':-._~:'`--'--_-'s==ccss(8oovovoXco<o,o~c=s=ossssoss)^!,!~,^.'''`------.-)joosossocccs~s,ssosXs)Xvsos!ssss==s'---':' ''---''''':-'.-''_'''``.`'-''``
                                                                                           '--`'` --``'' ''--'`'`---_'-~**occscoYX#looo/8csss8oooX)scs'':':~~<<XXXsc_*!,:-_=\!~_` --`--_=soXooc`':*\`\TclTXlos8sssco\7oY}8#X8ssc=oc=__ ''--':-:----'----'``-`--' - 
                                                                                         .  ---'`` -.-   ---`'---_~s/o8occsss=oocsssoco8}oss,}sossoo*oo\'!!!r!^,s8oY&8''!\'\,-.- ':. -%&oXss:-.==!:'cso~sssss8v`scsv8ossssscsocccsccs88\==-'':-'`-'-'-'-- `  `'`.-'
                                                                                        .-``-`''`'` -`.''-':_`'*oWs\ss*s8cos\+o8@8s~isossc'c='~ocsos=ocosc!+!***_`:csrc,''!'!!~*,:`- ~ccc*-^:'~~'`/ssss=oooco~'_c'cosooi,78@&s+/sssXosss=s%%*` ''-'''`''`_''.`-'-` 
                                                                                        ''.'..'' ' ` - '` '_^~so)~=so/ocXsoso=#8sooo+X%c-,=ossssY=csovsss'cc=_*:- ``::::'!!'*!*c+c**---__:-,~**~,c'css7o7c+sssssX=~-coX/sosss8/osos%ss=osc=cYs~,.'`' -''.'`'   '.` 
                                                                                            '-`'.`-' `  '`sc<<csc,js+s8ssoccos\7ssoo8+8o,-- `c{s%%8~_co)sYv{',-,~:--:`'---:'!!__:-:'-_-`-:~*___^i7s77os_~soXsYc` --:o8s8s8scY%sossos##scso:=o=s>cc''' -`'    ``-.  
                                                                                          `` ``'' --``',=ov!Xocos=,co#oo\8s8Xs`ss8oo8sssc-c'c,==s\soc~*8c,so*.>!,!:<!':!^^~'!!^,::''````:!*~'_^*o===sr*csY/sc=:c!=`=sso8oooss,LXs8s%oo8sc^~sscoo+soc` -` - '``- - '
                                                                                         -`'`- ''  -`-~_scso\so{)8sc8os\8@&&88vYoocoo8%Y8oc/*,~':.^soo\*oo888 ,,'-:'-''```:'!*~'`.-  -`:!:-:,~,o&soX+/o}s,-:._^c*co8l88os*oss78o%&@&vsYssc8scoscssss~c`   `   ` -  
                                                                                        '---' '  '-'-:v\s/c8ss*soc}o=so{/co888soss~cso8Xcss_=- '-` `~cocssX8c,'----`.  '. __-      ''-:-_:_=~=_ss#sscss_--`.''-'-7ssX8ssc_scss8#8Xc+ooo~Xscsscss8s\Tcv^   `'``-  '`
                                                                                        .``   .. ` ` 'ss\oc*Xoco~c:,_sXsocss&@88o, .>o=%ooos*.  `.`` -_:csso*!'      ' :_`          '':^!=**~*+csssc_:. `   '' :ssos8cYc` ~o88&&8oc#sos~~:==ocs%=co)ss''.      `''.
                                                                                        '-`-        ``sooccocosc\occssc-:c:s8&@X8s-' \ssTscs%!.    .    '=crs!*!'    -'!!'`       .------*!~~::c(s=''''-'-`- ':\s*ocss/-'-s8%@&8s-_/:=ooTco|sTs~ssssos'`      -'```
                                                                                        -`-`-`   `` ` _o~cYs>soccco8s/-'-.---so%8s%-.`'s%Y8Yso+   `...```` '!*!\'     --^\' --''~!*--.,:-:_:,' -.---''`--`-''*o8o8v8s':--8s8X8s_   ` -~o#sss=ss*77s:X_` -``  -`  -'
                                                                                         `-`--  `-  ` ``,osss=s8s!c^: ''-'-`-'o8ssss~ ':*oosooo* -`. ' .-:-.,^::~`     ,*c^-+(=*~~--'''--'''' ```--`'' '-`- *ssssoo~'`-,c8ss88`-`    ` ',*^ssscscso:.` `-    `  - '
                                                                                        ' ``` ''. ` `  `':::-__`- .'-''''`'-`.':o8csX*  `')X%oooc''` ``'''`''.`'-      '':'`^!-:' `''''----`''.`  -`'''`'-'=o8oXX):'' ~X8s88_'-'-`-''`' '- -.c_-_-,  `   -    .' `'
                                                                                        ' - `    ` ``-  ` ` - '' - ` '  ' ` -   `~ssssso-  :,on*s%~ ' ``'''`'' '         ,' `    ` . '' . ` '' -      `''_Xs=oo`,` `sossss:,'` ' . '' - ` '- -     `    ` ''   `   """
# Проверяем, выбран ли другой арт
if os.path.exists("selected_art.txt"):
    with open("selected_art.txt", "r", encoding="utf-8") as file:
        selected_art = file.read().strip()

    if selected_art == "art1" and os.path.exists("art/art1.txt"):
        with open("art/art1.txt", "r", encoding="utf-8") as file:
            art = file.read()
center_text(art)


time.sleep(1)
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

import os

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
        print("change - art")
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
        
    elif command == "art menu":
        print("")
        print("[ ART SELECTOR ]")
        print("")
        print("[1] DEFAULT")
        print("[2] ART 1")
        print("")
        print("change art     - preview ART 1")
        print("select art 1   - use ART 1")
        print("select default - use DEFAULT")
        
    elif command == "change art":
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
        print(art)
        print("save art?")
        
    
    elif command == "save art":
        import os

        os.makedirs("art", exist_ok=True)

        user_file = open("art/art1.txt", "w", encoding="utf-8")
        user_file.write(art)
        user_file.close()

        print("[+] ART 1 SAVED")
       
    elif command == "select art 1":
        user_file = open("selected_art.txt", "w", encoding="utf-8")
        user_file.write("art1")
        user_file.close()

        print("[+] ART 1 SELECTED")
        print("[+] RESTART DEDSEC")
        
        
     
        
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
