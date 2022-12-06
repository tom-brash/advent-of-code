def main():
    with open('4/4.txt', 'r') as open_file:
        input_data = open_file.read().split('\n\n')
    
    bingo_cards = []
    for i in range(1, len(input_data)):
        bingo_cards.append(Bingo(input_data[i]))

    
    calls = input_data[0].split(',')
    called = set()
    for c in calls:
        called.add(c)
        print(called)
        for bingo in bingo_cards:
            if bingo.check(called):
                print('Uncalled: ', bingo.uncalled(called))
                print(bingo.uncalled(called) * int(c))
                break
    print('Hi')


class Bingo:
    def __init__(self, data):
        self.rows = []
        self.cols = []
        self.nums = []
        for i in data.split('\n'):
            self.rows.append(i.split())
            for n in i.split():
                self.nums.append(n)
        for i in range(5):
            col = []
            for r in data.split('\n'):
                col.append(r.split()[i])
            self.cols.append(col)
    
    def check(self, nums):
        for row in self.rows:
            if set(row).issubset(nums):
                return True
        for col in self.cols:
            if set(col).issubset(nums):
                return True

    def uncalled(self, nums):
        uncalled = [int(n) for n in self.nums if n not in nums]
        return sum(uncalled)

if __name__ == '__main__':
    main()