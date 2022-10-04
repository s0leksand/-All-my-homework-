if __name__ == "__main__":
    text = open("text.txt", "w")
    while True:
        txt = str(input())
        if txt == "":
            break
        text.write(txt + "\n")
    text.close()
