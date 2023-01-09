from itertools import permutations
import numpy as np

"""  Permutations of 3 and 4-digit numbers """

swappedSums = []


class Sum:
    def __init__(self, sum):
        self.initNums = []
        self.sum = sum

    def addInit(self, num):
        if num not in self.initNums:
            self.initNums.append(num)


def main(y):
    initNum = y
    initNumStr: str = str(initNum)
    x = len(initNumStr)

    maxNum = 0
    tempCtr = x - 1
    for a in range(x):
        maxNum += 9 * np.power(10, tempCtr)
        tempCtr -= 1

    # print(maxNum)

    for j in range(initNum, maxNum + 1):
        ctr = 0
        for perm in list(permutations(str(j))):
            k = [str(x) for x in perm]
            sigma = int(''.join(k))

            if ctr >= 1:
                newSum = j + sigma
                print(j)
                print(sigma)
                print(newSum)

                for ss 
            ctr += 1


 #for swappedSum in swappedSums:
    # print('printing')
    # print(swappedSum.sum)
    # print(swappedSum.initNums)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(100)
