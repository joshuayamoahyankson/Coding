import csv

def main():
    with open("hymns.csv", "rt") as filename:
        reader = csv.reader(filename)
        for i in reader:
            print (i)
if __name__ == "__main__":
    main()