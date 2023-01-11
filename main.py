from itertools import permutations  # permutations import used to iterate through all permutations of a string
import numpy as np  # great math library

"""  Permutations of 3 and 4-digit numbers """

# this is the array that will hold all the swapped sum objects
swappedSums = []


# this class is for each individual unique swapped sum
# and holds the sum value as well as a list of all
class Sum:
    def __init__(self, ss):  # constructor for the class that takes a swapped sum
        self.initNums = []  # initializes empty initial numbers list
        self.ss = ss  # sets the object's swapped sum to the sum given in the parameters

    def addInit(self, num):  # this method is to add an initial number to the list
        if num not in self.initNums:  # checks if the initial number is in the list
            self.initNums.append(num)  # appends the initial number if it is not in the list


def main(y):  # main function where the body of the code and algorithm are
    initNum = y  # the y parameter should be some 10^n as the starting value
    initNumStr: str = str(initNum)  # converts the initial number to a string
    x = len(initNumStr)  # retrieves the length of the string

    # these next few lines is a working algorithm to obtain the max number for n-digits based on the initial number
    maxNum = 0
    tempCtr = x - 1
    for a in range(x):
        maxNum += 9 * np.power(10, tempCtr)
        tempCtr -= 1

    # uncomment this next line to confirm the above algorithm works (i.e. initNum = 10 -> maxNum = 99)
    # print(maxNum)

    # this is the for loop to iterate through all numbers in the n-digit range
    for j in range(initNum, maxNum + 1):
        # this is the nested for loop to iterate through every permutation of the number given from the parent loop
        for perm in list(permutations(str(j))):  # list(permutations(str(j))) obtains a list of all perms of j as perm

            sigma = int(''.join(perm))  # joins perm into an integer
            newSum = j + sigma  # adds initial number and sigma to get the swapped sum

            if len(swappedSums) != 0:   # if the swappedSums array isn't empty
                exists = False      # boolean to claim whether the sum exists in the already existing sums
                for sums in swappedSums:
                    if sums.ss == newSum:           # if the sum is in the existing sums
                        exists = True               # set exists to True
                        sums.initNums.append(j)
                        sums.initNums.append(sigma)     # append j and sigma to initNums

                if not exists:  # if it doesn't exist, make a new object and add the initial numbers
                    newSS = Sum(newSum)
                    newSS.initNums.append(sigma)
                    newSS.initNums.append(j)
                    swappedSums.append(newSS)
            else:   # if it is empty make a new object and append it to the swappedSums list
                newSS = Sum(newSum)
                newSS.initNums.append(sigma)
                newSS.initNums.append(j)
                swappedSums.append(newSS)

    # this iterates through each swappedSum object and print its value
    # and corresponding list of initial numbers that have a permutation to add to the sum
    """ Eventually this will not print to the console, but print to a .txt file """
    for swappedSum in swappedSums:
        print(swappedSum.ss)
        # this little algorithm makes the list of initial numbers unique
        initVals = []
        [initVals.append(g) for g in swappedSum.initNums if g not in initVals]
        print(initVals)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(100)
