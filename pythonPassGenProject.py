import string
import random
def main():
    
    num = string.digits
    let = string.ascii_uppercase
    randChar = ["!","@","$","%","^","&","*","(",")","_","+","}","{","/","?",">",".",","]
    randpass = ""

    def randpas():
        nonlocal randpass
        while len(randpass)<16:
            ran = random.randint(1,3)
            if ran == 1:
                r = random.randint(0,9)
                randpass+= num[r]

            elif ran == 2:
                c = random.randint(0,25)
                randpass+= let[c]

            elif ran == 3:
                d = random.randint(0,len(randChar)-1)
                randpass+= randChar[d]

        print("your password is " + randpass)
        
    randpas()
main()
