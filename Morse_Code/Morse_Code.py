
# Skeleton Program for the AQA AS Summer 2018 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA AS Programmer Team
# developed in a Python 3 environment


# Version Number : 1.6

SPACE = ' '
EOL = '#'
EMPTYSTRING = ''
FULLSTOP = "."

def ReportError(s):
    print('{0:<5}'.format('*'),s,'{0:>5}'.format('*')) 
        
def StripLeadingSpaces(Transmission): 
    TransmissionLength = len(Transmission)
    if TransmissionLength > 0:
        FirstSignal = Transmission[0]
        while FirstSignal == SPACE and TransmissionLength > 0:
            TransmissionLength -= 1
            Transmission = Transmission[1:]
        if TransmissionLength > 0:
            FirstSignal = Transmission[0]
    if TransmissionLength == 0:
        ReportError("No signal received")
    return Transmission

def StripTrailingSpaces(Transmission): 
    LastChar = len(Transmission) - 1
    while Transmission[LastChar] == SPACE:
        LastChar -= 1
        Transmission = Transmission[:-1]
    return Transmission  

def GetTransmission():
    FileName = input("Enter file name: ")
    if FileName[-4:] != ".txt":
        FileName += ".txt"
    try:
        FileHandle = open(FileName, 'r')
        Transmission = FileHandle.readline()
        FileHandle.close()
        Transmission = StripLeadingSpaces(Transmission)
        if len(Transmission) > 0:
            Transmission = StripTrailingSpaces(Transmission)
            Transmission = Transmission + EOL
    except:
        ReportError("No transmission found")
        Transmission = EMPTYSTRING
    return Transmission

def GetNextSymbol(i, Transmission):
    if Transmission[i] == EOL:
        print()
        print("End of transmission")
        Symbol = EMPTYSTRING
    else:
        SymbolLength = 0
        Signal = Transmission[i]
        while Signal != SPACE and Signal != EOL:
            i += 1
            Signal = Transmission[i]
            SymbolLength += 1
        if SymbolLength == 1:
            Symbol = '.'
        elif SymbolLength == 3:
            Symbol = '-'
        elif SymbolLength == 0: 
            Symbol = SPACE
        else:
            ReportError("Non-standard symbol received") 
            Symbol = EMPTYSTRING
    return i, Symbol 

def GetNextLetter(i, Transmission):
    SymbolString = EMPTYSTRING
    LetterEnd = False
    while not LetterEnd:
        i, Symbol = GetNextSymbol(i, Transmission)
        if Symbol == SPACE:
            LetterEnd = True
            i += 4
        elif Transmission[i] == EOL:
            LetterEnd = True
        elif Transmission[i + 1] == SPACE and Transmission[i + 2] == SPACE:
            LetterEnd = True
            i += 3
        else:
            i += 1
        SymbolString = SymbolString + Symbol
    return i, SymbolString

def Decode(CodedLetter, Dash, Letter, Dot, MorseCode):
    CodedLetterLength = len(CodedLetter)
    Pointer = 0
    for i in range(CodedLetterLength):
        Symbol = CodedLetter[i]
        if Symbol not in MorseCode:
            ReportError("invalid symbol", Symbol, "recieved.")
        if Symbol == SPACE:
            return SPACE
        elif Symbol == '-':
            Pointer = Dash[Pointer]
        else:
            Pointer = Dot[Pointer]
    return Letter[Pointer]

def ReceiveMorseCode(Dash, Letter, Dot, MorseCode): 
    PlainText = EMPTYSTRING
    MorseCodeString = EMPTYSTRING
    Transmission = GetTransmission()
    print(Transmission)
    LastChar = len(Transmission) - 1
    i = 0
    while i < LastChar:
        i, CodedLetter = GetNextLetter(i, Transmission)
        MorseCodeString = MorseCodeString + SPACE + CodedLetter
        PlainTextLetter = Decode(CodedLetter, Dash, Letter, Dot, MorseCode)
        PlainText = PlainText + PlainTextLetter
    print(MorseCodeString)
    print(PlainText)

def SendMorseCode(MorseCode):

    PlainText = input("Enter your message: ")
    PlainText = PlainText.upper()
    PlainTextLength = len(PlainText)
    MorseCodeString = EMPTYSTRING
    for i in range(PlainTextLength):
        PlainTextLetter = PlainText[i]
        if PlainTextLetter == SPACE:
            Index = 0

        elif PlainTextLetter == FULLSTOP:
            Index = 27

        else: 
            Index = ord(PlainTextLetter) - ord('A') + 1

        CodedLetter = MorseCode[Index]
        MorseCodeString = MorseCodeString + CodedLetter + SPACE
    print(MorseCodeString)

    lSep = "0"
    wSep = "1"
    dot = "2"
    dash = "3"
    Quart = ""
    space = 0
    chars = MorseCodeString  

    for i in range(len(chars)):
        if chars[i] == ".":
            Quart += dot
            space = 0

        elif chars[i] == "-":
            Quart += dash
            space = 0

        elif chars[i] == " ":
            space += 1
            if space == 3:
                Quart += wSep
            elif space == 1:
                Quart += lSep




