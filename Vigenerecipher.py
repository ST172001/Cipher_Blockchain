class VigenereCipher:
    def __init__(self, keyword):
        self.keyword = keyword.upper()

    def _repeat_keyword(self, length):
        """Repeat the keyword to match the given length."""
        return (self.keyword * (length // len(self.keyword))) + self.keyword[:length % len(self.keyword)]

    def encrypt(self, plaintext):
        repeated_keyword = self._repeat_keyword(len(plaintext))
        encrypted_text = []

        for p_char, k_char in zip(plaintext.upper(), repeated_keyword):
            if p_char.isalpha():
                encrypted_char = chr((ord(p_char) - 65 + ord(k_char) - 65) % 26 + 65)
                encrypted_text.append(encrypted_char)
            else:
                encrypted_text.append(p_char)

        return ''.join(encrypted_text)

    def decrypt(self, ciphertext):
        repeated_keyword = self._repeat_keyword(len(ciphertext))
        decrypted_text = []

        for c_char, k_char in zip(ciphertext.upper(), repeated_keyword):
            if c_char.isalpha():
                decrypted_char = chr((ord(c_char) - ord(k_char) + 26) % 26 + 65)
                decrypted_text.append(decrypted_char)
            else:
                decrypted_text.append(c_char)

        return ''.join(decrypted_text)

# Example
keyword=input('Enter keyword:')
cipher = VigenereCipher(keyword)
plaintext=input('Enter message to be transmitted:')
choice=input('Do you want to encrypt [Y/N]')
if choice=='Y':
    encrypted = cipher.encrypt(plaintext)
    print(f"Encrypted Text: {encrypted}")
choice=input('Do you want to decrypt [Y/N]')
if choice=='Y':
        decrypted = cipher.decrypt(encrypted)
        print(f"Decrypted Text: {decrypted}")

 