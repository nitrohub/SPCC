import re

symbols={
     "keywords":["break","else","long","switch","case","int","enum","register","typedef","char","extern","return","union","const","float","short","unsigned","continue","for","signed","void","default","goto","sizeof","volatile","do","if","static","while","main()","main(){"],
     "operators":["+", "-", "*", "/", "%","==", "!=" , ">"," <", ">=","&","<=","="],
     "preprocessor":["#define","#include","#undef","#ifdef","#ifndef","#if","#else","#elif","#endif","#error","#pragma"],
     "specialSymbol":["(", ")",";","#","{","}"],
     "libraryFiles": ["<stdio.h>","<conio.h>","<math.h>"],
     "inbuiltFunction": ["printf","scanf","if","while"]
       }

finput= open("C:/Users/HP/Downloads/Desktop/1.txt","r")
lis=[]
for i in finput:
    if(re.search("printf",i)):
        lis.append("printf")
        i=i[7:len(i)-3]
        lis.append(i)
    elif re.search("scanf",i):
        lis.append("scanf")
    elif re.search("if",i):
        lis.append("if")
        for j in range(2,len(i)):
            lis.append(i[j])
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
    elif item in symbols["inbuiltFunction"]:
        print(item+ ":"+ "Inbuilt function")
    elif (item !='' and item!='\n'):
        if item[0]=='"':  # to check inside of printf(" ") i.e, string
            print(item+":"+"String")
        else:
            for j in item:  # to check what is inside (a>b)
                if j in symbols["operators"]:
                    print(j + ":" + "operator")
                else:
                    print(j + ":" + "Identifier")


