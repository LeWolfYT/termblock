import os
import time

w,h = os.get_terminal_size()
os.system("clear")
print("Termblocks v1.1.1")
print("Type \"cl\" to see the full changelog")
time.sleep(4)

blocks = ["print ()", "clear screen", "new line", "exit", "sleep ()", "set variable () to ()", "reset timer", "run function,"]
blockcode = ["print({})", "os.system('clear')", "print()", "sys.exit()", "time.sleep({})", "{} = {}", "tbtimer = time.perf_counter()", "{}()"]
inputcode = [1,0,0,0,1,2,0,1]

wraps = ["if ():", "forever:", "repeat ():", "while ():", "function ()"]
wrapcode = ["if {}:", "while True:", "for _ in range({}):", "while {}:", "def {}():"]
inputwrap = [1,0,1,1,1]

reporters = ["var", "timer", "x + y", "x - y", "x * y", "x / y", "true", "false", "null", "x and y", "x or y", "not x", "x = y", "input (prompt)", "length of ()"]
reportercode = ["{}", "time.perf_counter - tbtimer", "{} + {}", "{} - {}", "{} * {}", "{} / {}", "True", "False", "None", "{} and {}", "{} or {}", "not {}", "{} == {}", "input({})", "len({})"]
inputop = [1,0,2,2,2,2,0,0,0,2,2,1,2,1,1]

code = ["import os","import sys","import time"]

global tabct
tab = "    "
tabct = 0

def changelog():
    print("Changelog:")
    print("v1.1.1")
    print("- First public release!")
    print("- Added function functionality for functions")
    print("v1.1.0")
    print("- Added wrap blocks such as if, forever, and for loops.")
    print("- Added input and length reporters")
    print("- Added boolean operators")
    print("\nPress enter when you are done reading!")
    print("v1.0.0")
    print("- Initial private release")
    input()

def printav():
    print("Available blocks:")
    for i in range(len(blocks)):
        print(str(i+1) + ". " + blocks[i])

def formattext(text):
    try:
        textint= int(text)
        return textint
    except:
        return "'{}'".format(text)

def inputrep(r,l):
    for i in range(r):
        n = input("Input "+str(i+1)+" (type _r for reporters): ")
        if not n == "_r":
            l.append(formattext(n))
        else:
            n = oper()
            l.append(formattext(n))

def oper():
    print("Available reporters:")
    for i in range(len(reporters)):
        print(str(i+1) + ". " + reporters[i])
    opi = int(input("Reporter number: "))
    opc = reportercode[opi-1]
    print(opc)
    inps = []
    inputrep(inputop[opi-1],inps)
    opf = opc.format(*inps)
    return opf

def inputbl():
    global tabct
    tabspace = tab * tabct
    if tabct > 0:
        bl = input("Block number (e to end, cd to see python code, c to see wrap blocks, w to exit wrap): ")
    else:
        bl = input("Block number (e to end, cd to see python code, c to see wrap blocks): ")
    try:
        blnum = int(bl)-1
    except:
        blnum = 0
    codein = []
    if bl == "e":
        if "sys.exit()" in code:
            return False
        else:
            print("WARNING: Exit statement not present in code.")
            return False
    elif bl == "cd":
        for i in code:
            print(i)
        time.sleep(5)
        return True
    elif bl == "c":
        return inputc()
    elif bl == "w" and tabct != 0:
        tabct -= 1
        return True
    elif bl == "cl":
        changelog()
        return True
    else:
        if blockcode[blnum] == "sys.exit()":
            #make sure nothing comes after exiting
            code.append("sys.exit()")
            return False
        else:
            if inputcode[blnum] != 0:
                inputrep(inputcode[blnum],codein)
                code.append(tabspace + blockcode[blnum].format(*codein))
                return True
            else:
                code.append(tabspace + blockcode[blnum])
                return True

def inputc():
    for c in range(len(wraps)):
        print(str(c+1) + ". " + wraps[c])
    wr = input("Input wrap number: ")
    wrf = formattext(wr)
    wrin = []
    if type(wrf) == int:
        cd = wrapcode[wrf-1]
        cdi = inputwrap[wrf-1]
        if cd != 0:
            inputrep(cdi,wrin)
        global tabct
        tabct += 1
    else:
        print("Invalid choice!")
        time.sleep(1.5)
        return True
    code.append(cd.format(*wrin))
    return True

def writefile(lines):
    with open(input("Enter file name: "), "a") as f:
        for line in lines:
            f.write(line + "\n")

while True:
    os.system("clear")
    printav()
    if not inputbl():
        writefile(code)
        break