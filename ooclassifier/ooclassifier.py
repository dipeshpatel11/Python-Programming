"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Name : Dipesh Patel
student ID : 1722408
CCID : dipesh1
CMPUT274 Fall 2021
Assignment-1 : OO Classifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""



# Copyright 2020-2021 Paul Lu
import sys
import copy     # for deepcopy()

Debug = False   # Sometimes, print for debugging.  Overridable on command line.
InputFilename = "file.input.txt"
TargetWords = [
        'outside', 'today', 'weather', 'raining', 'nice', 'rain', 'snow',
        'day', 'winter', 'cold', 'warm', 'snowing', 'out', 'hope', 'boots',
        'sunny', 'windy', 'coming', 'perfect', 'need', 'sun', 'on', 'was',
        '-40', 'jackets', 'wish', 'fog', 'pretty', 'summer'
        ]


def open_file(filename=InputFilename):
    try:
        f = open(filename, "r")
        return(f)
    except FileNotFoundError:
        # FileNotFoundError is subclass of OSError
        if Debug:
            print("File Not Found")
        return(sys.stdin)
    except OSError:
        if Debug:
            print("Other OS Error")
        return(sys.stdin)


def safe_input(f=None, prompt=""):
    try:
        # Case:  Stdin
        if f is sys.stdin or f is None:
            line = input(prompt)
        # Case:  From file
        else:
            assert not (f is None)
            assert (f is not None)
            line = f.readline()
            if Debug:
                print("readline: ", line, end='')
            if line == "":  # Check EOF before strip()
                if Debug:
                    print("EOF")
                return("", False)
        return(line.strip(), True)
    except EOFError:
        return("", False)


class C274:
    def __init__(self):
        self.type = str(self.__class__)
        return

    def __str__(self):
        return(self.type)

    def __repr__(self):
        s = "<%d> %s" % (id(self), self.type)
        return(s)


class ClassifyByTarget(C274):
    def __init__(self, lw=[]):
        super().__init__() # Call superclass
        # self.type = str(self.__class__)
        self.allWords = 0
        self.theCount = 0
        self.nonTarget = []
        self.set_target_words(lw)
        self.initTF()
        return

    def initTF(self):
        self.TP = 0
        self.FP = 0
        self.TN = 0
        self.FN = 0
        return

    # FIXME:  Incomplete.  Finish get_TF() and other getters/setters.
    def get_TF(self):
        return(self.TP, self.FP, self.TN, self.FN)

    # TODO: Could use Use Python properties
    #     https://www.python-course.eu/python3_properties.php
    def set_target_words(self, lw):
        # Could also do self.targetWords = lw.copy().  Thanks, TA Jason Cannon
        self.targetWords = copy.deepcopy(lw)
        return

    def get_target_words(self):
        return(self.targetWords)

    def get_allWords(self):
        return(self.allWords)

    def incr_allWords(self):
        self.allWords += 1
        return

    def get_theCount(self):
        return(self.theCount)

    def incr_theCount(self):
        self.theCount += 1
        return

    def get_nonTarget(self):
        return(self.nonTarget)

    def add_nonTarget(self, w):
        self.nonTarget.append(w)
        return

    def print_config(self,printSorted=True):
        print("-------- Print Config --------")
        ln = len(self.get_target_words())
        print("TargetWords (%d): " % ln, end='')
        if printSorted:
            print(sorted(self.get_target_words()))
        else:
            print(self.get_target_words())
        return

    def print_run_info(self,printSorted=True):
        print("-------- Print Run Info --------")
        print("All words:%3s. " % self.get_allWords(), end='')
        print(" Target words:%3s" % self.get_theCount())
        print("Non-Target words (%d): " % len(self.get_nonTarget()), end='')
        if printSorted:
            print(sorted(self.get_nonTarget()))
        else:
            print(self.get_nonTarget())
        return

    def print_confusion_matrix(self, targetLabel, doKey=False, tag=""):
        assert (self.TP + self.TP + self.FP + self.TN) > 0
        print(tag+"-------- Confusion Matrix --------")
        print(tag+"%10s | %13s" % ('Predict', 'Label'))
        print(tag+"-----------+----------------------")
        print(tag+"%10s | %10s %10s" % (' ', targetLabel, 'not'))
        if doKey:
            print(tag+"%10s | %10s %10s" % ('', 'TP   ', 'FP   '))
        print(tag+"%10s | %10d %10d" % (targetLabel, self.TP, self.FP))
        if doKey:
            print(tag+"%10s | %10s %10s" % ('', 'FN   ', 'TN   '))
        print(tag+"%10s | %10d %10d" % ('not', self.FN, self.TN))
        return

    def eval_training_set(self, tset, targetLabel, lines=True):
        print("-------- Evaluate Training Set --------")
        self.initTF()
        # zip is good for parallel arrays and iteration
        z = zip(tset.get_instances(), tset.get_lines())
        for ti, w in z:
            lb = ti.get_label()
            cl = ti.get_class()
            if lb == targetLabel:
                if cl:
                    self.TP += 1
                    outcome = "TP"
                else:
                    self.FN += 1
                    outcome = "FN"
            else:
                if cl:
                    self.FP += 1
                    outcome = "FP"
                else:
                    self.TN += 1
                    outcome = "TN"
            explain = ti.get_explain()
            # Format nice output
            if lines:
                w = ' '.join(w.split())
            else:
                w = ' '.join(ti.get_words())
                w = lb + " " + w

            # TW = testing bag of words words (kinda arbitrary)
            print("TW %s: ( %10s) %s" % (outcome, explain, w))
            if Debug:
                print("-->", ti.get_words())
        self.print_confusion_matrix(targetLabel)
        return

    def classify_by_words(self, ti, update=False, tlabel="last"):
        inClass = False
        evidence = ''
        lw = ti.get_words()
        for w in lw:
            if update:
                self.incr_allWords()
            if w in self.get_target_words():    # FIXME Write predicate
                inClass = True
                if update:
                    self.incr_theCount()
                if evidence == '':
                    evidence = w            # FIXME Use first word, but change
            elif w != '':
                if update and (w not in self.get_nonTarget()):
                    self.add_nonTarget(w)
        if evidence == '':
            evidence = '#negative'
        if update:
            ti.set_class(inClass, tlabel, evidence)
        return(inClass, evidence)

    # Could use a decorator, but not now
    def classify(self, ti, update=False, tlabel="last"):
        cl, e = self.classify_by_words(ti, update, tlabel)
        return(cl, e)

    def classify_all(self, ts, update=True, tlabel="classify_all"):
        for ti in ts.get_instances():
            cl, e = self.classify(ti, update=update, tlabel=tlabel)
        return


