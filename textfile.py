#def main():

    #list_of_text = text_file("download.txt")

    #print(list_of_text)

def text_file():

    text_list = []
    
    with open("download.txt", "rt") as text:
        for line in text:
            cleared = line.strip()

            text_list.append(cleared)
        print(text_list)
    return text_list

text_file()
#if __name__ == "__main__":
    #main()



