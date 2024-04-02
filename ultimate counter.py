import random
import time
class counting:
    # Characters
    class Characters:
        def Letter_counter():
            print ("_______________________")
            print ("Letter counter selected")
            print ("WARNING: Very short strings may error.")
            answer = input("Text:")
            print ("Are there any characters you want it to not count?")
            letters_ignored = []
            letter_list = []
            option2 = ""
            count = 0
            # it can't be blank
            if answer == "":
                print ("\nAnswer cannot be blank.")
                counting.Characters.Letter_counter()
            while True:
                if option2 in ["no", "n"]:
                    break
                option = input("[Y]es/[N]o:").strip().lower()
                if option in ["y", "yes", "ya"]:
                    while True:
                        print ("Please type character you want program to ignore:")
                        option2 = input()
                        if option2 == "":
                            print ("\nAnswer cannot be blank.")
                            continue
                        letters_ignored.append(option2)
                        print ("Any more letters you want to ignore?")
                        while True:
                            option2 = input("[Y]es/[N]o:").strip().lower()
                            if option2 in ["y", "yes", "ya"]:
                                c = 1
                                break
                            elif option2 in ["n", "no", "na"]:
                                c = 0
                                break
                            else:
                                print ("\nOption not recognized, restarting")
                                continue
                        if c == 1:
                            continue
                        else:
                            break
                elif option in ["n", "no", "na"]:
                    break
                else:
                    print ("\nOption not recognized, restarting")
                    continue
            for i in letters_ignored:
                if answer == i:
                    print ("\nOption not recognized, restarting")
                    counting.Characters.Letter_counter()
            for i in answer:
                letter_list.append(i)
            for i in letter_list:
                if i in letters_ignored:
                    letter_list.remove(i)
            option2 = len(letter_list) - 1
            option = letter_list[0]
            while count < option2:
                option += (letter_list[count + 1])
                count += 1

            print ("String with ignored characters:     ", answer)
            print ("Length including characters:        ", len(answer))
            print ("String without ignored characters:  ", option)
            print ("Length ignoring characters:         ", len(option))
            input("Enter to continue")
            counting.Start()
        def Word_counter():
            print ("_____________________")
            print ("Word counter selected")
            print ("WARNING: Very short strings may error.")
            option = input("Text:")
            count = 0
            print ("_____________________")
            print ("For double separator, simply type two of sign.\nSeparator can be anything.")
            seps = []
            words = 0
            c = 1
            if option == "":
                print ("\nAnswer cannot be blank.")
                counting.Characters.Word_counter()
            while True:
                separator = input("Separator:")
                if separator == "":
                    print ("\nAnswer cannot be blank.")
                    continue
                seps.append(separator)
                print ("Are there any more separators you want it to not count?")
                while True:
                    option2 = input("(Y/N):").strip().lower()
                    if option2 in ["y", "yes", "ya"]:
                        c = 1
                        break
                    elif option2 in ["n", "no", "na"]:
                        c = 0
                        break
                    else:
                        print ("n\nOption not recognized, restarting")
                        continue
                if c == 1:
                    continue
                else:
                    break
                break
            while count <len(seps):
                words += (option.count(seps[count]) + 1)
                count += 1
            if words == 1:
                print ("There is ", str(words), " word in\n\"", option, "\"", sep="")
            else:
                print ("There are ", str(words), " words in\n\"", option, "\"", sep="")
            input("Enter to continue")
            counting.Start()
        def Sentence_counter():
            print ("_________________________")
            print ("Sentence counter selected")
            print ("NOTE: According to Microsoft,\nsentences only have one space\nafter them in double spacing.")
            option = input("Text:")
            if option == "":
                print ("\nAnswer cannot be blank.")
                counting.Characters.Sentence_counter()
            answer = option.count(". ")
            if list(option)[-1].isspace() is False:
                answer += 1
            if answer == 1:
                print ("There is ", answer, " sentence in\n\"", option, "\"", sep="")
            else:
                print ("There are ", answer, " sentences in\n\"", option, "\"", sep="")
            input("Enter to continue")
            counting.Start()
    class Numbers:
        def Speed_adder():
            print ("____________________")
            print ("Speed adder selected")
            while True:
                option = input("Please enter number to count to:")
                if option == "":
                    print ("\nAnswer cannot be blank.")
                    counting.Numbers.Speed_adder()
                print ("Time to wait in seconds, decimals allowed.")
                time_wait = input("How long to wait between each:")
                if time_wait == "":
                    print ("\nAnswer cannot be blank.")
                    continue
                try:
                    option = int(option)
                    time_wait = float(time_wait)
                except:
                    print ("\nOption not recognized, restarting")
                    continue
                else:
                    break
            a = 0
            print ("Do you want it to start a line line each time?")
            while True:
                line = input("(Y/N):").strip().lower()
                if line in ["y", "yes", "ya"]:
                    line = 1
                    break
                elif line in ["n", "no" , "na"]:
                    line = 0
                    break
                else:
                    print ("\nOption not recognized, restarting")
                    continue
            while a < option:
                a += 1
                if line == 1:
                    print (a)
                else:
                    if a  < option:
                        print (a, end=", ")
                    else:
                        print (a)
                time.sleep(time_wait)
            input("Enter to continue")
            counting.Start()
        def Digit_counter():
            print ("______________________")
            print ("Digit counter selected")
            print ("No spaces.")
            print ("No decimals.")
            while True:
                answer = input("Please input digits to count:").strip()
                if answer == "":
                    print ("\nAnswer cannot be bank")
                    continue
                try:
                    answer = int(answer)
                except:
                    print ("\nOption not recognized, restarting")
                    continue
                else:
                    break
            answer = str(answer)
            print ("Are there any digits you want it to not count?")
            letters_ignored = [" "]
            letter_list = []
            option2 = ""
            count = 0
            c = 0
            while True:
                if option2 in ["n", "no", "na"]:
                    break
                option = input("[Y]es/[N]o:").strip().lower()
                if option == "":
                    print ("\nAnswer cannot be bank")
                    continue
                if option in ["y", "yes", "ya"]:
                    while True:
                        print ("Please type digit you want program to ignore:")
                        option2 = input()
                        if option == "":
                            print ("\nAnswer cannot be bank")
                            continue
                        letters_ignored.append(option2)
                        print ("Any more letters you want to ignore?")
                        while True:
                            option2 = input("[Y]es/[N]o:").strip().lower()
                            if option2 in ["y", "yes", "ya"]:
                                c = 1
                                break
                            elif option2 in ["n", "no", "na"]:
                                c = 0
                                break
                            else:
                                print ("\nOption not recognized, restarting")
                                continue
                        if c == 1:
                            continue
                        else:
                            break
                elif option in ["n", "no", "na"]:
                    break
                else:
                    print ("\nOption not recognized, restarting")
                    continue
            letter_list = list(answer)
            for i in letter_list:
                if i in letters_ignored:
                    letter_list.remove(i)
            option2 = len(letter_list) - 1
            option = letter_list[0]
            while count < option2:
                option += (letter_list[count + 1])
                count += 1

            print ("String with ignored digits:     ", answer)
            print ("Length including digits:        ", len(answer))
            print ("String without ignored digits:  ", option)
            print ("Length ignoring digits:         ", len(option))
            input("Enter to continue")
            counting.Start()
        def Digit_scrambler():
            print ("________________________")
            print ("Digit scrambler selected")
            print ("No decimals.")
            while True:
                option = input("Digits:")
                if option == "":
                    print ("\nAnswer cannot be bank")
                    continue
                try:
                    option = int(option)
                except:
                    print ("\nOption not recognized, restarting")
                    continue
                else:
                    break
            option2 = list(str(option))
            option3 = []
            var = 0
            while len(option2) - 1 > -1:
                var = random.randrange(0, len(option2), 1)
                option3.insert(0, option2[var])
                option2.pop(var)
                continue
            answer = "".join(option3)
            print ("Digits:\n      ", answer)
            input("Enter to continue")
            counting.Start()
        def Digit_reverser():
            print ("_______________________")
            print ("Digit reverser selected")
            print ("No spaces")
            print ("No periods")
            while True:
                option = input("Digits:")
                if option == "":
                        print ("\nAnswer cannot be bank")
                        counting.Other.Letter_reverser()
                try:
                    option = int(option)
                except:
                    print ("\nOption not recognized, restarting")
                    continue
                else:
                    break
            option = str(option)
            a = list(option)
            b = []
            for i in a:
                b.insert(0, i)
            answer = "".join(b)
            print ("Digits:\n      ", answer)
            input("Enter to continue")
            counting.Start()
    class Calculator:
        def Addition(): 
            print ("_________________")
            print ("Addition selected")
            print ("Decimals allowed.")
            while True:
                a = input("Number 1:")
                if a == "":
                    print ("\nAnswer cannot be bank")
                    continue
                try:
                    a = float(a)
                except:
                    print ("\nOption not recognized, restarting")
                    continue
                else:
                    break
            while True:
                b = input("Number 2:")
                if b == "":
                    print ("\nAnswer cannot be bank")
                    continue
                try:
                    b = float(b)
                except:
                    print ("\nOption not recognized, restarting")
                    continue
                else:
                    break
            print (a, " + ", b, " =\n", a + b, sep="")
            input("Enter to continue")
            counting.Start()
        def Subtraction():
            print ("____________________")
            print ("Subtraction selected")
            print ("Decimals allowed.")
            while True:
                a = input("Number 1:")
                if a == "":
                    print ("\nAnswer cannot be bank")
                    continue
                try:
                    a = float(a)
                except:
                    print ("\nOption not recognized, restarting")
                    continue
                else:
                    break
            while True:
                b = input("Number 2:")
                if b == "":
                    print ("\nAnswer cannot be bank")
                    continue
                try:
                    b = float(b)
                except:
                    print ("\nOption not recognized, restarting")
                    continue
                else:
                    break
            print (a, " - ", b, " =\n", a - b, sep="")
            input("Enter to continue")
            counting.Start()
        def Multiplication():
            print ("_______________________")
            print ("Multiplication selected")
            print ("Decimals allowed.")
            while True:
                a = input("Number 1:")
                if a == "":
                    print ("\nAnswer cannot be bank")
                    continue
                try:
                    a = float(a)
                except:
                    print ("\nOption not recognized, restarting")
                    continue
                else:
                    break
            while True:
                b = input("Number 2:")
                if b == "":
                    print ("\nAnswer cannot be bank")
                    continue
                try:
                    b = float(b)
                except:
                    print ("\nOption not recognized, restarting")
                    continue
                else:
                    break
            print (a, " * ", b, " =\n", a * b, sep="")
            input("Enter to continue")
            counting.Start()
        def Division():
            print ("_________________")
            print ("Division selected")
            print ("Decimals allowed.")
            while True:
                a = input("Number 1:")
                if a == "":
                    print ("\nAnswer cannot be bank")
                    continue
                try:
                    a = float(a)
                except:
                    print ("\nOption not recognized, restarting")
                    continue
                else:
                    break
            while True:
                b = input("Number 2:")
                if b == "":
                    print ("\nAnswer cannot be bank")
                    continue
                try:
                    b = float(b)
                except:
                    print ("\nOption not recognized, restarting")
                    continue
                else:
                    break
            print (a, " / ", b, " =\n", a / b, sep="")
            input("Enter to continue")
            counting.Start()
        def Remainder_Division():
            print ("___________________________")
            print ("Remainder division selected")
            print ("Decimals allowed.")
            while True:
                a = input("Number 1:")
                if a == "":
                    print ("\nAnswer cannot be bank")
                    continue
                try:
                    a = float(a)
                except:
                    print ("\nOption not recognized, restarting")
                    continue
                else:
                    break
            while True:
                b = input("Number 2:")
                if b == "":
                    print ("\nAnswer cannot be bank")
                    continue
                try:
                    b = float(b)
                except:
                    print ("\nOption not recognized, restarting")
                    continue
                else:
                    break
            print (a, " / ", b, " =\n", a//b, " R:",a % b, sep="")
            input("Enter to continue")
            counting.Start()
        def Exponent():
            print ("_________________")
            print ("Exponent selected")
            print ("Decimals allowed.")
            while True:
                a = input("Number 1:")
                if a == "":
                    print ("\nAnswer cannot be bank")
                    continue
                try:
                    a = float(a)
                except:
                    print ("\nOption not recognized, restarting")
                    continue
                else:
                    break
            while True:
                b = input("Number 2:")
                if b == "":
                    print ("\nAnswer cannot be bank")
                    continue
                try:
                    b = float(b)
                except:
                    print ("\nOption not recognized, restarting")
                    continue
                else:
                    break
            print (a, " ^ ", b, " =\n", a**b, sep="")
            input("Enter to continue")
            counting.Start()
        def Advanced(text):
            if text == 0:
                print ("____________________________")
                print ("Advanced calculator selected")
                print ("Experimental! May break.")
                print ("NO PROMISES IF IT ERRORS FOR NO REASON.")
                print ("NOTE: Does not work with variables... yet.")
                print ("If an error appears when running, hit up arrow in terminal your using to reload command.")
                print ("Decimals allowed.")
                print ("Key:", "\"()\" mean parenthesis", "\"^\" mean exponent", "\"*\" means multiplication", "\"/\" means division", "\"+\" means addition", "\"-\" means subtraction", sep="\n  ")
            elif text == 1:
                print ("____________________________")
                print ("Type \"HELP!\" in option to pull up help.")
            option = input("Equation to solve:").strip()
            if option == "HELP!":
                print ("Experimental! May break.")
                print ("NO PROMISES IF IT ERRORS FOR NO REASON.")
                print ("NOTE: Does not work with variables... yet.")
                print ("If an error appears when running, hit up arrow in terminal your using to reload command.")
                print ("Decimals allowed.")
                print ("Key:", "\"()\" mean parenthesis", "\"^\" mean exponent", "\"*\" means multiplication", "\"/\" means division", "\"+\" means addition", "\"-\" means subtraction", sep="\n  ")
                option = input("Equation to solve:").strip()
            if option == "":
                print ("\nAnswer cannot be bank")
                counting.Calculator.Advanced(2)
            option2 = list(option)
            count = -1
            c = True
            while count < len(option2) - 1:
                if c is True:
                    count += 1
                    c = False
                elif c is False:
                    c = True
                if option2[count] == " ":
                    option2.pop(count)
                    count -= 1
                    continue
                elif option2[count].isdigit() is True:
                    if count + 1 > len(option2) - 1:
                        continue
                    elif option2[count + 1] == "(":
                        option2.insert(count + 1, "*")
                        count += 1
                    else:
                        continue
                elif option2[count] in ["(", ")", "*", "/", "+", "-"]:
                    continue
                elif option2[count] == "^":
                    option2.pop(count)
                    option2.insert(count, "**")
                elif str(option2[count]).isalpha() is True:
                    print ("\nOption not recognized, restarting")
                    counting.Calculator.Advanced(1)
                else:
                    continue
            answer = "".join(option2)
            answer = eval(str(answer))
            print (option, " =\n", answer, sep="")
            input("Enter to continue")
            counting.Start()
    class Other():
        def Word_repeater():
            print ("______________________")
            print ("Word repeater selected")
            while True:
                option = input("How many times to repeat word?")
                if option == "":
                    print ("\nAnswer cannot be bank")
                    continue
                try:
                    option = int(option)
                except:
                    print ("\nOption not recognized, restarting")
                    continue
                else:
                    break
            while True:
                word = input("what is word to repeat?").strip()
                if word == "":
                    print ("\nAnswer cannot be bank")
                    continue
                else:
                    break
            print ("Time to wait in seconds, decimals allowed.")
            while True:
                time_wait = input("How long to wait between each:")
                if time_wait == "":
                    print ("\nAnswer cannot be bank")
                    continue
                try:
                    time_wait = float(time_wait)
                except:
                    print ("\nOption not recognized, restarting")
                    continue
                else:
                    break
            print ("Do you want it to start a line line each time?")
            while True:
                line = input("(Y/N):").strip().lower()
                if line in ["ya", "yes",'y']:
                    line = 1
                    break
                elif line in ["na", "n", "no"]:
                    line = 0
                    break
                else:
                    print ("\nOption not recognized, restarting")
                    continue
            a = 0
            while a < option:
                a += 1
                if line == 1:
                    print (word)
                else:
                    if a  < option:
                        print (word, end=", ")
                    else:
                        print (word)
                time.sleep(time_wait)
            input("Enter to continue")
            counting.Start()
        def Letter_counter_WEIRD():
            print ("_______________________________________")
            print ("Letter counter - WEIRD EDITION selected")
            print ("Alphabet and Numbers only, capitalized and uncapitalized.")
            print ("If some of them aren't alpha and num, I have no idea what it'll say.")
            print ("Once the program has begun, \033[4mthere is no ending it until completion.\033[0m")
            print ("I'm not responsible if the program is used to create words it shouldn't.")
            print ("\nTechnically can also be used as a timer!")
            option = input("Text:")
            if option == "":
                    print ("\nAnswer cannot be bank")
                    counting.Other.Letter_counter_WEIRD()
            while True:
                time_wait = input("How long to wait between each:")
                if time_wait == "":
                    print ("\nAnswer cannot be bank")
                    continue
                try:
                    time_wait = float(time_wait)
                except:
                    print ("\nOption not recognized, restarting")
                    continue
                else:
                    break
            option2 = list(option)
            count = -1
            count2 = -1
            letters_left = 0
            while count < len(option2) - 1:
                count += 1
                count2 = 0
                if option2[count] == " ":
                    letters_left = 0
                elif option2[count] == "0":
                    letters_left = 61
                elif option2[count] == "1":
                    letters_left = 60
                elif option2[count] == "2":
                    letters_left = 59
                elif option2[count] == "3":
                    letters_left = 58
                elif option2[count] == "4":
                    letters_left = 57
                elif option2[count] == "5":
                    letters_left = 56
                elif option2[count] == "6":
                    letters_left = 55
                elif option2[count] == "7":
                    letters_left = 54
                elif option2[count] == "8":
                    letters_left = 53
                elif option2[count] == "9":
                    letters_left = 52
                # lowercase letters
                elif option2[count] == "a":
                    letters_left = 51
                elif option2[count] == "b":
                    letters_left = 50
                elif option2[count] == "c":
                    letters_left = 49
                elif option2[count] == "d":
                    letters_left = 48
                elif option2[count] == "e":
                    letters_left = 47
                elif option2[count] == "f":
                    letters_left = 46
                elif option2[count] == "g":
                    letters_left = 45
                elif option2[count] == "h":
                    letters_left = 44
                elif option2[count] == "i":
                    letters_left = 43
                elif option2[count] == "j":
                    letters_left = 42
                elif option2[count] == "k":
                    letters_left = 41
                elif option2[count] == "l":
                    letters_left = 40
                elif option2[count] == "m":
                    letters_left = 39
                elif option2[count] == "n":
                    letters_left = 38
                elif option2[count] == "o":
                    letters_left = 37
                elif option2[count] == "p":
                    letters_left = 36
                elif option2[count] == "q":
                    letters_left = 35
                elif option2[count] == "r":
                    letters_left = 34
                elif option2[count] == "s":
                    letters_left = 33
                elif option2[count] == "t":
                    letters_left = 32
                elif option2[count] == "u":
                    letters_left = 31
                elif option2[count] == "v":
                    letters_left = 30
                elif option2[count] == "w":
                    letters_left = 29
                elif option2[count] == "x":
                    letters_left = 28
                elif option2[count] == "y":
                    letters_left = 27
                elif option2[count] == "z":
                    letters_left = 26
                # uppercase letters
                elif option2[count] == "A":
                    letters_left = 25
                elif option2[count] == "B":
                    letters_left = 24
                elif option2[count] == "C":
                    letters_left = 23
                elif option2[count] == "D":
                    letters_left = 22
                elif option2[count] == "E":
                    letters_left = 21
                elif option2[count] == "F":
                    letters_left = 20
                elif option2[count] == "G":
                    letters_left = 19
                elif option2[count] == "H":
                    letters_left = 18
                elif option2[count] == "I":
                    letters_left = 17
                elif option2[count] == "J":
                    letters_left = 16
                elif option2[count] == "K":
                    letters_left = 15
                elif option2[count] == "L":
                    letters_left = 14
                elif option2[count] == "M":
                    letters_left = 13
                elif option2[count] == "N":
                    letters_left = 12
                elif option2[count] == "O":
                    letters_left = 11
                elif option2[count] == "P":
                    letters_left = 10
                elif option2[count] == "Q":
                    letters_left = 9
                elif option2[count] == "R":
                    letters_left = 8
                elif option2[count] == "S":
                    letters_left = 7
                elif option2[count] == "T":
                    letters_left = 6
                elif option2[count] == "U":
                    letters_left = 5
                elif option2[count] == "V":
                    letters_left = 4
                elif option2[count] == "W":
                    letters_left = 3
                elif option2[count] == "X":
                    letters_left = 2
                elif option2[count] == "Y":
                    letters_left = 1
                elif option2[count] == "Z":
                    letters_left = 0
                
                while count2 < letters_left:
                    # numbers
                    print ("".join(option2))
                    count2 += 1
                    time.sleep(time_wait)
                    if option2[count] == "0":
                        option2.pop(count)
                        option2.insert(count, "1")
                        continue
                    elif option2[count] == "1":
                        option2.pop(count)
                        option2.insert(count, "2")
                        continue
                    elif option2[count] == "2":
                        option2.pop(count)
                        option2.insert(count, "3")
                        continue
                    elif option2[count] == "3":
                        option2.pop(count)
                        option2.insert(count, "4")
                        continue
                    elif option2[count] == "4":
                        option2.pop(count)
                        option2.insert(count, "5")
                        continue
                    elif option2[count] == "5":
                        option2.pop(count)
                        option2.insert(count, "6")
                        continue
                    elif option2[count] == "6":
                        option2.pop(count)
                        option2.insert(count, "7")
                        continue
                    elif option2[count] == "7":
                        option2.pop(count)
                        option2.insert(count, "8")
                        continue
                    elif option2[count] == "8":
                        option2.pop(count)
                        option2.insert(count, "9")
                        continue
                    elif option2[count] == "9":
                        option2.pop(count)
                        option2.insert(count, "a")
                        continue
                    # lowercase letters
                    elif option2[count] == "a":
                        option2.pop(count)
                        option2.insert(count, "b")
                        continue
                    elif option2[count] == "b":
                        option2.pop(count)
                        option2.insert(count, "c")
                        continue
                    elif option2[count] == "c":
                        option2.pop(count)
                        option2.insert(count, "d")
                        continue
                    elif option2[count] == "d":
                        option2.pop(count)
                        option2.insert(count, "e")
                        continue
                    elif option2[count] == "e":
                        option2.pop(count)
                        option2.insert(count, "f")
                        continue
                    elif option2[count] == "f":
                        option2.pop(count)
                        option2.insert(count, "g")
                        continue
                    elif option2[count] == "g":
                        option2.pop(count)
                        option2.insert(count, "h")
                        continue
                    elif option2[count] == "h":
                        option2.pop(count)
                        option2.insert(count, "i")
                        continue
                    elif option2[count] == "i":
                        option2.pop(count)
                        option2.insert(count, "j")
                        continue
                    elif option2[count] == "j":
                        option2.pop(count)
                        option2.insert(count, "k")
                        continue
                    elif option2[count] == "k":
                        option2.pop(count)
                        option2.insert(count, "l")
                        continue
                    elif option2[count] == "l":
                        option2.pop(count)
                        option2.insert(count, "m")
                        continue
                    elif option2[count] == "m":
                        option2.pop(count)
                        option2.insert(count, "n")
                        continue
                    elif option2[count] == "n":
                        option2.pop(count)
                        option2.insert(count, "o")
                        continue
                    elif option2[count] == "o":
                        option2.pop(count)
                        option2.insert(count, "p")
                        continue
                    elif option2[count] == "p":
                        option2.pop(count)
                        option2.insert(count, "q")
                        continue
                    elif option2[count] == "q":
                        option2.pop(count)
                        option2.insert(count, "r")
                        continue
                    elif option2[count] == "r":
                        option2.pop(count)
                        option2.insert(count, "s")
                        continue
                    elif option2[count] == "s":
                        option2.pop(count)
                        option2.insert(count, "t")
                        continue
                    elif option2[count] == "t":
                        option2.pop(count)
                        option2.insert(count, "u")
                        continue
                    elif option2[count] == "u":
                        option2.pop(count)
                        option2.insert(count, "v")
                        continue
                    elif option2[count] == "v":
                        option2.pop(count)
                        option2.insert(count, "w")
                        continue
                    elif option2[count] == "w":
                        option2.pop(count)
                        option2.insert(count, "x")
                        continue
                    elif option2[count] == "x":
                        option2.pop(count)
                        option2.insert(count, "y")
                        continue
                    elif option2[count] == "y":
                        option2.pop(count)
                        option2.insert(count, "z")
                        continue
                    elif option2[count] == "z":
                        option2.pop(count)
                        option2.insert(count, "A")
                        continue
                    # uppercase letters
                    elif option2[count] == "A":
                        option2.pop(count)
                        option2.insert(count, "B")
                        continue
                    elif option2[count] == "B":
                        option2.pop(count)
                        option2.insert(count, "C")
                        continue
                    elif option2[count] == "C":
                        option2.pop(count)
                        option2.insert(count, "D")
                        continue
                    elif option2[count] == "D":
                        option2.pop(count)
                        option2.insert(count, "E")
                        continue
                    elif option2[count] == "E":
                        option2.pop(count)
                        option2.insert(count, "F")
                        continue
                    elif option2[count] == "F":
                        option2.pop(count)
                        option2.insert(count, "G")
                        continue
                    elif option2[count] == "G":
                        option2.pop(count)
                        option2.insert(count, "H")
                        continue
                    elif option2[count] == "H":
                        option2.pop(count)
                        option2.insert(count, "I")
                        continue
                    elif option2[count] == "I":
                        option2.pop(count)
                        option2.insert(count, "J")
                        continue
                    elif option2[count] == "J":
                        option2.pop(count)
                        option2.insert(count, "K")
                        continue
                    elif option2[count] == "K":
                        option2.pop(count)
                        option2.insert(count, "L")
                        continue
                    elif option2[count] == "L":
                        option2.pop(count)
                        option2.insert(count, "M")
                        continue
                    elif option2[count] == "M":
                        option2.pop(count)
                        option2.insert(count, "N")
                        continue
                    elif option2[count] == "N":
                        option2.pop(count)
                        option2.insert(count, "O")
                        continue
                    elif option2[count] == "O":
                        option2.pop(count)
                        option2.insert(count, "P")
                        continue
                    elif option2[count] == "P":
                        option2.pop(count)
                        option2.insert(count, "Q")
                        continue
                    elif option2[count] == "Q":
                        option2.pop(count)
                        option2.insert(count, "R")
                        continue
                    elif option2[count] == "R":
                        option2.pop(count)
                        option2.insert(count, "S")
                        continue
                    elif option2[count] == "S":
                        option2.pop(count)
                        option2.insert(count, "T")
                        continue
                    elif option2[count] == "T":
                        option2.pop(count)
                        option2.insert(count, "U")
                        continue
                    elif option2[count] == "U":
                        option2.pop(count)
                        option2.insert(count, "V")
                        continue
                    elif option2[count] == "V":
                        option2.pop(count)
                        option2.insert(count, "W")
                        continue
                    elif option2[count] == "W":
                        option2.pop(count)
                        option2.insert(count, "X")
                        continue
                    elif option2[count] == "X":
                        option2.pop(count)
                        option2.insert(count, "Y")
                        continue
                    elif option2[count] == "Y":
                        option2.pop(count)
                        option2.insert(count, "Z")
                        letters_left = 0
                    print ("".join(option2))
            input("Enter to continue")
            counting.Start()
        def Letter_scrambler():
            print ("_________________________")
            print ("Letter scrambler selected")
            option = input("Text:")
            if option == "":
                    print ("\nAnswer cannot be bank")
                    counting.Other.Letter_scrambler()
            option2 = list(option)
            option3 = []
            var = 0
            while len(option2) - 1 > 0:
                var = random.randrange(0, len(option2) - 1, 1)
                option3.insert(0, option2[var])
                option2.pop(var)
                continue
            answer = "".join(option3)
            print ("Text:\n    ", answer)
            input("Enter to continue")
            counting.Start()
        def Letter_reverser():
            print ("________________________")
            print ("Letter reverser selected")
            option = input("Text:")
            if option == "":
                    print ("\nAnswer cannot be bank")
                    counting.Other.Letter_reverser()
            a = list(option)
            b = []
            for i in a:
                b.insert(0, i)
            answer = "".join(b)
            print ("Text:\n    ", answer)
            input("Enter to continue")
            counting.Start()
        def Palindrome_detector():
            print ("____________________________")
            print ("Palindrome detector selected")
            option = input("Text:")
            if option == "":
                    print ("\nAnswer cannot be bank")
                    counting.Other.Palindrome_detector()
            archive = option
            print ("Do you want to count spaces?")
            while True:
                spaces = input("(Y/N):")
                if spaces in ["y", "yes", "ya"]:
                    spaces = 1
                    break
                elif spaces in ["n", "no", "na"]:
                    spaces = 0
                    break
                else:
                    print ("\nOption not recognized, restarting")
                    continue
            print ("Do you want to count capitalization?")
            while True:
                capitalize = input("(Y/N):")
                if capitalize in ["y", "yes", "ya"]:
                    capitalize = 0
                    break
                elif capitalize in ["n", "no", "na"]:
                    option = option.lower()
                    break
                else:
                    print ("\nOption not recognized, restarting")
                    continue
            option2 = list(option)
            option3 = []
            if spaces == 1:
                option3 = option2
            else:
                for i in option2:
                    if i == " ":
                        continue
                    else:
                        option3.append(i)
            x = 0
            while x < ((len(option3) - 1) / 2):
                if option3[x] == option3[((x * -1) - 1)]:
                    x += 1
                else:
                    print ("\"" + archive + "\"", "is not a Palindrome.")
                    input("Enter to continue")
                    counting.Start()
            print ("\"" + archive + "\"", "is a Palindrome.")
            input("Enter to continue")
            counting.Start()
    def Start():
        # text
        print ("\n\033[4m\033[1mOptions:\033[0m")
        print ("\033[1m    Characters:\033[0m", "\033[4m|Letter counter                          (Lc)\033[0m", "\033[4m|Word counter                            (Wc)\033[0m", "\033[4m|Sentence counter                        (Sc)\033[0m", sep="\n      ") # Characters
        print ("\033[1m    Numbers:\033[0m", "\033[4m|Speed adder                             (Sd)\033[0m", "\033[4m|Digit counter                           (Dc)\033[0m", "\033[4m|Digit scrambler                         (Ds)\033[0m", "\033[4m|Digit reverser                          (Dr)\033[0m", sep="\n      ") # Numbers
        print ("\033[1m    Calculator:\033[0m", "\033[4m|Addition                                (Ad)\033[0m", "\033[4m|Subtraction                             (Sb)\033[0m", "\033[4m|Multiplication                          (Mu)\033[0m", "\033[4m|Division                                (Dv\033[0m)", "\033[4m|Remainder division                      (Rd)\033[0m", "\033[4m|Exponent                                (Ex)\033[0m", "\033[4m|Advanced edition                        (Av)\033[0m", sep="\n      ") # Calculator
        print ("\033[1m    Other:\033[0m", "\033[4m|Word repeater                           (Wr)\033[0m", "\033[4m|Letter counter - WEIRD EDITION          (Lw)\033[0m", "\033[4m|Letter scrambler                        (Ls)\033[0m", "\033[4m|Letter reverser                         (Lr)\033[0m", "\033[4m|Palindrome detector                     (Pd)\033[0m", sep="\n      ") # Other
        #                        Letter counter means it cycles through the letters like a->b->c
        print ("\033[1m\033[4mExit                                           (Lv or Leave)\033[0m")

        #option selection
        while True:
            option = input("Option:").lower()
            if option in ["letter counter", "lc"]:
                counting.Characters.Letter_counter()
            elif option in ["word counter", "wc"]:
                counting.Characters.Word_counter()
            elif option in ["sentence counter", "sc"]:
                counting.Characters.Sentence_counter()
            elif option in ["speed adder", "sd"]:
                counting.Numbers.Speed_adder()
            elif option in ["digit counter", "dc"]:
                counting.Numbers.Digit_counter()
            elif option in ["digit scambler", "ds"]:
                counting.Numbers.Digit_scrambler()
            elif option in ["digit reverser", "dr"]:
                counting.Numbers.Digit_reverser()
            elif option in ["addition", "ad"]:
                counting.Calculator.Addition()
            elif option in ["subtraction", "sb"]:
                counting.Calculator.Subtraction()
            elif option in ["multiplication", "mu"]:
                counting.Calculator.Multiplication()
            elif option in ["division", "dv"]:
                counting.Calculator.Division()
            elif option in ["remainder division", "rd"]:
                counting.Calculator.Remainder_Division()
            elif option in ["exponent", "ex"]:
                counting.Calculator.Exponent()
            elif option in ["advanced", "av"]:
                counting.Calculator.Advanced(0)
            elif option in ["word repeater", "wr"]:
                counting.Other.Word_repeater()
            elif option in ["letter counter - weird edition", "lw"]:
                counting.Other.Letter_counter_WEIRD()
            elif option in ["letter scrambler", "ls"]:
                counting.Other.Letter_scrambler()
            elif option in ["letter reverser", "lr"]:
                counting.Other.Letter_reverser()
            elif option in ["palindrome detector", "pd"]:
                counting.Other.Palindrome_detector()
            elif option in ["leave", "lv"]:
                print ("Bye! Thank you for choosing Ultimate Counter by Chief guy :).\n")
                exit()
            else:
                print ("\nOption not recognized, restarting")
                continue
print ("Hello! Welcome to the ultimate counting program!                           _  _\nIn this program, you can do all sorts of things related to counting!      / \\/ \\")
print ("For choosing simply type the code associated with program.                \\    /")
print ("Made with love by Chief guy.                                               \\  /\nLinks: \033[4mhttps://bit.ly/chfslnks\033[0m                                              \\/")
print ("\nThere may be some bugs, as it is impossible to find every bug sometimes.\nLet me know on this project's Itch page and I'll fix it.")
print ("I'm quite proud of this project, it's the longest I've ever written too, at 1187 lines of code. :)")
input("\nEnter to continue")
counting.Start()