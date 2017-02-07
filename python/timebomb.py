import sys

digits_coded=[
          '**** ** ** ****',
          '  *  *  *  *  *',
          '***  *****  ***',
          '***  ****  ****',
          '* ** ****  *  *',
          '****  ***  ****',
          '****  **** ****',
          '***  *  *  *  *',
          '**** ***** ****',
          '**** ****  ****'
        ]

digits=[]
for line in sys.stdin:
    row_digits=[]
    for i in range(0,len(line),4):
        it=line[i:i+3]
        try:
            digits[i/4]+=it
        except:
            digits.append(it)

int_str=''
for digit in digits:
    try:
        new_digit=digits_coded.index(digit)
        int_str+=str(new_digit)
    except:
        int_str='1'
        break

print "BEER!!" if not int(int_str)%6 else "BOOM!!"


