from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP as pk

import json
import base64

with open("dataset.json",'r') as f:
    data = json.loads(f.read())

for attr,val in data['taxi'].items():
    key_pair = RSA.generate(1024)
    priv_key = pk.new(key_pair.publickey())
    str_list = ','.join([str(item) for item in data['taxi'][attr]['location']])
    print(str_list)
    data['taxi'][attr]['location'] = base64.b64encode(priv_key.encrypt(bytearray(str_list,'ascii'))).decode('ascii')
    data['taxi'][attr]['key'] = key_pair.exportKey().decode('ascii')

with open("encrypted_dataset.json",'w') as f:
    f.write(json.dumps(data))