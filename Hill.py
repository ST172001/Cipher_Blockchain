import numpy as np
class HillCipher:
    def __init__(self, matrix):
        self.matrix = np.array(matrix, dtype=int)
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.modulus = len(self.alphabet)

        determinant = round(np.linalg.det(self.matrix))
        if self._mod_inverse(determinant, self.modulus) is None:
            raise ValueError("The provided matrix is not invertible modulo {self.modulus}")

    def _mod_inverse(self, a, m):
        """Find modular inverse of a under modulo m."""
        a = a % m
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    def _text_to_numbers(self, text):
        """Convert a text string to a list of numbers."""
        return [self.alphabet.index(char) for char in text]

    def _numbers_to_text(self, numbers):
        """Convert a list of numbers to a text string."""
        return ''.join([self.alphabet[num] for num in numbers])

    def _prepare_text(self, text, block_size):
        """Prepare text by converting to uppercase, removing non-alphabet characters, and padding if necessary."""
        text = text.upper().replace(" ", "")
        text = ''.join([char for char in text if char in self.alphabet])

        # Padding
        while len(text) % block_size:
            text += 'X'
        return text

    def encrypt(self, plaintext):
        plaintext = self._prepare_text(plaintext, self.matrix.shape[0])
        encrypted_text = []

        for i in range(0, len(plaintext), self.matrix.shape[0]):
            block = plaintext[i:i+self.matrix.shape[0]]
            numbers = self._text_to_numbers(block)
            result = self.matrix.dot(numbers) % self.modulus
            encrypted_text.append(self._numbers_to_text(result))

        return ''.join(encrypted_text)

    def decrypt(self, ciphertext):
        determinant = round(np.linalg.det(self.matrix))
        adjugate = np.linalg.inv(self.matrix).T * np.linalg.det(self.matrix)
        inverse_matrix = (self._mod_inverse(determinant, self.modulus) * adjugate) % self.modulus

        decrypted_text = []

        for i in range(0, len(ciphertext), inverse_matrix.shape[0]):
            block = ciphertext[i:i+inverse_matrix.shape[0]]
            numbers = self._text_to_numbers(block)
            result = (inverse_matrix.dot(numbers) % self.modulus).astype(int)  # Ensure result is integer
            decrypted_text.append(self._numbers_to_text(result))

        return ''.join(decrypted_text)

# User Interaction
matrix_size = 2  # For simplicity, we're using 2x2 matrices
print(f"Enter the elements for a {matrix_size}x{matrix_size} matrix, row by row:")
matrix_key = []
for i in range(matrix_size):
    row = list(map(int, input(f"Enter {matrix_size} numbers for row {i+1}, separated by spaces: ").split()))
    matrix_key.append(row)

cipher = HillCipher(matrix_key)

plaintext = input('Enter message to be transmitted: ')

choice = input('Do you want to encrypt [Y/N]: ')
if choice.upper() == 'Y':
    encrypted = cipher.encrypt(plaintext)
    print(f"Encrypted Text: {encrypted}")

choice = input('Do you want to decrypt [Y/N]: ')
if choice.upper() == 'Y':
    decrypted = cipher.decrypt(encrypted)
    print(f"Decrypted Text: {decrypted}")

