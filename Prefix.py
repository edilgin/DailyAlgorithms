"""
Q: Write a  function to find the longest common prefix amongst an array of strings
A: My friend gurkan suggested to use a trie approach to this problem and i will follow his approach.
    My algorithm is as follows:
    1) Get words from the user and store them inside a list
    2) Add all of these words inside a trie data structure
    3) For adding i will do the following
        A. start from root node
        B. create a for loop for every character inside the word that we will add
        C. check if the character is inside the nodes children
            => if not add the character to roots children
            => if it exists just continue to the next node
        E. end with a "." to denote word is finished
    4) After adding words we will check the common prefix count. For this i do the following
        A. start from the root node
        B. create a while loop
        C. inside loop check the child node count of the node
            => if it is one that means we share a prefix
            => if it is not it means we dont share a prefix anymore and we break the loop by returning count of prefixes
        D. we show the count of prefixes and the trie's structure to the user
    5)

"""

class Trie:
    def __init__(self):
        # define a root node that forms the base of the trie
        self.root = {".":{}}

    def add(self, word):
        # start from the base node
        node = self.root["."]
        # this process will itarate for every character inside the word
        for char in word:
            # if the character is not inside the node
            if char not in node:
                # add that character to the dictionary and give it a empty dictionary value
                node[char] = {}
            # new value will be the last added value
            node = node[char]
        # if the word ended add a "." to denote word has ended
        node["."] = {}

    # check common prefixes
    def check_prefix(self):
        # start from the base node
        node = self.root["."]
        # initially the count of prefixes is zero
        count = 0
        while True:
            # if the node only has a single child this means that words have a common prefix
            if len(node) == 1:
                count += 1                # increase common prefixes by one
                node = node[list(node)[0]]  # continue with the next element in the trie

            # if node has more than one child we know that we are no more counting prefixes
            else:
                return count


# words that will be added to the trie
words = []
# get user inputs / if user enters q input process ends
while True:
    inp = input("enter a word for comparison: ")
    if inp == "q":
        break
    words.append(inp)

# create a trie instance
trie = Trie()
# add all of the words entered by the user to the trie
for word in words:
    trie.add(word)
print("-------\n trie looks like this: \n", trie.root)
count = trie.check_prefix()
print("-------\n common prefix count: ", count)
print("-----------")