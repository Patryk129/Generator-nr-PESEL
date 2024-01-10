flaga = True
while(flaga == True):
    dzien = input('Podaj dzien np01')
    if(len(dzien)==2 and int(dzien)<= 31):
        miesiac =input('Podaj miesiac np01')
        if(len(miesiac)==2 and int(miesiac)<= 12):
            rok = str(input('Podaj rok'))
            if(len(rok)==4):
                plec = input("Podaj plec M lub K")
                if(plec == "M" or plec == "K"):
                    flaga = False
i = 0
j = 0
k = 0
l = 0
pesel = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    for j in range(10):
        for k in range(10):
                for l in range(10):
                    pesel[0] = rok[2]
                    pesel[1] = rok[3]
                    if int(rok)>=2000:
                        pesel[2] = str(int(miesiac[0]))
                    elif int(rok)>1900 and int(rok)<2000:
                        pesel[2] = str(int(miesiac[0]))
                    else:
                        pesel[2] = str(int(miesiac[0])+8)
                    pesel[3] = miesiac[1]
                    pesel[4] = dzien[0]
                    pesel[5] = dzien[1]
                    pesel[6] = str(i)
                    pesel[7] = str(j)
                    pesel[8] = str(k)
                    if plec == "K":
                        if l%2==0:
                            pesel[9] = str(l)#kobieta0
                    else:
                        if l%2!=0:
                            pesel[9] = str(l)#mezczyzna=1
                    w = 1*int(pesel[0])+3*int(pesel[1])+7*int(pesel[2]) + 9*int(pesel[3])+1*int(pesel[4]) + 3*int(pesel[5]) + 7*int(pesel[6]) + 9*int(pesel[7])+ 1*int(pesel[8]) + 3*int(pesel[9])
                    w = str(w)
                    w = int(w[len(w)-1])
                    k2= 10-w
                    pesel[10] = str(k2)
                    print(pesel)
