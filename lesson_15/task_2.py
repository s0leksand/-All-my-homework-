def longest_words(file):

    r = open(file, "r")
    listw = r.read().split()
    lenw = 0
    maxword = []

    for i in range(len(listw)):
        if len(listw[i]) > lenw:
            lenw = len(listw[i])

    for j in range(len(listw)):
        if len(listw[j]) == lenw:
            maxword.append(listw[j])
    r.close()
    return maxword


if __name__ == "__main__":
    filew = "article.txt"
    for y in range(len(longest_words(filew))):
        print(longest_words(filew)[y])
