import sys

morse={
     'A':".-",
     'B':"-...",
     'C':'-.-.',
     'D':'-..',
     'E':'.',
     'F':'..-.',
     'G':'--.',
     'H':'....',
     'I':'..',
     'J':'.---',
     'K':'-.-',
     'L':'.-..',
     'M':'--',
     'N':'-.',
     'O':'---',
     'P':'.--.',
     'Q':'--.-',
     'R':'.-.',
     'S':'...',
     'T':'-',
     'U':'..-',
     'V':'...-',
     'W':'.--',
     'X':'-..-',
     'Y':'-.--',
     'Z':'--..',
     '_':'..--',
     ',':'.-.-',
     '.':'---.',
     '?':'----'
}

morse_r={}

for key,value in morse.items():
    morse_r[value]=key

for line in sys.stdin:
    line=line.strip()
    numbers=[]
    morse_text=""
    for c in line:
        morse_text+=morse[c]
        numbers.append(len(morse[c]))
    numbers_r=numbers.reverse()
    coded_text=""
    i=0
    for number in numbers:
        morse_chunk=morse_text[i:i+number]
        coded_text+=morse_r[morse_chunk]
        i+=number
        
    print coded_text
