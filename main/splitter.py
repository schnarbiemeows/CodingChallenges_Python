import random

def splitter(input):
    index = input.split(",")
    return index[0][1:]
print("WTF")

def randomssn():
    item = random.randrange(100000000,999999999)
    return item

if __name__ == "__main__":
    print("you heard me!")
    input = "hi,there,how,are,you?"
    output = splitter(input)
    print("answer is : " + output)
    ssns = open("/config/ssns.txt","w")
    try:
        counter = 100
        while counter>0:
            ssns.write((str(randomssn()))+"\n")
            counter -=1
    except:
        print("something went wrong!")
    finally:
        ssns.close()






