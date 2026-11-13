def minNumberCoins(n: str) -> list[int]:
    n_int = int(n)
    c5 = 0

    # Если число нечётное, то оно содержит одну 5
    if n_int % 2 != 0:
        c5 = 1
        n_int -= 5

    c10 = n_int // 10
    c2 = (n_int - (c10 * 10)) // 2

    return [c10, c5, c2]
    

if __name__ == "__main__":
    n = '26'
    print(minNumberCoins(n))

    # Проверка всех вариантов
    # for a in range(4, 100):
    #     result = minNumberCoins(str(a))
    #     print(
    #         f"Total = {a} result = {result} "
    #         f"res = {a == 10 * result[0] + 5 * result[1] + 2 * result[2]}"
    #     )