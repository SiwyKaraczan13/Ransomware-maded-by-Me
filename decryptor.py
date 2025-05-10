from Crypto.Cipher import AES

# Funkcja deszyfrująca plik
def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        iv = f.read(16)  # Odczytanie IV (pierwsze 16 bajtów to wektor inicjalizacji)
        encrypted_data = f.read()  # Odczytanie zaszyfrowanych danych

    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Deszyfrowanie
    decrypted_data = cipher.decrypt(encrypted_data)
    
    # Usunięcie paddingu
    padding_length = decrypted_data[-1]  # Długość paddingu
    decrypted_data = decrypted_data[:-padding_length]  # Usuwanie paddingu

    # Zapisanie odszyfrowanych danych
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

# Przykładowe użycie
key = b'32bajtowyklucz123456789012345678'  # Klucz o długości 32 bajtów (256 bitów)
input_file = 'plik_zaszyfrowany.enc'  # Zaszyfrowany plik
output_file = 'plik_odszyfrowany.txt'  # Odszyfrowany plik

# Deszyfrowanie pliku
decrypt_file(input_file, output_file, key)

print("Deszyfrowanie zakończone.")
