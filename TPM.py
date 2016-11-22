from Crypto.Cipher import AES

class TPM:

    key = "This is a key123"
    iv = 'This is an IV456'

    def writeToTPM(self, n):
        encrypted_value = self.encrypt(n)
        # write to file
        return true # or false if it fails

    def readFromTPM(self, n):
        # read from file
        decrypted_value = self.decrypt(n)
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
    b = t.encrypt(a)
    print(b)
    c = t.decrypt(b)

    print(c)
