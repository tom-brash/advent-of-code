from collections import defaultdict

def main():
    with open('day9/9.txt', 'r') as open_file:
        stream_data = open_file.read()
    
    stream = Stream(stream_data)
    stream.score()
    
class Stream:
    def __init__(self, stream_data):
        self.stream_data = [c for c in stream_data]
    
    def score(self):
        level = 1
        score = 0
        mode = 'normal'
        skip = False
        for c in self.stream_data:
            if skip:
                skip = False
                continue

            if c == '!':
                skip = True
                continue

            if mode == 'garbage':
                if c == '>':
                    mode = 'normal'
                    continue
                else:
                    continue

            if c == '{':
                score += level
                level += 1
            elif c == '}':
                level -= 1
            elif c == '<':
                mode = 'garbage'
        print('Score:', score)

if __name__ == '__main__':
    main()