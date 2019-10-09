binary=[]                               #create an empty binary list
n=input("input the c code : ")          #Input
p=list(n)                                
if p[0]=='@':                           #If Address
    p.remove('@')                       
    binary.append('0')                  
    lol=list(bin(int(''.join(p))))      
    lol.remove('b')                     
    for i in range(15-len(lol)):            
        binary.append('0')              
    binary.extend(lol)                  #Binary representation in the form of lists
    
else:
    x=n.split()                         #To separate Dest, Comp, Jump
    a=n.split('=')                      
    b=a[1].split(';')                   
    dest,comp,jump=a[0],b[0],b[1]       
    first='111'                         
    binary.extend(first)                
    #for comp binary
    if comp=='0':                           
        binary.append('0')
        l=list('101010')
        binary.extend(l)        
    elif comp=='1': 
        binary.append('0')
        l=list('111111')
        binary.extend(l)
    elif comp=='-1':
        binary.append('0')
        l=list('111010')
        binary.extend(l)
    elif comp=='D':
        binary.append('0')
        l=list('001100')
        binary.extend(l)
    elif comp=='A':
        binary.append('0')
        l=list('110000')
        binary.extend(l)
    elif comp=='M':
        binary.append('1')
        l=list('110000')
        binary.extend(l)
    elif comp=='!D':
        binary.append('0')
        l=list('001101')
        binary.extend(l)
    elif comp=='!A':
        binary.append('0')
        l=list('110001')
        binary.extend(l)
    elif comp=='!M':
        binary.append('1')
        l=list('110001')
        binary.extend(l)
    elif comp=='-D':
        binary.append('0')
        l=list('001111')
        binary.extend(l)
    elif comp=='-A':
        binary.append('0')
        l=list('110011')
        binary.extend(l)
    elif comp=='-M':
        binary.append('1')
        l=list('110011')
        binary.extend(l)
    elif comp=='D+1':
        binary.append('0')
        l=list('011111')
        binary.extend(l)
    elif comp=='A+1':
        binary.append('0')
        l=list('110111')
        binary.extend(l)
    elif comp=='M+1':
        binary.append('1')
        l=list('011111')
        binary.extend(l)
    elif comp=='D-1':
        binary.append('0')
        l=list('001110')
        binary.extend(l)
    elif comp=='A-1':
        binary.append('0')
        l=list('110010')
        binary.extend(l)
    elif comp=='M-1':
        binary.append('1')
        l=list('110010')
        binary.extend(l)
    elif comp=='D+A':
        binary.append('0')
        l=list('000010')
        binary.extend(l)
    elif comp=='D+M':
        binary.append('1')
        l=list('011111')
        binary.extend(l)
    elif comp=='D-A':
        binary.append('0')
        l=list('010011')
        binary.extend(l)
    elif comp=='D-M':
        binary.append('1')
        l=list('010011')
        binary.extend(l)
    elif comp=='A-D':
        binary.append('0')
        l=list('000111')
        binary.extend(l)
    elif comp=='M-D':
        binary.append('1')
        l=list('000111')
        binary.extend(l)
    elif comp=='D&A':
        binary.append('0')
        l=list('000000')
        binary.extend(l)
    elif comp=='D&M':
        binary.append('1')
        l=list('000000')
        binary.extend(l)
    elif comp=='D|A':
        binary.append('0')
        l=list('010101')
        binary.extend(l)
    elif comp=='D|M':
        binary.append('1')
        l=list('010101')
        binary.extend(l)
    else:
        print('Wrong comp syntax')
        boolcompflag=False
    
    #For Destination binary
    if dest=='null':
        l=list('000')
        binary.extend(l)
    elif dest=='M':
        l=list('001')
        binary.extend(l)    
    elif dest=='D':
        l=list('010')
        binary.extend(l)    
    elif dest=='MD':
        l=list('011')
        binary.extend(l)    
    elif dest=='A':
        l=list('100')
        binary.extend(l)    
    elif dest=='AM':
        l=list('101')
        binary.extend(l)    
    elif dest=='AD':
        l=list('110')
        binary.extend(l)    
    elif dest=='AMD':
        l=list('111')
        binary.extend(l)    
    else:
        print('Wrong dest syntax')
        booldestflag=False
    
    #For Jump binary
    if jump=='null':
        l=list('000')
        binary.extend(l)
    elif jump=='JGT':
        l=list('001')
        binary.extend(l)    
    elif jump=='JEQ':
        l=list('010')
        binary.extend(l)    
    elif jump=='JGE':
        l=list('011')
        binary.extend(l)    
    elif jump=='JLT':
        l=list('100')
        binary.extend(l)    
    elif jump=='JNE':
        l=list('101')
        binary.extend(l)    
    elif jump=='JLE':
        l=list('110')
        binary.extend(l)    
    elif jump=='JMP':
        l=list('111')
        binary.extend(l)    
    else:
        print('Wrong jump syntax')
        boolcompflag=False
print(binary)
v=''.join(binary)
print(v)   
    
