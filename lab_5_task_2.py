def binary_search(low, high):
    if low > high:
        return 
    
    mid = (low + high) // 2

    resp = input(f"Число меньше {mid}? (да/нет): ").strip().lower()

    if resp == "да":
        binary_search(low, mid - 1)

    else:
        resp = input(f"Число больше {mid}? (да/нет): ").strip().lower()

        if resp == "да":
            binary_search(mid + 1, high)
        
        else:
            print("Нашел число")

user_input = int(input("Введите число от 1 до 100: "))

if user_input >= 1 and user_input <= 100:
    print("Число корректно")
    print("Начинаю угадывать Ваше число:")
    binary_search(1, user_input)
else:
    print("Число вне диапазона")


