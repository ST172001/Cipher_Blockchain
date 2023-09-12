class PlayfairCipher:
    def __init__(self, keyword):
        self.tableau = self._generate_tableau(keyword)

    def _generate_tableau(self, keyword):
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' is excluded
        tableau = [[None for _ in range(5)] for _ in range(5)]
        
        # Remove duplicate letters from keyword and convert to uppercase
        keyword = "".join(sorted(set(keyword), key=keyword.index)).upper()
        
        # Remove any non-alphabet characters and 'J' from the keyword
        keyword = "".join([char for char in keyword if char in alphabet and char != 'J'])
        
        # Fill the tableau with the keyword
        k_index = 0
        for row in range(5):
            for col in range(5):
                if k_index < len(keyword):
                    tableau[row][col] = keyword[k_index]
                    k_index += 1
        
        # Fill the tableau with the remaining alphabet characters
        for char in alphabet:
            if char not in keyword:
                for row in range(5):
                    for col in range(5):
                        if tableau[row][col] is None:
                            tableau[row][col] = char
                            break

        return tableau

    def _prepare_text(self, text):
        prepared_text = []
        i = 0
        while i < len(text):
            if i + 1 < len(text) and text[i] == text[i + 1]:
                prepared_text.append(text[i])
                prepared_text.append('X')
                i += 1
            elif i + 1 < len(text):
                prepared_text.append(text[i])
                prepared_text.append(text[i + 1])
                i += 2
            else:
                prepared_text.append(text[i])
                prepared_text.append('X')
                i += 1
        return ''.join(prepared_text)

    def _find_position(self, char):
        for row in range(5):
            for col in range(5):
                if self.tableau[row][col] == char:
                    return row, col
        return -1, -1

    def encrypt(self, plaintext):
        prepared_text = self._prepare_text(plaintext.upper().replace('J', 'I'))
        encrypted_text = []

        for i in range(0, len(prepared_text), 2):
            char1, char2 = prepared_text[i], prepared_text[i + 1]
            row1, col1 = self._find_position(char1)
            row2, col2 = self._find_position(char2)

            # Characters are in the same row
            if row1 == row2:
                encrypted_text.append(self.tableau[row1][(col1 + 1) % 5])
                encrypted_text.append(self.tableau[row2][(col2 + 1) % 5])
            # Characters are in the same column
            elif col1 == col2:
                encrypted_text.append(self.tableau[(row1 + 1) % 5][col1])
                encrypted_text.append(self.tableau[(row2 + 1) % 5][col2])
            # Characters form a rectangle
            else:
                encrypted_text.append(self.tableau[row1][col2])
                encrypted_text.append(self.tableau[row2][col1])

        return ''.join(encrypted_text)

    def decrypt(self, ciphertext):
        decrypted_text = []

        for i in range(0, len(ciphertext), 2):
            char1, char2 = ciphertext[i], ciphertext[i + 1]
            row1, col1 = self._find_position(char1)
            row2, col2 = self._find_position(char2)

            # Characters are in the same row
            if row1 == row2:
                decrypted_text.append(self.tableau[row1][(col1 - 1) % 5])
                decrypted_text.append(self.tableau[row2][(col2 - 1) % 5])
            # Characters are in the same column
            elif col1 == col2:
                decrypted_text.append(self.tableau[(row1 - 1) % 5][col1])
                decrypted_text.append(self.tableau[(row2 - 1) % 5][col2])
            # Characters form a rectangle
            else:
                decrypted_text.append(self.tableau[row1][col2])
                decrypted_text.append(self.tableau[row2][col1])

        return ''.join(decrypted_text)

# User Interaction
keyword = input('Enter a keyword for the Playfair tableau: ')
cipher = PlayfairCipher(keyword)

plaintext = input('Enter message to be transmitted: ')

choice = input('Do you want to encrypt [Y/N]: ')
if choice.upper() == 'Y':
    encrypted = cipher.encrypt(plaintext)
    print(f"Encrypted Text: {encrypted}")

choice = input('Do you want to decrypt [Y/N]: ')
if choice.upper() == 'Y':
    decrypted = cipher.decrypt(encrypted)
    print(f"Decrypted Text: {decrypted}")

