import json
import datetime
import string
import random
import time
import traceback

from Crypto.Cipher import PKCS1_OAEP as pk
from Crypto.PublicKey import RSA
import base64

from scripts.classes import *


"""
Good-to-have decorators
"""

def timeit(method):
    """
    Timer decorator
    """
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
        return result

    return timed





"""
General Controller Functions Section
"""

def decrypting(message,key):
    """
    Helper function for decrypting stuff
    ------------------------------------
    RSA size : 1024 bytes
    """
    try:
        #print(message)
        #print(key)
        private_key = RSA.importKey(key)
        #print(private_key.publickey().export)
        cipher = pk.new(private_key)
        return_msg = cipher.decrypt(base64.b64decode(message))
        return return_msg
    except:
        print(traceback.format_exc())


def encrypting(message,key):
    print(key)
    print()
    public_key = RSA.importKey(key).publickey()
    cipher = pk.new(public_key)
    str_list = ','.join([str(item) for item in message])
    print(str_list)
    return_msg = base64.b64encode(cipher.encrypt(bytearray(str_list,'ascii'))).decode('ascii')
    return return_msg



extra = "test_data"
@timeit
def read():
    with open(f"iexec_in/encrypted_dataset.json",'r+') as f:
        data = json.loads(f.read())

    for attr,val in data['taxi'].items():
        print(bytearray(val['location'],'ascii'))
        data['taxi'][attr]['location'] = [float(item) for item in decrypting(val['location'],bytearray(val['key'],'ascii')).decode('ascii').split(',')]
        #print(data['taxi'][attr]['location'])

    #print(data)
    return data


def write(output_dictionary):
    with open(f"iexec_out/encrypted_dataset.json",'w+') as f:
        if 'taxi' in output_dictionary.keys():
            #print(output_dictionary)
            for attr,val in output_dictionary['taxi'].items():
                #pass
                #print(val)
                output_dictionary['taxi'][attr]['location'] = encrypting(val['location'],bytearray(val['key'],'ascii'))

        f.write(json.dumps(output_dictionary))

    return True


def save_call_instance(user):
    current_time = datetime.datetime.now()
    minute = str(current_time.minute)
    hour = str(current_time.hour)
    day = str(current_time.day)
    month = str(current_time.month)
    year = str(current_time.year)
    location = user.location
    parameters = False
    with open("dataset.csv",'r+') as g:
        if g.readline(0) != "start_time;pochetok\n":
            parameters = True

    with open("dataset.csv","a+") as f:

        if parameters == False:
            f.write("start_time;pochetok\n")

        f.write(f"{minute}-{hour}-{day}-{month}-{year};{location}\n")
    
    return True


def filter_taxis():
    data = read()
    taxis = []

    for taxi in data['taxi'].items():
        if taxi[1]['active'] == False:
            taxis.append(Taxi(taxi[0],taxi[1]['location']))
    return taxis

"""
Good-to-have functions
"""

def new_hash(size=26, chars=string.ascii_letters + string.digits):
    """
    Function which returns a random hash
    """
    return ''.join(random.choice(chars) for _ in range(size))

