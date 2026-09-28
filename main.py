"""Решение задач по 2 лабораторной работе."""
import math


def multiplication_table():
    """Среднее № 1: вернуть таблицу умножения как список строк."""
    print("Таблица умножения:")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i * j}", end=" ")
        print()


def calculate_factorial(n):
    """Среднее № 2: вернуть факторил числа."""
    result_factorial = math.factorial(n)
    print(f"Факторил числа {n} равен: {result_factorial}")
    return result_factorial


def prime_numbers():
    """Среднее № 3: Список простых чисел до 100."""
    table_prime = []
    for n in range(2, 101):
        count = 0
        for i in range(1, n+1):
            if n % i == 0:
                count += 1
        if count == 2:
            table_prime.append(n)
    print("Простые числа до 100: ", table_prime)


if __name__ == "__main__":
    multiplication_table()
    calculate_factorial(5)
    prime_numbers()
