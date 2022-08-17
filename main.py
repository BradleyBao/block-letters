# Bradley Bao
# I am 17

class ASCII:
    
    def __init__(self):
        self.data = {
            "A" : ["  A  ", " A A ", "A   A", "AAAAA", "A   A", "A   A", "A   A"],
            "B" : ["BBBB ", "B   B", "B   B", "BBBB ", "B   B", "B   B", "BBBB "],
            "C" : [" CCC ", "C   C", "C    ", "C    ", "C    ", "C   C", " CCC "],
            "D" : ["DDDD ", "D   D", "D   D", "D   D", "D   D", "D   D", "DDDD "],
            "E" : ["EEEEE", "E    ", "E    ", "EEE  ", "E    ", "E    ", "EEEEE"],
            "F" : ["FFFFF", "F    ", "F    ", "FFF  ", "F    ", "F    ", "F    "],
            "G" : [" GGG ", "G   G", "G    ", "GGGGG", "G   G", "G   G", " GGG "],
            "H" : ["H   H", "H   H", "H   H", "HHHHH", "H   H", "H   H", "H   H"],
            "I" : ["IIIII", "  I  ", "  I  ", "  I  ", "  I  ", "  I  ", "IIIII"],
            "J" : ["JJJJJ", "  J  ", "  J  ", "  J  ", "J J  ", "J J  ", " JJ  "],
            "K" : ["K   K", "K  K ", "K K  ", "KK   ", "K K  ", "K  K ", "K   K"],
            "L" : ["L    ", "L    ", "L    ", "L    ", "L    ", "L    ", "LLLLL"],
            "M" : ["M   M", "MM MM", "MM MM", "M M M", "M   M", "M   M", "M   M"],
            "N" : ["N   N", "NN  N", "N N N", "N  NN", "N   N", "N   N", "N   N"],
            "O" : [" OOO ", "O   O", "O   O", "O   O", "O   O", "O   O", " OOO "],
            "P" : ["PPPP ", "P   P", "P   P", "PPPP ", "P    ", "P    ", "P    "],
            "Q" : [" QQQ ", "Q   Q", "Q   Q", "Q   Q", "Q   Q", "Q  Q ", " QQ Q"],
            "R" : ["RRRR ", "R   R", "R   R", "RRRR ", "R R  ", "R  R ", "R   R"],
            "S" : [" SSS ", "S   S", "S    ", " SSS ", "    S", "S   S", " SSS "],
            "T" : ["TTTTT", "  T  ", "  T  ", "  T  ", "  T  ", "  T  ", "  T  "],
            "U" : ["U   U", "U   U", "U   U", "U   U", "U   U", "U   U", " UUU "],
            "V" : ["V   V", "V   V", "V   V", "V   V", "V   V", " V V ", "  V  "],
            "W" : ["W   W", "W   W", "W   W", "W W W", "WW WW", "WW WW", "W   W"],
            "X" : ["X   X", "X   X", " X X ", "  X  ", " X X ", "X   X", "X   X"],
            "Y" : ["Y   Y", " Y Y ", "  Y  ", "  Y  ", "  Y  ", "  Y  ", "  Y  "],
            "Z" : ["ZZZZZ", "    Z", "   Z ", "  Z  ", " Z   ", "Z    ", "ZZZZZ"],
            " " : ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
        }
    

    def process(self, target, step=0):
        end = len(self.data[target])
        # Stop
        if step == end:
            print(" ")
        print(self.data[target][step], end="   ")

    def run(self, alphabet):
        # Upper the user input
        alphabet = alphabet.upper()
        
        # Split them
        alphabet_list = list(alphabet)
        
        # Absolute range number 7 because of height, if change, need more characters inside
        for x in range(7):
            for i in alphabet_list:
                self.process(i, x)
                
            # Change Line
            print(" ")
            
        # Add two empty spaces between each
        print(" ")
        print(" ")

app = ASCII()

# The Program only support the basic alphabet and space, does not support comma and full stop or any other special character
# You can use the input method to replace Hello World
app.run("Hello World")
app.run("Wait")
app.run("ok then")
app.run("sl")
app.run("what does it mean")
app.run("that is strange")