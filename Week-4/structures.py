'''
structures.py

Simple functions performing operations on basic Python data structures.  
'''

# Lists

# write a function that returns a list containig the first and the last element
# of "the_list". 
def first_and_last(the_list):
    return [the_list[0], the_list[-1]]


# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is ?greater? than "beginning" or any of the indices is out of the
# list, raise a "ValueError" exception. 
def part_reverse(the_list, beginning, end):
   
    if beginning > end or beginning < 0 or end >= len(the_list):
        raise ValueError
    elif beginning == end:
        return the_list[beginning]
    else:
        new_list = the_list[beginning:end+1]
        return  new_list.reverse() 


# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
    new_list = the_list.insert(index,the_list[index]) # insert the value of the index position at the index position
    new_list = the_list.insert(index,the_list[index]) # repeat again
    return new_list


# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards

def palindrome_word(word):
    check_word = word[::-1]
    if word.lower() == check_word.lower():
        return True
    else:
        return False

    

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence(sentence):
    new_sentence = sentence.lower() # convert all cases into lower case character
    convert_to_strings = "" # a new string to store alphabetical strings from the sentence
    for i in range(len(new_sentence)):
        if new_sentence[i].isalpha():
            convert_to_strings += new_sentence[i]
        
    return palindrome_word(convert_to_strings) # check palindrome using palindrome word function

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence. 
def concatenate_sentences(sentenece1, sentence2):
     
    return


# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    if value in dictionary.values():
        return True
    else:
        return False

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    new_dictionary = dictionary1.copy()
    new_dictionary.update(dictionary2)
    return new_dictionary
