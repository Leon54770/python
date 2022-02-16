"""
Beispiel 1
Der String Zeile besteht aus allem möglichen aber nicht aus Zahlen
er soll mit dem Befehl sub aus dem import re zu einer Folge von Ziffern
gewandelt werden.
"""
import re
zeile =  '934257 18 66 7 0 1 99 6'

print(zeile)
zeile = re.sub('[^0-9]', '', zeile)
print(zeile)
zeile_orig = zeile
print (zeile[8])

summe = 0
for i in range(0, len(zeile) -1):
    #print (zeile[i])
    if (i % 2 == 0):
        #Quersumme bilden falls der Wert groesser 10
        if (2 * int(zeile[i]) > 9):
            temp = 2 * int(zeile[i])
            temp_char = str(temp)
            summe += int(temp_char[0]) + int(temp_char[1])
        else:
            summe += 2 * int(zeile[i])
    else:
        summe += int(zeile[i])

print ("Die Summe ist ", summe)

subtraent = summe % 10
print (subtraent)



print ("Die Ziffer ist " , 10 - subtraent, "und die ist identisch mit ", zeile[len(zeile)-1])




