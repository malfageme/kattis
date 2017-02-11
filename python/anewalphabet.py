import sys

translate_table={
                  'a':'@',
                  'b':'8',
                  'c':'(',
                  'd':'|)',
                  'e':'3',
                  'f':'#',
                  'g':'6',
                  'h':'[-]',
                  'i':'|',
                  'j':'_|',
                  'k':'|<',
                  'l':'1',
                  'm':'[]\/[]',
                  'n':'[]\[]',
                  'o':'0',
                  'p':'|D',
                  'q':'(,)',
                  'r':'|Z',
                  's':'$',
                  't':"']['",
                  'u':'|_|',
                  'v':'\/',
                  'w':'\/\/',
                  'x':'}{',
                  'y':'`/',
                  'z':'2'
                }

pt=sys.stdin.readline().strip()


print "".join([translate_table[c.lower()] if c.lower() in translate_table.keys() else c  for c in pt])


