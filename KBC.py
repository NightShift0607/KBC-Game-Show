# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 22:56:36 2023

@author: Rajat Gupta
"""
def rules():
    print("\n                        !!! WELCOME TO KAUN BANEGA CROREPATI !!!")
    print("""\n              YOU WILL GET 5 QUESTION AND EACH QUESTION WILL HAVE 4 OPTIONS.
              WITH EACH CORRECT ANSWER YOU WILL GET INCREMENT OF 10 LAKHS,
              YOUR FIRST QUESTION WILL BE OF 10 LAKHS AND LAST WOULD BE OF
              50 LAKHS. BUT, IF YOUR ANSWER IS WRONG YOU WILL LOSE ALL THE
              MONEY. HOWEVER, YOU CAN ANSWER (QUIT) AT ANY QUESTION YOU LIKE AND YOU
              WILL GET THE MONEY TILL THE LAST RIGHT ANSWER.""")
    print("\n HOPE YOU UNDERSTAND THE RULES OF THE GAME, THEN LETS START KAUN BANUGA CROREPATI \n")

def question(q):
    ques = ["WHO IS THE FIRST PRESIDENT OF INDEPENDENT INDIA ?\n","WHO IS THE FIRST PRIME MINISTER OF INDEPENDENT INDIA ?\n","WHO DISCOVERED FARADAY CAGE ?\n","WHO WROTE THE BOOK PRIDE AND PREJUDICE ?\n","WHICH INDIAN CAPTAIN WON ICC TOURNAMENT IN ALL 3 FORMATS ?\n"]
    if q == 1 :
        print(ques[0])
        print("""A. DR APJ ABDUL KALAM                       B. DR RAJENDER PRASAD
C. PT JAWARAHAR LAL NEHRU                   D. SARDAR VALLABHAI PATEL\n""")
    elif q == 2 :
        print(ques[1])
        print("""A. NARENDRA MODI                            B. MANMOHAN SINGH
C. PT JAWARAHAR LAL NEHRU                   D. INDIRA GANDHI\n""")
    elif q == 3 :
        print(ques[2])
        print("""A. NIKOLA TESLA                    B. MICHAEL FARADAY
C. THOMAS EDISON                   D. ALBERT EINSTEIN\n""")
    elif q == 4 :
        print(ques[3])
        print("""A. WILLIAM SHAKESPEARE              B. JK ROWLING
C. VIRGINIA WOOLF                   D. JANE AUSTEN\n""")
    elif q == 5 :
        print(ques[4])
        print("""A. MS DHONI                         B. KAPIL DEV
C. SUNIL GAVASKAR                   D. RAHUL DRAVID \n""")

def chkans(a):
    ans = str(input("GIVE YOUR OPTION: "))
    if a == 1 and ans == 'B' :
        return True
    elif a == 2 and ans == 'C' :
        return True
    elif a == 3 and ans == 'A' :
        return True
    elif a == 4 and ans == 'D' :
        return True
    elif a == 5 and ans == 'A' :
        return True
    elif ans.upper() == "QUIT" :
        return False

def rtwr(f1):
    if f1 == True :
        print("\nCONGRATULATION !!! CORRECT ANSWER !!!\n")
        return 'T'
    elif f1 == False :
        print(announcer(6))
        return 'Q'
    else :
        print("\nI AM SORRY, ITS A WRONG ANSWER, BETTER LUCK NEXT TIME\n")
        return 'F'

def announcer(x):
    announce = ["\nYOUR FIRST QUESTION FOR 10 LAKHS IS AS FOLLOWS","\nYOUR NEXT QUESTION FOR","IS AS FOLLOWS","\nALRIGHT THEN THE GAME ENDS HERE"]
    if x == 1 :
        print(announce[0],"\n")
    elif x == 2 :
        print(announce[1],"20 LAKHS",announce[2],"\n")
    elif x == 3 :
        print(announce[1],"30 LAKHS",announce[2],"\n")
    elif x == 4 :
        print(announce[1],"40 LAKHS",announce[2],"\n")
    elif x == 5 :
        print(announce[1],"50 LAKHS",announce[2],"\n")
    elif x == 6 :
        print(announce[3])

def game():
    rules()
    i = 1
    while True :
        announcer(i)
        question(i)
        f=chkans(i)
        res = rtwr(f)
        if res == 'T' :
            i=i+1
            if i == 6 :
                print(f"CONGRATULATION YOU HAVE WON {(i-1)*10} LAKHS, THANK YOU FOR PLAYING KBC")
                break
        elif res == 'Q' :
            print(f"YOU HAVE WON {(i-1)*10} LAKHS, THANK YOU FOR PLAYING KBC")
            break
        elif res == 'F'  :
            break

name = input("Enter Your Name: ")
name = name.upper()
a=input(f"\nAre YOU READY TO START KBC {name} !!! (Yes/No): ")
if a.lower() == "no" :
    print("\nTAKE ALL YOUR TIME AND WHEN YOU ARE READY, RESTART THE GAME")
else:
    game()