class TrainingInstance(C274):
    def __init__(self):
        super().__init__() # Call superclass
        # self.type = str(self.__class__)
        self.inst = dict()
        # FIXME:  Get rid of dict, and use attributes
        self.inst["label"] = "N/A"      # Class, given by oracle
        self.inst["words"] = []         # Bag of words
        self.inst["class"] = ""         # Class, by classifier
        self.inst["explain"] = ""       # Explanation for classification
        self.inst["experiments"] = dict()   # Previous classifier runs
        return

    def get_label(self):
        return(self.inst["label"])

    def get_words(self):
        return(self.inst["words"])

    def set_class(self, theClass, tlabel="last", explain=""):
        # tlabel = tag label
        self.inst["class"] = theClass
        self.inst["experiments"][tlabel] = theClass
        self.inst["explain"] = explain
        return

    def get_class_by_tag(self, tlabel):             # tlabel = tag label
        cl = self.inst["experiments"].get(tlabel)
        if cl is None:
            return("N/A")
        else:
            return(cl)

    def get_explain(self):
        cl = self.inst.get("explain")
        if cl is None:
            return("N/A")
        else:
            return(cl)

    def get_class(self):
        return self.inst["class"]

    def process_input_line(
                self, line, run=None,
                tlabel="read", inclLabel=False
            ):
        for w in line.split():
            if w[0] == "#":
                self.inst["label"] = w
                if inclLabel:
                    self.inst["words"].append(w)
            else:
                self.inst["words"].append(w)

        if not (run is None):
            cl, e = run.classify(self, update=True, tlabel=tlabel)
        return(self)

    # TASK 1.1
    def preprocess_words(self, mode=''):

        def symbol_process(text):
            """ Remove punctuation and symbols 
            
            Return:
                new_text: a list of words with removed punctuation and symbols
            """
            new_text = []

            for word in text:
                # append alphanumeric words to new_text
                if word.isalnum():
                    new_text.append(word)
                else:
                    # remove punctuation and symbols by appending alphanumeric
                    temp = ""
                    for char in word:
                        if char.isalnum():
                            temp += char

                    # do not append empty strings in new_text
                    if (temp == "") is False:
                        new_text.append(temp)

            return new_text

        def number_process(text):
            """ Remove all numbers in a list of words, unless a word consists
                of only numbers.
            """
            new_text = []

            for word in text:
                # append words consisting of only numbers or only alphabets or
                
                if word.isnumeric():
                    new_text.append(word)
                else:
                    temp = ""
                    for char in word:
                        if char.isdigit() is False:
                            temp += char

                    # temp cannot be empty here
                    new_text.append(temp)

            return new_text

        def stopword_process(text):
            """ Remove all stopwords from a list of words.
            """
            stop_words = ["i", "me", "my", "myself", "we", "our", "ours",
                          "ourselves", "you", "your", "yours", "yourself",
                          "yourselves", "he", "him", "his", "himself", "she",
                          "her", "hers", "herself", "it", "its", "itself",
                          "they", "them", "their", "theirs", "themselves",
                          "what", "which", "who", "whom", "this", "that",
                          "these", "those", "am", "is", "are", "was", "were",
                          "be", "been", "being", "have", "has", "had",
                          "having", "do", "does", "did", "doing", "a", "an",
                          "the", "and", "but", "if", "or", "because", "as",
                          "until", "while", "of", "at", "by", "for", "with",
                          "about", "against", "between", "into", "through",
                          "during", "before", "after", "above", "below",
                          "to", "from", "up", "down", "in", "out", "on",
                          "off", "over", "under", "again", "further", "then",
                          "once", "here", "there", "when", "where", "why",
                          "how", "all", "any", "both", "each", "few", "more",
                          "most", "other", "some", "such", "no", "nor",
                          "not", "only", "own", "same", "so", "than", "too",
                          "very", "s", "t", "can", "will", "just", "don",
                          "should", "now"]

            new_text = []

            for word in text:
                # append non-stopwords to new_text
                if (word in stop_words) is False:
                    new_text.append(word)

            return new_text

        def preprocess_words_main():
            # assume full preprocessing
            keep_symbols = keep_digits = keep_stops = False

            # if mode is present, change the corresponding mode value to True
            if mode == "keep-symbols":
                keep_symbols = True
            elif mode == "keep-digits":
                keep_digits = True
            elif mode == "keep-stops":
                keep_stops = True

            # text contains all the words of the training instance that
            # need to be preprocessed
            text = self.inst['words']

            text = [str(word).lower() for word in text]

            # a True mode value will ignore its corresponding
            # preprocessing step
            if keep_symbols is False:
                text = symbol_process(text)
            if keep_digits is False:
                text = number_process(text)
            if keep_stops is False:
                text = stopword_process(text)

            # update the words in inObjHash
            self.inst['words'] = text
            return

        preprocess_words_main()


