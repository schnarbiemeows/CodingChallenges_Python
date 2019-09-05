from challenges.FindDisappearedNumbers import *

if __name__ == "__main__":
    sol = FindDisappearedNumbers()
    input = []
    answer = sol.findDisappearedNumbers(input)
    for i in answer:
        print(str(i))