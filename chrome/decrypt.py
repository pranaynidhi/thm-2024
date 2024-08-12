from Crypto.Cipher import AES
import os

def decrypt_file(input_file, output_file, key, iv):
    chunk_size = 64 * 1024
    aes = AES.new(key, AES.MODE_CBC, iv)
    with open(input_file, 'rb') as in_file:
        with open(output_file, 'wb') as out_file:
            while True:
                chunk = in_file.read(chunk_size)
                if len(chunk) == 0:
                    break
                out_file.write(aes.decrypt(chunk))

def main():
    key = b'PjoM95MpBdz85Kk7ewcXSLWCoAr7mRj1'
    iv = b'lR3soZqkaWZ9ojTX'
    encrypted_file = "encrypted_files"
    decrypted_file = "decrypted_files.zip"
    decrypt_file(encrypted_file, decrypted_file, key, iv)
    print("File decrypted and saved successfully.")

if __name__ == "__main__":
    main()
