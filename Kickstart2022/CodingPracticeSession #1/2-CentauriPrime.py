vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

def get_ruler(kingdom):
    if kingdom[-1] == 'y' or kingdom[-1] == 'Y':
        return "nobody"
    elif kingdom[-1] in vowels:
        return "Alice"
    else:
        return "Bob"

def main():
    T = int(input())
    for t in range(T):
        kingdom = input()
        print('Case #%d: %s is ruled by %s.' % (t + 1, kingdom, get_ruler(kingdom)))

if __name__ == '__main__':
    main()
