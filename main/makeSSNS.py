import random

def randomssn():
    item = random.randrange(100000000,999999999)
    return item

if __name__ == "__main__":
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






