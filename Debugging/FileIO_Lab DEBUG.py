import os, statistics

def main():
    f1 = input("Enter a filename: ").strip()
    if os.path.isfile(f1):
        inFile = open(f1, "r")
        al = inFile.read()
        scores = [ eval(i) for i in al.split() ]

        print("Calculating data from the file...\n")
        print("There are", len(scores), "scores")
        print("The total is", sum(scores))
                      
        mean = sum(scores) / len(scores)
        print("The mean is %.2f" % (mean))
                      
        medians = statistics.median(scores)
        print("The median is", medians)
        inFile.close()
    else:
        print("Failed to open file!")
        

main()


