s = input("Enter the statement : ")
words = s.split()
def reverse (words, i):
    if i < 0:
        return
    print(words[i], end=" ")
    reverse (words, i-1)
reverse(words, len(words) - 1)