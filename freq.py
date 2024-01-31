import sys


def make_dict(filename):
    """Generates a dictionary where keys are unique words found in file
    and values are corresponding frequencies.
    Arguements:
        filename: name of the file to be read
    Return:
        dictionary: dictionary storing unique words and their frequencies
        count: total number of words in file
    """

    fin = open(filename,"r")

    dictionary = {}
    count = 0

    # go through each line
    for line in fin:
        line = line.strip('\n').split()

        # split line into words
        for word in line:
            count += 1

            # increase count for that word; create new key if word does not exist in dictionary
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1

    fin.close()
    return (dictionary, count)


if __name__ == "__main__":
   

    correct_usage = "USAGE: python3 freq.py <input_file_name>"

    # print error and exit if user does not use correct syntax
    if len(sys.argv)<2:
        print("ERROR: Too few command-line arguements")
        print(correct_usage)
    elif len(sys.argv)>2:
        print("ERROR: Too many command-line arguements")
        print(correct_usage)

    else:
        dictionary, count = make_dict(sys.argv[1])

        # print error if file does not contain a single word
        if count == 0:
            print ("No words present in {}".format(sys.argv[1]))

        else:
            freq_out = open(sys.argv[1]+".out", "w")

            # output each word, frequency and relative frequency in new file (sorted alphabetically)
            for x, y in sorted(dictionary.items()):
                freq_out.write(x + " " + str(y) + " " + str(round(y/count, 3)) + "\n")
            
            freq_out.close()


# testing the git pull and commit and push ....0.2