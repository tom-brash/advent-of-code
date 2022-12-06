import re
def main():
    with open('day9/9.txt', 'r') as open_file:
        code = open_file.read()

    print(get_length(code))

    # current_length = len(code)
    # while True:
    #     code = decompress(code)
    #     print(len(code))
    #     if len(code) == current_length:
    #         break
    #     current_length = len(code)
    
    # print(len(code))

def get_length(code):
    n = 0
    l = 0
    while n < len(code):
        if code[n] == '(':
            current_marker = re.match(r'\((\d+)x(\d+)\)', code[n:])
            n += len(current_marker.group(0))
            l += int(current_marker.group(2)) * get_length(code[n: n + int(current_marker.group(1))])
            n += int(current_marker.group(1))
        else:
            l += 1
            n += 1
    return l


# def decompress(code):
#     decompressed = ''
#     n = 0
#     while n < len(code):
#         if code[n] == '(':
#             current_marker = re.match(r'\((\d+)x(\d+)\)', code[n:])
#             n += len(current_marker.group(0))
#             for i in range(int(current_marker.group(2))):
#                 decompressed += code[n: n + int(current_marker.group(1))]
#             n += int(current_marker.group(1))
#         else:
#             decompressed += code[n: n + 1]
#             n += 1
#     return decompressed



if __name__ == '__main__':
    main()