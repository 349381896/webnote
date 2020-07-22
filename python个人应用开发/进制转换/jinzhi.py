

def inputbin(input):  #二进制转换至其它
    input = eval(input)
    input = '0b'+str(input)
    outbin = input              #二进制
    outint = str(int(input,2))  #10进制
    outoct = oct(int(outint))
    outhex = hex(int(outint))   #16进制
    return [outbin,outoct,outint,outhex]


def inputoct(input):  #八进制转换至其它
    input = eval(input)
    outbin = bin(input)
    outoct = oct(input)
    outint = str(int(outbin,2))
    outhex = hex(int(outint))   #16进制
    return [outbin,outoct,outint,outhex]

def inputint(input):  #10进制转换至其它
    input = eval(input)
    outbin = bin(input)
    outint = str(int(outbin,2))  #10进制
    outoct = oct(int(outint))
    outhex = hex(int(outint))   #16进制
    return [outbin,outoct,outint,outhex]

def inputhex(input):  #16进制转换至其它
    input = eval(input)
    outbin = bin(input)
    outoct = oct(input)
    outint = str(int(outbin,2))
    outhex = hex(int(outint))   #16进制
    return [outbin,outoct,outint,outhex]

print(inputbin('11'))
print(inputoct('0o3'))
print(inputint('3'))
print(inputhex('0x3'))