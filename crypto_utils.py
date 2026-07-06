import os

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


# ==========================
# Configuration
# ==========================

SALT_SIZE = 16
NONCE_SIZE = 12
KEY_SIZE = 32          # AES-256
ITERATIONS = 100000


# ==========================
# Key Generation
# ==========================

def generate_key(password: str, salt: bytes) -> bytes:
    """
    Generate a secure AES-256 key from a password.
    """

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_SIZE,
        salt=salt,
        iterations=ITERATIONS,
    )

    return kdf.derive(password.encode("utf-8"))


# ==========================
# Encryption
# ==========================

def encrypt_file(file_path: str, password: str, output_path=None):
    """
    Encrypt a file using AES-GCM.

    Parameters
    ----------
    file_path : str
        Original file.

    password : str
        Encryption password.

    output_path : str | None
        Save location. If None, saves as file.enc

    Returns
    -------
    str
        Path of encrypted file.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError("Selected file does not exist.")

    with open(file_path, "rb") as f:
        file_data = f.read()

    salt = os.urandom(SALT_SIZE)
    nonce = os.urandom(NONCE_SIZE)

    key = generate_key(password, salt)

    aes = AESGCM(key)

    encrypted_data = aes.encrypt(
        nonce,
        file_data,
        None
    )

    if output_path is None:
        output_path = file_path + ".enc"

    with open(output_path, "wb") as f:
        f.write(salt)
        f.write(nonce)
        f.write(encrypted_data)

    return output_path


# ==========================
# Decryption
# ==========================

def decrypt_file(file_path: str, password: str, output_path=None):
    """
    Decrypt an AES-GCM encrypted file.

    Parameters
    ----------
    file_path : str
        Encrypted file.

    password : str
        Password.

    output_path : str | None
        Save location.

    Returns
    -------
    str
        Decrypted file path.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError("Encrypted file not found.")

    with open(file_path, "rb") as f:

        salt = f.read(SALT_SIZE)
        nonce = f.read(NONCE_SIZE)
        encrypted_data = f.read()

    key = generate_key(password, salt)

    aes = AESGCM(key)

    decrypted_data = aes.decrypt(
        nonce,
        encrypted_data,
        None
    )

    if output_path is None:

        if file_path.endswith(".enc"):
            output_path = file_path[:-4]
        else:
            output_path = file_path + "_decrypted"

    with open(output_path, "wb") as f:
        f.write(decrypted_data)

    return output_path