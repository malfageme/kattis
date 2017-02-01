#!/usr/bin/python

import sys


def calc_result(variables, values, sum_list, sub_list):
    sum_total=0
    sub_total=0
    try:
        for name in sum_list:
            sum_total+=variables[name]
        for name in sub_list:
            sub_total+=variables[name]
        return values[sum_total-sub_total]
    except:
        return 'unknown'

tokens={}
variables={}
values={}
while 1:
    line=sys.stdin.readline()
    if not line:
        break
    tokens=line.split()
    op=tokens[0]
    if op=='def':
        #print "New var:"
        name=tokens[1]
        value=int(tokens[2])
        try:
            values.pop(variables[name])
        except:
            pass
        variables[name]=value
        values[value]=name
        #print "   Variables:", variables
        #print "   Values:", values
    elif op=='clear':
        #print "clear:"
        variables={}
        values={}
    elif op=='calc':
        #print "Calc:"
        sum_list=[]
        sub_list=[]
        last='+'
        for token in tokens[1::]:
            #print "Token:", token
            if token in '-+':
                last=token
            elif token=='=':
                print " ".join(tokens[1::]), calc_result(variables, values, sum_list, sub_list)
            elif last=='+':
                sum_list.append(token)
            else:
                sub_list.append(token)
                
              


