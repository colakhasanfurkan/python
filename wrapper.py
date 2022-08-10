import textwrap

def wrap(string, max_width):
    # add '\n' charachter after every 4 elements of array
    return"\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)