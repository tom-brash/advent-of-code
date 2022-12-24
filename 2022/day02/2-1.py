def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    outcomes = {"A": {"X": 3, "Y": 6, "Z": 0}, "B": {"X": 0, "Y": 3, "Z": 6}, "C": {"X": 6, "Y": 0, "Z": 3}}

    raw_scores = {"X": 1, "Y": 2, "Z": 3} 

    total = 0

    for x in input:
        a, b = x.split(" ")
        
        total += raw_scores[b]
        total+= outcomes[a][b]
    print("Final total:", total)

if __name__ == "__main__":
    main()
