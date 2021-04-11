from challenges.AlienDictionary import *


if __name__ == "__main__":
    sol = AlienDitionary()
    words = ["ubg","kwh"]
    order = "qcipyamwvdjtesbghlorufnkzx"
    answer = sol.isAlienSorted(words,order)
    print(str(answer))