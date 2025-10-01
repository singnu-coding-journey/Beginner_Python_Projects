def multiplication_table():
    for i in range(1, 11):
        print(f"\nTable of {i}")
        for p in range(1, 11):
            print(f"{i} x {p} = {i * p}")

multiplication_table()
