from curses.ascii import isalnum, isalpha, isdigit, islower


s = input()
a = False
b = False
c = False
d = False
e = False

for i in range(len(s)):
    if s[i].isalnum(): a = True
    if s[i].isalpha(): b = True
    if s[i].isdigit(): c = True
    if s[i].islower(): d = True
    if s[i].isupper(): e = True
print(a,b,c,d,e,sep='\n')