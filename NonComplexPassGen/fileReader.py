def FileReader(fileName):
    file= open(fileName,'r')
    readData = file.read()
    words= readData.split()
    return words
