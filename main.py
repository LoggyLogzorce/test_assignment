def minNumberCoins(n: str) -> list[int]:
    n_int = int(n)

    # Если чисто чётное, то для него не нужны монеты наминалом 5
    if n_int % 2 == 0:
        c10 = n_int // 10
        c2 = (n_int - (c10 * 10)) // 2
        return [c10, 0, c2]

    # Если число нечётное, то понадобится только одна монета наминалом 5
    # так как две 5 заменяются десяткой
    c10 = (n_int - 5) // 10
    c2 = (n_int - (c10 * 10) - 5) // 2
    return [c10, 1, c2]
    

if __name__ == "__main__":
    n = '26'
    print(minNumberCoins(n))

    # Проверка всех вариантов
    # for a in range(4, 100):
    #     result = minNumberCoins(str(a))
    #     if a == (10 * result[0] + 5 * result[1] + 2 * result[2]):
    #         print("Total = ", a, "result = ", result, "res = ", True)
    #     else:
    #         print("Total = ", a, "result = ", result, "res = ", False)
