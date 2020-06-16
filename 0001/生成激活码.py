import random

def generateCode(filename, lenth = 8, num = 200):
    file = open(filename, 'a')
    for codeCount in range(0, num):
        for codeLen in range(0, lenth):
            file.write(chr(random.randint(65, 90)))
        file.write('\n')
    return

if __name__ == '__main__':
    filename = 'active_code'
    generateCode(filename, 8, 200)