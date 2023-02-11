from random import shuffle
from words import words


class Caesar:
    def __init__(self, s: str, n: int = 3) -> None:
        self.original = s.lower()
        self.code = ''.join(
            chr((ord(c) - ord('a') + n) % 26 + ord('a'))
            if c != ' ' else ' ' for c in self.original
        )
        self.numeric = [
            ord(c) - ord('a') + 1 if c != ' ' else 0 for c in self.code
        ]
        shuffle(self.numeric)


def main() -> None:
    all_encryptions: list[list[Caesar]] = [[], [], [], []]

    for word in words:
        if ' ' in word:
            level = 3
        elif len(word) <= 3:
            level = 0
        elif 3 < len(word) <= 6:
            level = 1
        else:
            level = 2

        all_encryptions[level].append(Caesar(word))

    for i, encryptions in enumerate(all_encryptions, 0):
        print(f'LEVEL {i}: {len(encryptions)} problems in total')
        for j, e in enumerate(encryptions, 1):
            print(f'    {i}_{j}: ', end='')
            print(f'{e.original} - {e.code} - {e.numeric}')
        else:
            print()


if __name__ == '__main__':
    main()
