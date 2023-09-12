class AffineCipher:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.m = 26  # for English alphabet

        # Ensure 'a' is coprime with 'm'
        if self.gcd(self.a, self.m) != 1:
            raise ValueError("'a' must be coprime with 26")

    def encrypt(self, plaintext):
        return ''.join([self._encrypt_char(char) for char in plaintext.upper()])

    def decrypt(self, ciphertext):
        return ''.join([self._decrypt_char(char) for char in ciphertext.upper()])

    def _encrypt_char(self, char):
        if char.isalpha():
            x = ord(char) - 65
            return chr((self.a * x + self.b) % self.m + 65)
        return char

    def _decrypt_char(self, char):
        if char.isalpha():
            x = ord(char) - 65
            a_inv = self.modular_inverse(self.a, self.m)
            return chr(a_inv * (x - self.b) % self.m + 65)
        return char

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def modular_inverse(a, m):
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        raise ValueError(f"No modular inverse found for {a} mod {m}")

# Example
a=int(input('Enter the value of a:'))
b=int(input('Enter the value of b:'))
cipher = AffineCipher(a,b)
plaintext=input('Enter the data to be tranmitted')
choice=input('Do you want to encrypt [Y/N]')
if choice=='Y':
    encrypted = cipher.encrypt(plaintext)
    print(f"Encrypted Text: {encrypted}")
choice=input('Do you want to decrypt [Y/N]')
if choice=='Y':
        decrypted = cipher.decrypt(encrypted)
        print(f"Decrypted Text: {decrypted}")

