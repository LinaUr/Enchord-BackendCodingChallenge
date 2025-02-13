import sys




def tetris(input_line: str) -> int:

    # Example logic: Count the number of blocks (Q0, Q1, etc.) in the input
    blocks = input_line.split(',')

    return str(len(blocks) * 2)  # Example: return double the number of blocks

def main():
    input_line = sys.stdin.readline().strip()
    result = tetris(input_line)
    sys.stdout.write(str(result))
    sys.exit(0)


if __name__ == "__main__":
    main()
