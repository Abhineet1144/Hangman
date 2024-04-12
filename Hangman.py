import time
import random

wrdsandclue = {"cablecar":"mode of transport", "auditorium":"found in schools", "dragonfly":"an insect", "kangaroo":"an animal",\
"predator":"pc brand"}
wrds = []
agu = "_"
chance = 7
brkn = False
for w in wrdsandclue:
    wrds.append(w)

def space(l, h = None):
    global agu
    
    for s in range(len(l)):
        l[s] += " "
        agu += l[s]
        
        #print(agu)
        #print(s)

wrd = wrds[random.randint(0, len(wrds) - 1)]
clue = wrdsandclue[wrd]
lett = list(wrd)
hidwrd = "_ " * len(wrd)
hwws = "_" * len(wrd)
gss = " "
ag = []
gl = list(hwws)

print("hidden word: ", hidwrd)
print("\nClue:", clue + ". Length: ", len(wrd))
i = 0
while True:
    i += 1
    while gss not in ag:
        if i != 0:
            #print(gl)
            agu = ""
            for j in range(len(gl)):
                gl[j] = gl[j].rstrip()
                #print(gl[j], "gl[j]")
            for s in range(len(gl)):
                
                gl[s] += " "
                agu += gl[s]
                #print(agu)

            print(agu)

        if agu.count("_") == 0:
            print("You Have Found The Word with", 7 - (7 - chance), "chances remaining!!")
            brkn = True
            break
        
        ag.append(gss)
        if not brkn:
            gss = input("\n \nGuess: ")
            gss.lower()
        if gss in ag:
            gss = " "
            ag.remove(" ")
            continue
        else:
            break
    if brkn:
            break
        
    if gss in lett:
        cnt = lett.count(gss)
        if cnt == 1:
            wi = wrd.find(gss)
            gl.pop(wi)
            gl.insert(wi, gss)

        else:
            aci = [wrd.find(gss)]
            wi = wrd.find(gss)
            while cnt != 0:
                
                lett[wi] = "_"
                
                #print(aci)
                cnt = lett.count(gss)
                #print(cnt)
                if cnt != 0:
                    aci.append(lett.index(gss))
                    wi = lett.index(gss)

            for i in aci:
                gl.pop(i)
                gl.insert(i, gss)
    else:
        chance -= 1
        print("Wrong Guess", 7 - (7 - chance), "Remains: ")

    if chance == 6:
        print("""
______________
|            | 
|            |
|
|
|
|
|
|\n""")
    elif chance == 5:
        print("""
______________
|            | 
|            |
|            O
|
|
|
|
|\n""")

    elif chance == 4:
        print("""
______________
|            | 
|            |
|           [O]
|            |
|            |
|            |
|
|\n""")

    elif chance == 3:
        print("""
______________
|            | 
|            |
|           [O]
|           /|
|          / | 
|            |
|
|\n""")
    elif chance == 2:
        print("""
______________
|            | 
|            |
|           [O]
|           /|\\
|          / | \\
|            |
|
|
\n""")
    elif chance == 1:
        print("""
______________
|            | 
|            |
|           [O]
|           /|\\
|          / | \\
|            |
|           /
|          /
\n""")
    elif chance == 0:
        print("""
______________
|            | 
|            |
|           [O]
|           /|\\
|          / | \\
|            |
|           / \\
|          /   \\

YOU ARE HANGED!
the word was: """, wrd)
        break
