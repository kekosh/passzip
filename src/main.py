#-*- coding: utf-8 -*-
import pyminizip
import os
import sys

"""pyminizip.compress("src_path","zippath","password",int(level_Num) as compress single file"""
# pyminizip.compress("../sample/test1.txt","../sample/testzip.zip","password",1)

"""pyminizip.compress_multiple([compress filepath list],"zippath","password",int(compress_level_num) as compress some files """
# compresses = ["../sample/test1.txt","../sample/test2.txt"]
# pyminizip.compress_multiple(compresses, "../sample/multiple.zip", "password", 1)


def create_zip(files, zip_name, output_path, password):
    zip_path = os.path.join(output_path, zip_name)
    
    try:
        if len(files) == 1:
            single = files[0]
            pyminizip.compress(single, zip_path, password, 1)
        else:
            pyminizip.compress_multiple(files, zip_path, password, 1)
    except:
        return sys.exc_info()

if __name__ == "__main__":
    files = ["../sample/test1.txt"]
    zip_name = "zipfile.zip"
    output_path = "../sample"
    password = "password"
    
    result = create_zip(files, zip_name, output_path, password)
    if result == None:
        print("fin.")
    else:
        print(result)
        