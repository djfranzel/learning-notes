
# binary files under the hood are the same as all files, they are just containers for data stored in bytes
# based on the file type, your machine needs an interpreter to read the file and display it appropriately

data = bytearray(100) # one byte is 8 bits, which is enough to store a number or character
data[0] = 100 # max storable number is 255 because it is 11111111 - which is 8 bits, totaling 1 byte
print(data[0])

data[1] = 120

try:
    stream = open('file.bin', 'wb') # 'wb' means we don't treat it as a txt file
    stream.write(data)
    stream.close()
except Exception as e:
    print(e)

try: 
    bf = open('file.bin', 'rb') # 'rb' means read binary
    byte_array = bf.read()
    print(byte_array)

    # below shows hexadecimal version
    for byte in byte_array:
        print(hex(byte), end='')

    # below shows integer representation
    for byte in byte_array:
        print(int(byte), end='')
    bf.close()
except Exception as e:
    print(e)


# bytes class is immutable
# bytesarray is a list and therefore mutable
# these are similar, but this is a key difference
# run bytearray(bf.read()) to get the array version easily
# or bf.readinto(bytearray)


# default for open() method second argument which sets mode is 'r' which is read text file mode
# many others open('filename', 'r+b') open as binary in read mode, but allow writing without deleting
# should get to know these for each specific use! 


# below is predefined streams, how are these useful?
import sys

for line in sys.stdin:
    if line.rstrip() == 'q':
        break
    print(line)

print('pressed q')


sys.stdout.write('hello')
sys.stderr.write('error')

# these exist but aren't all that useful, why not just input() or print() ? 
# the instructor says it might be in the exam, so know they exist

# more on file exceptions
from os import strerror

try: 
    stream = open('doesnotexist.txt')
    stream.close()
except Exception as e:
    print(e.errno) # many options here to have more verbose error messages
    print(strerror(e.errno)) # using this module provides a nice exception! 

