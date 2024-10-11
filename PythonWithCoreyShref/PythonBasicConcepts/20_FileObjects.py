# File Objects
# open is built in command. if you use this way file need to close manually.

# f = open('text.txt', 'r')     #r=read w=write a=append readandwrite='r+'
# print(f.name)          # return the file name
# print(f.mode)          # what mode we are used
# f.close()
    
with open('text.txt', 'r') as f:
    # f_contents = f.read()
    #f_contents = f.readlines() # readlines() method return list of lines in list. 
    # f_contents = f.readline() # return single line at a time.
    # print(f_contents, end='')          # this is small file we can easily able to read.
    
    # f_contents = f.readline() 
    # print(f_contents, end='')  
    
    # for line in f:
    #     print(line, end='')
    
    # To more controlled way 
    
    f_contents = f.read(100)      #read 100 characters in the file
    print(f_contents, end='')
    
    
    # how to use same techinque to handle large number of data.
    # with open('text.txt', 'r') as f:
        
    #     size_to_read = 10
    #     f_contents = f.read(size_to_read)
        
    #     f.seek(0)  # begining the file
    #     # while len(f_contents) > 0:
    #     #     print(f_contents, end='*')
    #     #     f_contents = f.read(size_to_read)
    
    
# with open('text2.txt', 'w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('R')

with open('text.txt','r') as rf:
    with open('test_copy', 'w') as wf:
        for line in rf:
            wf.write(line)
    
# in order open and read and write to picture file need to open in binary mode.
with open('text.jpg','rb') as rf:
    with open('test_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
    
