'''
author: teja
date : 1/8/2018
'''

VARA = input("enter an  varA")
VARB = input("enter an  varB")
if(type(VARA)==str or type(VARB)==str):
	print("string involved")
if(VARA>VARB):
    print("bigger")
if(VARA==VARB):
	print("equal")
if(VARA<VARB):
	print("smaller")