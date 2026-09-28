def multiplication_table():
    for i in range (1, 11):
        for j in range(1, 11):
            print(f"{i * j}", end="")
        print()


if __name__ == "__main__":
    multiplication_table
