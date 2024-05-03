from app import read_file


def main():
    while True:
        cmd = input('\nВведите команду\n')
        if cmd == '--read':
            read_file()


if __name__ == '__main__':
    main()
