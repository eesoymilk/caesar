from random import shuffle, sample
from words import words


class Caesar:
    def __init__(self, s: str, n: int = 3) -> None:
        self.original = s.lower()

        self.code = ''.join(
            chr((ord(c) - ord('a') + n) % 26 + ord('a'))
            if c != ' ' else ' ' for c in self.original
        )       
        
        self.ladder_code = ''.join(
            chr((ord(c) - ord('a') + i) % 26 + ord('a')) if c != ' ' else ' '
            for i, c in enumerate(self.original)
        )

        self.numeric = [
            ord(c) - ord('a') + 1 if c != ' ' else 0 for c in self.code
        ]
        shuffle(self.numeric)


def generate_codes(n: int = 3) -> list[list[Caesar]]:
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

    return all_encryptions


def all_result(n: int = 3) -> None:
    for i, encryptions in enumerate(generate_codes(n), 0):
        print(f'LEVEL {i}: {len(encryptions)} problems in total')
        for j, e in enumerate(encryptions, 1):
            print(f'    {i}_{j}:', end='')
            print(f'{e.original} - {e.code} - {e.numeric}')
        else:
            print()

        
def generate_problems(n: int = 3) -> None:
    print(f'n = {n}')
    
    for level, pset in enumerate(generate_codes(n)[1:], 1):
        print(f'{level = }')
        for i, problem in enumerate(sample(pset, 3), 1):
            print(f'Q{i}: {problem.code}')
            print(f'A{i}: {problem.original}\n')
        print()


def generate_chanllenges(n: int = 3) -> None:
    print(f'n_i = {n} + i, starting at i = 0')
    
    for level, pset in enumerate(generate_codes(n)[1:], 1):
        print(f'{level = }')
        for i, problem in enumerate(sample(pset, 3), 1):
            print(f'Q{i}: {problem.ladder_code}')
            print(f'A{i}: {problem.original}\n')
        print()


if __name__ == '__main__':
    generate_problems()
