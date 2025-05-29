def solution(word):
    word_len = len(word) - 1 # Getting the position of the index starting including 0
    reverse = ""
    while word_len > -1:
        reverse = reverse + word[word_len] # adding the last char to the reversed word
        word_len -= 1 # iterate to the next word
    print(reverse)
    return reverse

solution("hello")
