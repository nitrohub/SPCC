f= open("program.txt","r")
li=[]
SymTab=[]
LitTab=[]
[li.append(i.split()) for i in f]
MOT=['LA','SR','L','AR','A','ST','C','LR','BC','BCR']
POT=['*PROCESS','ACONTROL','ACTR','ADATA','AGO ','AIF','AINSERT','ALIAS','AMODE','ANOP ','AREAD','CATTR','CCW','CCW0','CCW1','CNOP ','COM ','COPY','CSECT','CXD' ,'DC','DROP','DS','DSECT','DXD','EJECT','END','ENTRY','EQU','EXITCTL','EXTRN','GBLA','GBLB','GBLC','ICTL','ISEQ','LCLA','LCLB','LCLC','LOCTR','LTORG','MACRO','MEND','MEXIT','MNOTE','OPSYN','ORG','POP' ,'PRINT','PUNCH','PUSH' ,'REPRO','RMODE','RSECT ','SETA' ,'SETB' ,'SETC ','SPACE' ,'TITLE','START','USING ','WXTRN' ,'XATTR']
locPtr=0
for i in li:
  print(i)
