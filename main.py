"""Решение задач по 2 лабораторной работе."""
import math


def multiplication_table():
    """Среднее № 1: вывести таблицу умножения от 1 до 10."""
    print("Таблица умножения:")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i * j}", end=" ")
        print()


def calculate_factorial(n):
    """Среднее № 2: вернуть факториал числа n."""
    result_factorial = math.factorial(n)
    print(f"Факторил числа {n} равен: {result_factorial}")
    return result_factorial


def prime_numbers():
    """Среднее № 5: вернуть список простых чисел до 100."""
    table_prime = []
    for n in range(2, 101):
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            table_prime.append(n)
    print("Простые числа до 100:", table_prime)
    return table_prime


def bubble_sort(arr):
    """Пов. сложность № 1: сортировка списка пузырьком."""
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        print(f"после прохода {i + 1}: {arr}")
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    multiplication_table()
    calculate_factorial(5)
    prime_numbers()
    bubble_sort([5, 1, 4, 2, 8])
