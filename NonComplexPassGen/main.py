#with open('words.txt', 'r') as file:

from generator import Generator
from fileReader import FileReader
file= open('words.txt','r')

def main():  
    wordsArray= FileReader('words.txt')
    specialCharArray= FileReader('specialChar.txt')
    #readData = file.read()
    #words= readData.split()
    #print(words)
    Generator(wordsArray,specialCharArray)

