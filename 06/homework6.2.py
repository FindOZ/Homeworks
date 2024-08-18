s = int(input("Введіть кількість секунд: "))
if 0 <= s > 8640000:
    print("Введене число не знаходиться в допустимому діапазоні")
else:
    d, remaining_seconds = divmod(s, 86400)
    h, remaining_seconds = divmod(remaining_seconds, 3600)
    m, remaining_seconds = divmod(remaining_seconds, 60)
    s = remaining_seconds

    h_str = str(h).zfill(2)
    m_str = str(m).zfill(2)
    s_str = str(s).zfill(2)

    if d == 1:
        d_str = "день"
    elif 2 <= d <= 4:
        d_str = "дні"
    else:
        d_str = "днів"

    print(f"{d} {d_str}, {h_str}:{m_str}:{s_str}")