# TASK 2.1 AND 2.2
class ClassifyByTopN(ClassifyByTarget):

    def target_top_n(self, tset, num=5, label=''):
        myWords = []
        uniqueWords = []
        freqCount = []
        myTargetWords = []
        # for every training instance in tset
        for ti in tset.get_instances():
            # check if labels match
            if ti.get_label() == label:
                for w in ti.get_words():
                    if w[0] == '#':
                        pass
                    else:
                        # form a list containing
                        # all words in training instances
                        myWords.append(w)

        for word in myWords:
            if word not in uniqueWords:
                # form a list of unique words
                uniqueWords.append(word)
        for word in uniqueWords:
            # count the frequency of the words
            # in the original list
            x = myWords.count(word)
            freqCount.append(x)
        # sort list
        sortedFreq = sorted(freqCount)
        # sort from biggest to smallest number
        sortFreq = list(reversed(sortedFreq))
        for i in range(num):
            for j in range(len(freqCount)):
                # check for words that have the same frequency
                if sortFreq[i] == freqCount[j]:
                    # check if word has not been appended already
                    if uniqueWords[j] not in myTargetWords:
                        # form a list containing the top num
                        # most frequent words
                        myTargetWords.append(uniqueWords[j])
        # set target words to be myTargetWords
        self.set_target_words(myTargetWords)
        return


