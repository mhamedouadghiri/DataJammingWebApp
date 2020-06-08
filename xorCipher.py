def cipher(message, key="pfa2020"):
    result = ""
    for i in range(len(message)):
        chr1 = message[i]
        
        if chr1.isspace():
            result += chr1
            continue
        
        chr2 = key[i % len(key)]
        r = chr(ord(chr1) ^ ord(chr2))
    
        if r.isspace():
            result += chr(256)
        else:
            result += r
        
    return result
