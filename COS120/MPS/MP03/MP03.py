#MP03 by Jake Hayes
def rail4Encrypt(plainText):
    firstChars=""
    secondChars=""
    thirdChars=""
    fourthChars=""
    for i in range(len(plainText)):
        if i%4==0:
            fourthChars=fourthChars+plainText[i]
        elif (i-1)%4==0:
            thirdChars=thirdChars+plainText[i]
        elif i%2==0:
            secondChars=secondChars+plainText[i]
        else:
            firstChars=firstChars+plainText[i]
    encryptText=firstChars+secondChars+thirdChars+fourthChars
    if (len(secondChars)<len(firstChars)):
        encryptText=encryptText+firstChars[-1]
    elif len(thirdChars)<len(secondChars):
        encryptText=encryptText+fistChars[-1]+secondChars[-1]
    elif len(fourthChars)<len(thirdChars):
        encryptText=encryptText+fistChars[-1]+secondChars[-1]+thirdChars[-1]
    return encryptText

def rail4Decrypt(cipherText):
    quartLength=len(cipherText)//4
    extra=len(cipherText)%4
    fourthChars=cipherText[:quartLength]
    thirdChars=cipherText[quartLength:quartLength*2]
    secondChars=cipherText[quartLength*2:quartLength*3]
    if extra>0:
        firstChars=cipherText[quartLength*3:(quartLength*4+extra)]
    else:
        firstChars=cipherText[quartLength*3:]
    plainText=""
    for i in range(quartLength):
        plainText=plainText+firstChars[i]
        plainText=plainText+secondChars[i]
        plainText=plainText+thirdChars[i]
        plainText=plainText+fourthChars[i]
    if len(thirdChars)>len(fourthChars):
        plainText=plainText+thirdChars[-1]
    if len(secondChars)>len(thirdChars):
        plainText=plainText+secondChars[-1]
    if len(firstChars)>len(secondChars):
        plainText=plainText+firstChars[-1]                   
    return plainText

def test4Rail():
    print("Life Together;",rail4Encrypt("Life Together"),";",rail4Decrypt(rail4Encrypt("Life Together")))
    print("Go Buckeyes!;",rail4Encrypt("Go Buckeyes!"),";",rail4Decrypt(rail4Encrypt("Go Buckeyes!")))
    print("Hayes, Jacob;",rail4Encrypt("Hayes, Jacob"),";",rail4Decrypt(rail4Encrypt("Hayes, Jacob")))
    print("Encryption works fine, decryption does not always work.;",rail4Encrypt("Encryption works fine, decryption does not always work."),";",rail4Decrypt(rail4Encrypt("Encryption works fine, decryption does not always work.")))
    
test4Rail()