class TrainingSet(C274):
    def __init__(self):
        super().__init__() # Call superclass
        # self.type = str(self.__class__)
        self.inObjList = []     # Unparsed lines, from training set
        self.inObjHash = []     # Parsed lines, in dictionary/hash
        self.variable = dict()  # NEW: Configuration/environment variables
        return

    def set_env_variable(self, k, v):
        self.variable[k] = v
        return

    def get_env_variable(self, k):
        if k in self.variable:
            return(self.variable[k])
        else:
            return ""

    def inspect_comment(self, line):
        if len(line) > 1 and line[1] != ' ':      # Might be variable
            v = line.split(maxsplit=1)
            self.set_env_variable(v[0][1:], v[1])
        return

    def get_instances(self):
        return(self.inObjHash)      # FIXME Should protect this more

    def get_lines(self):
        return(self.inObjList)      # FIXME Should protect this more

    def print_training_set(self):
        print("-------- Print Training Set --------")
        z = zip(self.inObjHash, self.inObjList)
        for ti, w in z:
            lb = ti.get_label()
            cl = ti.get_class_by_tag("last")     # Not used
            explain = ti.get_explain()
            print("( %s) (%s) %s" % (lb, explain, w))
            if Debug:
                print("-->", ti.get_words())
        return

    def process_input_stream(self, inFile, run=None):
        assert not (inFile is None), "Assume valid file object"
        cFlag = True
        while cFlag:
            line, cFlag = safe_input(inFile)
            if not cFlag:
                break
            assert cFlag, "Assume valid input hereafter"

            if len(line) == 0:   # Blank line.  Skip it.
                continue

            # Check for comments *and* environment variables
            if line[0] == '%':  # Comments must start with % and variables
                self.inspect_comment(line)
                continue

            # Save the training data input, by line
            self.inObjList.append(line)
            # Save the training data input, after parsing
            ti = TrainingInstance()
            ti.process_input_line(line, run=run)
            self.inObjHash.append(ti)
        return

    # TASK 1.2
    def preprocess(self, mode=''):
        # iterate through all training instances
        for i in range(len(self.get_instances())):
            ti = self.get_instances()[i]
            # preprocessing a training instance
            ti.preprocess_words(mode)
        return

    # TASK 3.1
    def return_nfolds(self, num=3):
        nfolds = []

        for i in range(num):
            ts = TrainingSet()
            counter = i
            # round robin strategy is used to create num folds of the
            # original training dataset
            # counter chooses instances at num increments until there are
            # no more training instances in that counter loop
            while counter < len(self.inObjHash):
                # inObjHash and inObjList are appended with the data
                # for that specific training instance
                ts.inObjHash.append(copy.deepcopy(self.inObjHash[counter]))
                ts.inObjList.append(copy.deepcopy(self.inObjList[counter]))
                counter += num

            # add training set to nfolds
            nfolds.append(ts)
        return(nfolds)

    # TASK 3.2
    def copy(self):
        # create a deepcopy of the training set and return it
        ts = copy.deepcopy(self)
        return(ts)

    # TASK 3.3
    def add_training_set(self, tset):
        # iterate through each training instance and append a deepcopy of all
        # the attributes to inObjHash and inObjList
        for i in range(len(tset.inObjHash)):
            self.inObjHash.append(copy.deepcopy(tset.inObjHash[i]))
            self.inObjList.append(copy.deepcopy(tset.inObjList[i]))
        return


# Very basic test of functionality
def basemain():
    global Debug
    tset = TrainingSet()
    run1 = ClassifyByTarget(TargetWords)
    if Debug:
        print(run1)     # Just to show __str__
        lr = [run1]
        print(lr)       # Just to show __repr__

    argc = len(sys.argv)
    if argc == 1:   # Use stdin, or default filename
        inFile = open_file()
        assert not (inFile is None), "Assume valid file object"
        tset.process_input_stream(inFile, run1)
        inFile.close()
    else:
        for f in sys.argv[1:]:
            # Allow override of Debug from command line
            if f == "Debug":
                Debug = True
                continue
            if f == "NoDebug":
                Debug = False
                continue

            inFile = open_file(f)
            assert not (inFile is None), "Assume valid file object"
            tset.process_input_stream(inFile, run1)
            inFile.close()

    print("--------------------------------------------")
    plabel = tset.get_env_variable("pos-label")
    print("pos-label: ", plabel)
    print("NOTE: Not using any target words from the file itself")
    print("--------------------------------------------")

    if Debug:
        tset.print_training_set()
    run1.print_config()
    run1.print_run_info()
    run1.eval_training_set(tset, plabel)

    return


if __name__ == "__main__":
    basemain()