import re

symbols={
     "keywords":["break","else","long","switch","case","int","enum","register","typedef","char","extern","return","union","const","float","short","unsigned","continue","for","signed","void","default","goto","sizeof","volatile","do","if","static","while","main()","main(){"],
     "operators":["+", "-", "*", "/", "%","==", "!=" , ">"," <", ">=","&","<="],
     "preprocessor":["#define","#include","#undef","#ifdef","#ifndef","#if","#else","#elif","#endif","#error","#pragma"],
     "specialSymbol":["(", ")",";","#","{","}"],
     "libraryFiles": ["<stdio.h>","<conio.h>","<math.h>"],
     "inbuiltFunction": ["printf","scanf","if","while"]
       }

finput= open("C:/Users/OAD/Desktop/1611123.txt","r")
lis=[]
for i in finput:
    if(re.search("printf",i)):
        lis.append("printf")
    elif re.search("scanf",i):
        lis.append("scanf")
    elif re.search("if",i):
        lis.append("if")
    elif re.search("while",i):
        lis.append("while")
    elif re.search("for",i):
        lis.append("for")
    else:
        lis+=re.split("[ ,;\n\t]",i)

print(lis)

for item in lis:
    if item in symbols["keywords"]:
        print(item+":"+"keyword")
    elif item in symbols["operators"]:
        print(item+":"+"operators")
    elif item in symbols["preprocessor"]:
        print(item+":"+"preprocessor")
    elif item in symbols["specialSymbol"]:
        print(item+":"+"Special Symbol")
    elif item in symbols["libraryFiles"]:
        print(item + ":" + "Library files")
# print(lis)
# finput = open("C:/TC/BIN/1715065.c","r")
# characters = finput.readlines()
#
# for line in characters:
# print(line)
