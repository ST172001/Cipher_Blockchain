class Atbash:
    def __init__(self):
        self.name = ""
    
    def enter(self):
        self.name = input("Enter the alphabet data (in caps) you want to transmit: ")
    
    def encrypt(self):
        my_dict = {}
        for key in range(65, 91):  # Including 91 to cover 'Z'
            my_dict[chr(key)] = chr(90 - (key - 65))
        
        encrypted_text = "".join([my_dict[char] if char!= ' ' else ' 'for  char in self.name])
        return encrypted_text
    
    def decrypt(self):
        # In Atbash, decryption is same as encryption
        return self.name

# Example of usage
if __name__ == "__main__":
    atbash = Atbash()
    atbash.enter()
    choice=input('Do you want to encrypt [Y/N]')
    if choice=='Y':
        encrypted = atbash.encrypt()
        print(f"Encrypted Text: {encrypted}")
    choice=input('Do you want to decrypt [Y/N]')
    if choice=='Y':
        decrypted = atbash.decrypt()
        print(f"Decrypted Text: {decrypted}")