#    '''
#            if space == 3:
#                Quart += lSep
#                space = 0
#
#            elif space == 1:
#                Quart += wSep
#                space = 0
#    '''


    print(Quart)
    print("my length of the morse code string is: ", len(MorseCodeString))
  
    return(MorseCodeString)






def DisplayMenu():
    print()
    print("Main Menu")
    print("=========")
    print("R - Receive Morse code")
    print("S - Send Morse code")
    print("P - Print Morse code symbols")
    print("T - Transmit Morse code")
    print("C - Convert Morse code")
    print("X - Exit program")
    print()

def ConvertMorseCode(MorseCode, Letter):
    DecryptedMorse = ""
    MorseMessage = input("enter a morse code message using - and . only: ")
    MorseLen = len(MorseMessage)
    # splits the morse code string into individuals based on what is inside the brackets; in this case it is a space
    symbol = MorseMessage.split(" ")
    for i in range(len(symbol)):
        if symbol[i] == "":
            DecryptedMorse += " "
        if symbol[i] in MorseCode:
            # creates a variable that stores the index value of where the symbol is in the list - morsecode -.
            # ".index(name)" stores the index value of where the names variable is in the list prior
            AlphaIndex = MorseCode.index(symbol[i])
            # this finds the letter in the list - Letter - that has the same index value as the symbol in MorseCode and adds it to the string
            DecryptedMorse += Letter[AlphaIndex]
    print(DecryptedMorse)


def GetMenuOption():
	"""
	Asks the user for a menu input, checks if it is in the list of valid choices and returns it.
	"""
	MenuOption = EMPTYSTRING
	Invalid = True
	ValidChoices = ["R", "S", "X", "P", "T", "C"]
	while Invalid:
		MenuOption = input("Enter your choice: ")
		MenuOption = MenuOption.upper()
		if MenuOption not in ValidChoices:
			print("Invalid choice, please choose a letter from the menu: ")
		else:
			Invalid = False
			
	return MenuOption


def PrintMorseCodeSymbols(Letters, MorseCode):
	print("letter  | Symbol")
	for (this_letter, this_morse_code) in zip(Letters, MorseCode):
		print("     ", this_letter, "|", this_morse_code)


def TransmitMorseCode(MorseCode):
#stores the string of morse code that has been converted from the users input
    MorseCodeString = SendMorseCode(MorseCode)
    Transmission = ""
#loops around for the entire length of the morse code string looking at every character in it and checkin if it is a space, dot, or dash
#if it is a space it adds a string with a space in only to the transmission string
#if the character is a '.', it adds an equals (=) to the transmission string
    for i in range(len(MorseCodeString)):
        if MorseCodeString[i] == SPACE:
            Transmission += "  "
        elif MorseCodeString[i] == ".":
            Transmission += "= "
        elif MorseCodeString[i] == "-":
            Transmission += "=== "
        else:
            ReportError("Invalid Morse code symbol")
    FileName = input("Enter file name for transmission: ")
    try:
        FileHandle = open(FileName, 'w')
        FileHandle.write(Transmission)
        FileHandle.close()
    except:
        ReportError("File could not be written")
    print(Transmission)
    


def SendReceiveMessages():
    Dash = [20,23,0,0,24,1,0,17,0,21,0,25,0,15,11,0,0,0,0,22,13,0,0,10,0,0,0]
    Dot = [5,18,0,0,2,9,0,26,0,19,0,3,0,7,4,0,0,0,12,8,14,6,0,16,0,0,0]
    Letter = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', FULLSTOP]
    MorseCode = [' ','.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..',
                 '--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..', '.-.-.-']

    ProgramEnd = False
    while not ProgramEnd:
        DisplayMenu() 
        MenuOption = GetMenuOption()
        if MenuOption == 'R':
            ReceiveMorseCode(Dash, Letter, Dot, MorseCode)
        elif MenuOption == 'S':
            SendMorseCode(MorseCode) 
        elif MenuOption == 'P':
            PrintMorseCodeSymbols(Letter, MorseCode)
        elif MenuOption == 'T':
            TransmitMorseCode(MorseCode)
        elif MenuOption == "C":
            ConvertMorseCode(MorseCode, Letter)
        elif MenuOption == 'X':
            ProgramEnd = True
    



if __name__ == "__main__":
  SendReceiveMessages()
