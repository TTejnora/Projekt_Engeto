
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
users={'bob':'123','ann':'pass123','mike':'password123','liz':'pass123'}
uzivatel = input('Username :')
if not(uzivatel in users.keys()):
    print('neexistujici uzivatel')
else:
    heslo= input('Password :')
    if heslo == users[uzivatel] :
        cara='-'*40
        print(cara)
        print(f'Welcome to the app, {uzivatel}')
        print(f'We have {len(TEXTS)} texts to be analyzed.')
        print(cara)
        cislo = (input(f'Enter a number btw. 1 and {len(TEXTS)} to select: '))
        if cislo.isnumeric() :
            if (int(cislo) in range(1,len(TEXTS)+1)):
############## HERE IS THE MAIN BODY OF PROGRAM  ################
                textik = TEXTS[int(cislo)-1].split()
                clean_textik = list()
                # cistime slova od znaku
                for slovo in textik:
                    clean_textik.append(slovo.strip(".'\n"))
                # plnime ukoly, vytvorime promenne, ktere pak budeme navysovat
                pocet_istitle = 0
                pocet_isupper = 0
                pocet_islower = 0
                pocet_isdigit = 0
                suma_cisel = 0
                delka_slov = dict()
                for slovo in clean_textik:
                    if slovo.istitle():
                        pocet_istitle += 1
                    if slovo.isupper():
                        pocet_isupper += 1
                    if slovo.islower():
                        pocet_islower += 1
                    if slovo.isdigit():
                        pocet_isdigit += 1
                        suma_cisel += int(slovo)
                    delka_slov.setdefault(len(slovo), 0)
                    delka_slov[len(slovo)] += 1
                #tiskneme
                print(cara)
                print(f'There are {len(clean_textik)} words in the selected text.')
                print(f'There are {pocet_istitle} titlecase words.')
                print(f'There are {pocet_isupper} uppercase words.')
                print(f'There are {pocet_islower} lowercase words.')
                print(f'There are {pocet_isdigit} numeric strings.')
                print(f'The sum of all the numbers is :{suma_cisel}')
                nejdelsi = max(list(delka_slov.keys()))
                maxik = max(list(delka_slov.values()))
                nejdel = str(max(list(delka_slov.keys())))
                d_tit = len('  OCCURENCES  ')
                print(f'LEN|  OCCURENCES  {(maxik-d_tit)*" "}|NR.')
                for i in range(1, (nejdelsi + 1)):
                    delka_slov.setdefault(i, 0)
                    print(f'{(3 - len(str(i))) * " "}{i}|{"*" * delka_slov[i]}{(maxik - delka_slov[i]) * " "}|{delka_slov[i]}')
#############  HERE IS THE END OF MAIN BODY OF PROGRAM  ################
            else:
                print(cara)
                print('Spatne cislo textu')
        else :
            print(cara)
            print(f'Nezadal jsi cislo -{cislo}')
    else:
        print('Spatne heslo')
print(cara)
print('konec vazeni')