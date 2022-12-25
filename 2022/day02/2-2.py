def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    outcomes = {"A": {"X": "Z", "Y": "X", "Z": "Y"}, "B": {"X": "X", "Y": "Y", "Z": "Z"}, "C": {"X": "Y", "Y": "Z", "Z": "X"}}
    points = {"X": 0, "Y": 3, "Z": 6}
    raw_scores = {"X": 1, "Y": 2, "Z": 3} 

    total = 0

    for x in input:
        
        a, b = x.split(" ")
        total += points[b]
        total += raw_scores[outcomes[a][b]]
    print(f"\n(2-2) Following the amended strategy would yield: {total} points")

if __name__ == "__main__":
    main()
