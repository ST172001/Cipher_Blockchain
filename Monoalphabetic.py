class MonoalphabeticCipher:
    def __init__(self, key):
        # The alphabet used for reference
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        # The key provided for substitution
        self.key = key.upper()
        
        # Ensure the key is valid (contains each letter of the alphabet once)
        if sorted(self.key) != sorted(self.alphabet):
            raise ValueError("Invalid key for Monoalphabetic Cipher")
    
    def encrypt(self, plaintext):
        """Encrypts the provided plaintext using the key."""
        encrypted_text = [self.key[self.alphabet.index(char)] if char in self.alphabet else char for char in plaintext.upper()]
        return ''.join(encrypted_text)
    
    def decrypt(self, ciphertext):
        """Decrypts the provided ciphertext using the key."""
        decrypted_text = [self.alphabet[self.key.index(char)] if char in self.key else char for char in ciphertext.upper()]
        return ''.join(decrypted_text)

# User Interaction
key = input('Enter a key (a permutation of the alphabet): ')
cipher = MonoalphabeticCipher(key)

plaintext = input('Enter message to be transmitted: ')

choice = input('Do you want to encrypt [Y/N]: ')
if choice.upper() == 'Y':
    encrypted = cipher.encrypt(plaintext)
    print(f"Encrypted Text: {encrypted}")

choice = input('Do you want to decrypt [Y/N]: ')
if choice.upper() == 'Y':
    decrypted = cipher.decrypt(encrypted)
    print(f"Decrypted Text: {decrypted}")

