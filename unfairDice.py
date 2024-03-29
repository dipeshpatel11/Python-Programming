import random


def biased_rolls(prob_list, s, n):  #([1/4, 1/6, 1/12, 1/12, 1/4, 1/6], 42, 200)
    """ Simulate n rolls of a biased m-sided die and return
    a list containing the results. 
    Arguments:
        prob_list: a list of the probabilities of rolling the 
                   number on each side of the m-sided die. The list  
                   will always have the length m (m >= 2), where m is 
                   the number of sides numbered 1 to m. Therefore,  
                   for example, the probability stored at index 0 in 
                   the list is the probability of rolling a 1 on
                   the m-sided die.
        s: the seed to use when initializing the PRNG
        n: the number of rolls to return
    Return:
        rolls: a list (of length n) containing each of the n rolls of the 
               biased die, in the order they were generated.
    """

    rolls = []  # list that stores results
    map = [0]  # list used to "map" ranadom number from [0,1) to a corresponding valid die faces, based on probablity of each face
    random.seed(s)  # set seed to s
    length = len(prob_list)  # calculate number of sides on die

    # creates a list map where the (i+1)'th element is equal to the cumulative sum of elements in prob_list from 0 to i
    for i in range(length):
        sum = map[i] + prob_list[i]
        map.append(sum)

    for i in range(n):
        rand = random.random()  # creates random float between 0 and 1

        for j in range(length):

            # uses map to find corresponding die face value based on rand
            if rand >= map[j] and rand < map[j+1]:
                rolls.append(j+1)  # append that face value to rolls

    # return the resulting rolls
    return rolls


def draw_histogram(m, rolls, width):
    """ Draws a frequency histogram of the rolls of an m-sided die
    mapped to a fixed width.
    Arguments: 
        m (int): the number of sides on the die
        rolls (list): the list of rolls generated by the biased die
        width (int): the fixed width of the histogram, in characters
                     (this is the length of the longest bar in the 
                     histogram, to maximize space in the chart)
    Returns:
        None (but prints the histogram to standard output)
    """

    # calculates the frquency of the mode (most occuring element) in rolls
    max = rolls.count(6)
    for i in range(m):
        if rolls.count(i+1) > max:
            max = rolls.count(i+1)

    # print histogram to std output
    print("Frequency Histogram: {}-sided Die".format(m))  # prints title
    for i in range(m):
        hashes = round(rolls.count(i+1) * (width/max))  # calculates number of hash symbols required; scales based on user-inputted width
        dots = width - hashes  # calculates number of dots required; scales based on user-inpuuted width

        print(i+1, ":", "#"*hashes, "."*dots, sep='')  # prints each bar of histogram


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 unfairDice.py". This can be useful for
    # testing your implementations.

    print("Probabilities: ", end='')

    prob_list = [float(x) for x in input().split()]
    seed = float(input("Seed: "))
    n = int(input("Sample Size: "))

    rolls = biased_rolls(([1/4, 1/6, 1/12, 1/12, 1/4, 1/6], 42, 200))

    print(rolls)

    width = int(input("Histogram Width: "))

    draw_histogram(len(prob_list), rolls, width)