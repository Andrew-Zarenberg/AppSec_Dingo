from Crypto.Cipher import AES
import hashlib
import csv

class TPM:

    # TODO: figure out file name
    file_name = "TPM.csv"

    # TODO: remove later
    key = "This is a key123"
    iv = 'This is an IV456'

    PCR_REGISTER_LENGTH = 40

    def __init__(self, name):
        self.file_name = name

    def clearTPM(self):
        # Every time TPM is re-initialized, registers should be reset
	with open(self.file_name,'w') as f:
		fobj = csv.writer(f)
		for x in range(0,17):
			baseSTR = "PCR -"+ str(x)
			regVal = "0000000000000000000000000000000000000000"
			data = [baseSTR,regVal]
			fobj.writerow(data)
		for y in range(18,23):
			baseSTR = "PCR -" + str(y)
			regVal = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"
			data = [baseSTR,regVal]
			fobj.writerow(data)
		baseSTR = "PCR -23"
		regVal = "0000000000000000000000000000000000000000"
    		data = [baseSTR,regVal]
                fobj.writerow(data)
	return

    def writeToTPM(self, register, n):
        #TODO: add check to ensure valid register
        # Ensure that the data is valid
        if(self.validate_data(n)):
        	with open(self.file_name, 'r+') as f:
            		fobj = csv.reader(f)
			cnt = -1
			data = []
			for row in fobj:
				foo =[]
				cnt += 1
				if (cnt == register):
					baseSTR = "PCR -"+ str(register)
					regVal = n
					foo = [baseSTR,regVal]
					data.append(foo)
				else:
					data.append(row)
			f.close()
		with open(self.file_name,'w') as f:
			fobj=csv.writer(f)
			fobj.writerows(data)
		return True
	else:
		return False
            
        # if data is not valid, return false
        return False

    # Reads the contents of the TPM and returns the register values
    def readFromTPM(self, register):
        #TODO: add check to ensure valid register
        # read from file
        with open(self.file_name,'r') as f:
		fobj = csv.reader(f)
		cnt = -1
		for row in fobj:
			cnt +=1
			if (cnt == register):
				break
	return str(row[1])
    """
    def readFromTPM(self):
        # read from file
        with open(self.file_name,'r') as f:
		fobj = csv.reader(f)
		cnt = 0
		for row in fobj:
			cnt +=1
			if (cnt == 18):
				break
	return str(row[1])
"""

    # TODO: REMOVE THIS 
    # Takes data as an input and returns the encrypted value
    def encrypt(self, n):
        encryption = AES.new(self.key, AES.MODE_CBC, self.iv)
        result = encryption.encrypt(n)
        return result

    # TODO: REMOVE THIS
    # Takes an encrypted value as input and returns the decrypted value
    def decrypt(self, n):
        decryption = AES.new(self.key, AES.MODE_CBC, self.iv)
        result = decryption.decrypt(n)
        return result

    # This is what should be called by In-Toto
    def extend(self, register, n):
        #TODO: add code to check valid register
        # Get the existing values from the PCR, and hash the new values based on the existing ones.
        current_value = self.readFromTPM(register)
        hash_object = hashlib.sha1(n + current_value)
        hex_dig = hash_object.hexdigest()
        return self.writeToTPM(register, hex_dig)

    # Ensure that the register data is valid
    def validate_data(self, n):
        return len(n) == self.PCR_REGISTER_LENGTH
        

    # Only to be called the first initial time
    def set_register_23(self):
        registers = [0,1,2,3,17,18,19]

        for x in registers:
            register_val = self.readFromTPM(x)
            self.extend(23, register_val) 

    # To be called every time after the first time in order to verify the integrity
    def check_register_23(self):
        current_value = 0

        registers = [0,1,2,3,17,18,19]

        for x in registers:
            register_val = self.readFromTPM(x)
            hash_object = hashlib.sha1(register_val + str(current_value))
            current_value = hash_object.hexdigest()

        register_23_value = self.readFromTPM(23)

        return register_23_value == current_value

    def initialize_register_23(self):
        register_23_val = self.readFromTPM(23)
        print(register_23_val)
        if register_23_val == str(0):
            self.set_register_23()
            log.doing("TPM: First time running - creating entry for register 23.")
            return True
        else:
            return self.check_register_23()


if __name__ == "__main__":
    a = "1234567890123456"
    t = TPM("TPM.csv")
    t.A()
    print(t.extend(18, a))

    
