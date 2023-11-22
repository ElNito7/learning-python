fhandle = open('mbox-short.txt')
for line in fhandle :
    upline = line.rstrip()
    print(upline.upper()) 