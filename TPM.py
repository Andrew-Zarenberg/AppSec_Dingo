from Crypto.Cipher import AES

class TPM:

    file_name = "TPMfile"

    key = "This is a key123"
    iv = 'This is an IV456'

    def writeToTPM(self, n):
        encrypted_value = self.encrypt(n)

        # write to file
        f = open(self.file_name, 'w')
        f.write(encrypted_value)

        return True # or false if it fails

    def readFromTPM(self):

        # read from file
        f = open(self.file_name, 'r')
        value = f.read()

        decrypted_value = self.decrypt(value)
        return decrypted_value

    def encrypt(self, n):
        encryption = AES.new(self.key, AES.MODE_CBC, self.iv)
        result = encryption.encrypt(n)
        return result

    def decrypt(self, n):
        decryption = AES.new(self.key, AES.MODE_CBC, self.iv)
        result = decryption.decrypt(n)
        return result



if __name__ == "__main__":
    a = "1234567890123456"

    t = TPM()
    t.writeToTPM(a)
    print(t.readFromTPM())
    

    """
    t = TPM()
    b = t.encrypt(a)
    print(b)
    c = t.decrypt(b)

    print(c)
"""
