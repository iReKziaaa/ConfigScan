from cryptography.fernet import Fernet

# Mets ici ta clé générée
SECRET_KEY = b"5uGyxA7NKDoqQTXvGQPzOMPHUcVOgFNvuyjCMKXdCm8="
cipher = Fernet(SECRET_KEY)

files_to_encrypt = ["ConfigScan.py",]

for file in files_to_encrypt:
    with open(file, "rb") as f:
        data = f.read()
    encrypted = cipher.encrypt(data)
    with open(file + ".enc", "wb") as f:
        f.write(encrypted)
    print(f"{file} -> {file}.enc")
