# #!/usr/bin/env python


def count_unique(string1):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}
  
    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """
    word_dict = {}
    word_list = string1.split()
    for word in word_list:
        word_count = word_dict.get(word, 0) +1
        word_dict[word] = word_count

    return word_dict

    #by default splits on any whitespace
    # words = string1.split()
    # d = {}
    # for word in words:
    #     if word in d:
    #         d[word] = d[word] + 1 
    #     else:
    #         d[word] = 1

    # return d

def common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between 
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in both lists, return it each
    time:

        >>> sorted(common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """
    #don't really understand this one
    # common_items = []

    # for item in list1:
    #     if list2.count(item) != 0 and common_items.count == 0:
    #         common_items.append(item)
    # for item in list2:
    #     if common_items.count(item) == 1:
    #         common_items.append(item)
    # return common_items

    #Solve in O(n)

    # common = []

    # for word1 in list1:
    #     for word2 in list2:
    #         if word1 == word2:
    #             common.append(word1)

    # return common

    return []


def unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between 
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `common_items`, this should find [1, 2]:

        >>> sorted(unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show 
    more than 1 or 2 once:

        >>> sorted(unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """
    set1 = set(list1)
    set2 = set(list2)
    #returns unique items between sets
    result = set1.intersection(set2)
    list_of_result = list(result)

    return list_of_result


def sum_zero(list1):
    """Return list of x,y number pair lists from a list where x+y==0

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

        
    For example:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together, 
    that's fine, too:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 0, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """
    d= {}

    for item in list1:
        if item == 0:
            if list1.count(item) > 1:
                    d[(item, item)] = 0
        else:
            if -item in list1:
                    d[(-abs(item), abs(item))] = 0
    return d.keys()
    

#     newlist = []
#     finallist = []

#     for i in range(0, len(list1)):
#         for j in range(i, len(list1)):
#             if list1[i] + list1[j] == 0:
#                 if list1[i] not in newlist and -list1[i] not in newlist:
#                     newlist.append(list1[i])

#     for item in newlist:
#         finallist.append([item, -item])

#     return finallist

# ourlist = [1, -1, 5, 6, 7, 8, 7]

# print sum_zero(ourlist)

    return []

def find_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    For example:

        >>> sorted(find_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(find_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    new_list = set(words)
    return new_list

    # mylist = []

    # for word in words:
    #     if word  not in mylist:
    #         mylist.append(word)

    # return mylist
    return []


def word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that 
    word-length, and the list of words of that word length.

    For example:

        >>> word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """
    d = {}
    new_list = []

    for word in words:
        length = len(word)
        if length in d:
            d[length] = d[length] + [word]
        else:
            d[length] = [word]

    for k, v in d.iteritems():
        new_list.append((k,v))

    return new_list


def adv_word_length_sorted_words(words):
    """Given list of words, return list of ascending [(len, [sorted-words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that 
    word-length, and the list of words of that word length. The list of words
    for that length should be sorted alphabetically.

    For example:

        >>> adv_word_length_sorted_words(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """
# not O(n)
    d = {}
    new_list = []

    for word in words:
        length = len(word)
        if length in d:
            d[length] = d[length] + [word]
        else:
            d[length] = [word]

    for k, v in d.iteritems():
        v.sort()
        new_list.append((k,v))

    return new_list


def pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.
   
    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """

    dict_pirate = {'madam': 'proud beauty', 'boy': 'matey', 'lawyer': 'foul blaggart', 'sir': 'matey', 'students': 'swabbies', 'hello': 'avast', 'professor': 'foul blaggart', 'hotel': 'fleabag inn', 'restroom': 'head', 'excuse': 'arr', 'are': 'be', 'student': 'swabbie', 'the': "th'", 'man': 'matey', 'my': 'me', 'your': 'yer', 'is': 'be', 'restaurant': 'galley'}

    phrase_list = phrase.split()

    for i in range(0, len(phrase_list)):
        if phrase_list[i] in dict_pirate:
            phrase_list[i] = dict_pirate[phrase_list[i]]

    new_phrase = " ".join(phrase_list)
    return new_phrase
    
##############################################################################
# END OF SKILLS TEST; YOU CAN STOP HERE.


def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d

def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documenttion tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)
 

if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "** ALL TESTS PASSED. GOOD WORK!" 
    print