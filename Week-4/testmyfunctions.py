def concatenate_sentences(sentence1, sentence2):
    
        if sentence1[0].isupper() and sentence2[0].isupper(): # check whether the two sentences both starts with a capital letter
            if sentence1[-2] == "." or sentence1[-2] == "?" or sentence1[-2] == "!":
                if sentence2[-2] == "." or sentence2[-2] == "?" or sentence2[-2] == "!":
                    return sentence1 + sentence2
        else:
            return "Your input sentences are wrong."
        

a = "This is sentence 1. "
b = "This is sentence 2. "
m = " This is wrong."
n = "This is wrong. too  "
print(concatenate_sentences(a,b))
print(concatenate_sentences(m,n))



