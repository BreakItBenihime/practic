    """Індекс першого елемента з найменшою довжиною."""
    k = 0
    for i in range(1, len(words)):
        if len(words[i]) < len(words[k]):
            k = i
    return k


def index_of_max(words):
    """Індекс першого елемента з найбільшою довжиною."""
    k = 0
    for i in range(1, len(words)):
        if len(words[i]) > len(words[k]):
            k = i
    return k


def read_words(n):
    while True:
        words = input(f"Введіть {n} слів через пробіл: ").split()
        if len(words) == n:
            return words
        print(f"Потрібно рівно {n} слів, спробуйте ще раз.")


def main():
    n = 15
    C = read_words(n)
    print("\nТекстовий масив C:")
    for i, w in enumerate(C, start=1):
        print(f"C[{i}] = {w} (довжина {len(w)})")
    imin = index_of_min(C)
    imax = index_of_max(C)
    print(f"\nНайкоротший елемент: C[{imin + 1}] = {C[imin]}, довжина {len(C[imin])}")
    print(f"Найдовший елемент: C[{imax + 1}] = {C[imax]}, довжина {len(C[imax])}")
    print("Сума довжин цих елементів =", len(C[imin]) + len(C[imax]))


if __name__ == "__main__":
    main()actic
