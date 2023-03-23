
# python has streams/handles that will deal with the particulars of 
# 2 kinds of files -> text and binary
# binary can be images, videos, songs, etc. 

try:
    stream = open('animals.txt')
    
    # this is elegant and simple, and it also closes the stream automatically
    # many ways to read files, choose the best way based on your needs
    for line in stream:
        print(line, end='')

    lines = stream.readlines() # can also pass an argument here, lots of ways to read depending on your file!
    for line in lines:
        print(line, end='')

    line = stream.readline()
    while line != '':
        print(line, end='-')
        line = stream.readline()

    # this might be used in the case that a file is huge, prevents program crash
    character = stream.read(1)
    while character != '':
        print(character, end='-')
        character = stream.read(1)

    print(stream.read()) # simply shows total file
    # when you invoke 'read()', this moves the read index which might be picked up again later
    print(stream.read(10)) # reads the first 10 bytes, which is typically the first 10 chars
except Exception as e:
    print('Error:', e)
finally:
    stream.close()


try:
    stream = open('newfile.txt', 'w') # 'w' mode will either create the file, or overwrite an existing one
    stream.write('First message\n')
    stream.write('Second message')
except Exception as e:
    print(e)
finally:
    stream.close()


# this was a little tricky, although not really
# needs to strip different chars like '.' or ',' and find out how many times a word occurs
def count_occurences(file_name, word):
    count = 0
    try:
        stream = open(file_name)
        split_stream = stream.read().split()
        for item in split_stream:
            if word == item.lower().replace(',','').replace('.',''):
                count += 1
    except Exception as e:
        print(e)
    finally:
        stream.close()
    return count
