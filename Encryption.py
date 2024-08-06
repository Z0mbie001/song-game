import string
class encryption:
 
    def __init__(self, valueToUse, key):
        self.item = valueToUse
        self.alpha = list(string.printable)
        self.key = key

    def encrypt(self):
        encryptedStr = ""
        for i in self.item:
            positionInAlpha = self.alpha.index(str(i))
            newPos = positionInAlpha + self.key
            while newPos > len(self.alpha):
                ##print(newPos)
                newPos -= len(self.alpha)
                ##print(newPos)
            newLetter = self.alpha[newPos]
            encryptedStr += newLetter
        return encryptedStr

    def decrypt(self):
        decryptedStr = ""
        for i in self.item:
            positionInAlpha = self.alpha.index(str(i))
            newPos = positionInAlpha - self.key
            while newPos < 0:
                ##print(newPos)
                newPos += len(self.alpha)
                ##print(newPos)
            newLetter = self.alpha[newPos]
            decryptedStr += newLetter
        return decryptedStr
        