Space = " "
Zero = "نۆل"
One = "بىر"
Two = "ئىككى"
Thr = "ئۈچ"
For = "تۆت"
Fiv = "بەش" 
Six = "ئالتە"
Sev = "يەتتە"
Eig = "سەككىز"
Nin = "توققۇز"
Ten = "ئون"
Yigr = "يىگىرمە"
Otuz = "ئوتتۇز"
Qirq = "قىرىق"
Alik = "ئەللىك"
Atmx = "ئاتمىش"
Yatm = "يەتمىش"
Saks = "سەكسەن"
Toqs = "توقسان"
Yuz = "يۈز"
Ming = "مىڭ"
Mill = "مىليون"
Mily = "مىليارد"
Tril = "تىرىللىيون"
Quwa = "كىۋادرىللىيون"
Kiwn = "كىۋىنتىللىيون"
Siks = "سېكستىللىيون"
Sept = "سېپتىللىيون"
Octl = "ئوكتىللىيون"
Nont = "نونىللىيون"
Dets = "دېتسىللىيون"
Unds = "ئۇندېتسىللىيون"
Duod = "دۇئودېتسىللىيون"
Trid = "تىرىدېتسىللىيون"
Kwat = "كىۋاتتوردېتسىللىيون"
Kwit = "كىۋىندېتسىللىيون"

BaseNum = ["نۆل","بىر","ئىككى","ئۈچ","تۆت","بەش","ئالتە","يەتتە","سەككىز","توققۇز"]
TensNum = ["**","ئون","يىگىرمە","ئوتتۇز","قىرىق","ئەللىك","ئاتمىش","يەتمىش","سەكسەن","توقسان","يۈز"]
MillNum = ["مىڭ","مىليون","مىليارد","تىرىللىيون","كىۋادرىللىيون","كىۋىنتىللىيون","سېكستىللىيون","سېپتىللىيون","ئوكتىللىيون",\
           "نونىللىيون","دېتسىللىيون","ئۇندېتسىللىيون","دۇئودېتسىللىيون","تىرىدېتسىللىيون","كىۋاتتوردېتسىللىيون","كىۋىندېتسىللىيون"]

def Red(San):
    Br = San%10
    San = San//10
    On = San%10
    Yz = San//10
    Temp = ""
    if Yz != 0:
        Temp = BaseNum[Yz]+Space+Yuz+Space
    if On != 0:
        Temp = Temp + TensNum[On] + Space
    if Br != 0:
        Temp = Temp + BaseNum[Br]
    return Temp

Num = int(input())
Asl = Num
Len = len(str(Num))
Ans = ""
if Len==1:
    Ans = BaseNum[Num]
else:
    cnt = 0
    while(Len > 1 or (Len == 1 and Num > 0)):
        Par = Num%1000
        Num = Num//1000
        cnt = cnt + 1
        Swap = Red(Par)
        if cnt > 1:
           Swap = Swap+Space+MillNum[cnt-2]+Space
        Ans = Swap +Ans
        Swap = ""
        Len = len(str(Num))
print(Asl)
print(Ans)

'''
f = open("ans.txt","w+",encoding = "UTF-8")
f.write(str(Asl))
f.write('\n')
f.write(Ans)
f.close()
''
