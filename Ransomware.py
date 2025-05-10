from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

# Funkcja szyfrująca plik
def encrypt_file(input_file, output_file, key):
    cipher = AES.new(key, AES.MODE_CBC)
    
    # Odczytanie danych wejściowych
    with open(input_file, 'rb') as f:
        data = f.read()

    # Dodanie paddingu, aby dane miały długość wielokrotności 16
    padding_length = 16 - len(data) % 16
    data += bytes([padding_length]) * padding_length
    
    # Szyfrowanie
    encrypted_data = cipher.encrypt(data)
    
    # Zapisanie zaszyfrowanych danych oraz IV (wektora inicjalizacji)
    with open(output_file, 'wb') as f:
        f.write(cipher.iv)  # Zapisujemy wektor inicjalizacji (IV)
        f.write(encrypted_data)

# Funkcja deszyfrująca plik
def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        iv = f.read(16)  # Odczytanie IV
        encrypted_data = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Deszyfrowanie
    decrypted_data = cipher.decrypt(encrypted_data)
    
    # Usunięcie paddingu
    padding_length = decrypted_data[-1]
    decrypted_data = decrypted_data[:-padding_length]

    # Zapisanie odszyfrowanych danych
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

# Generowanie losowego klucza AES (256 bitów)
key = get_random_bytes(32)

# Szyfrowanie pliku
encrypt_file('plik_do_szyfrowania.txt', 'plik_zaszyfrowany.enc', key)

# Deszyfrowanie pliku
decrypt_file('plik_zaszyfrowany.enc', 'plik_odszyfrowany.txt', key)

print("Szyfrowanie i deszyfrowanie zakończone.")
