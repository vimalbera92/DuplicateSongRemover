'''
Created on May 21, 2017

@author: vbera
'''
import os
import hashlib
import argparse

songs = set()

def get_hash(name):
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()
    
def isDuplicateSong(file):
    md5 = get_hash(file)
    if md5 in songs:
        return True
    else:
        songs.add(md5)
        return False

def removeFile(file):
    os.remove(file)
    return True;

def listFiles(directory):
    file_paths = []
    for folder, _, files in os.walk(directory):
        for filename in files:
            file_paths.append(os.path.abspath(os.path.join(folder, filename)))
    
    for file in file_paths:
        if os.path.isdir(file):
            listFiles(file)
        elif file.endswith('.mp3'):
            duplicate = isDuplicateSong(file)
            if duplicate:
                removeFile(file)
                print(file+" is removed.")
    
    
def main(folderName):
    if len(folderName) > 0:
        listFiles(folderName) 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    main(args.filename)
