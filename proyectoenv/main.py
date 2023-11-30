from fileinput import filename
from parser import miParser

def readSourceCodeFromFile(filename):
    with open(filename, 'r') as file:
        source_code = file.read()
    return source_code

def main():
    print("Parseando subset por defecto:")
    subset_c = "subsetC.cpp"
    source_code = readSourceCodeFromFile(subset_c)
    miParser(source_code)
    input("Pesione enter para salir...")


if __name__ == '__main__':
    main()
