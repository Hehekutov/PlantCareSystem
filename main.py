from datetime import date, timedelta


def get_next_watering(last_watering, interval):
    return last_watering + timedelta(days=interval)


def get_watering_status(next_watering, today):
    if next_watering < today:
        return "Полив просрочен"
    elif next_watering == today:
        return "Нужно полить сегодня"
    else:
        return "Поливать пока не нужно"


def mark_watering(today):
    print("Полив отмечен.")
    return today


def main():
    plant_name = "Фикус"
    # Учебный пример: растение поливали неделю назад.
    today = date.today()
    last_watering = today - timedelta(days=7)
    interval = int("7")

    print(f"Растение: {plant_name}")
    print(f"Сегодня: {today}")
    print(f"Последний полив: {last_watering}")
    print(f"Поливать раз в {interval} дней")

    next_watering = get_next_watering(last_watering, interval)
    print(f"Следующий полив: {next_watering}")
    print(get_watering_status(next_watering, today))

    answer = input("Вы уже полили растение? да/нет: ").strip().lower()
    is_watered = answer == "да"
    if is_watered:
        last_watering = mark_watering(today)
        next_watering = get_next_watering(last_watering, interval)
        print(f"Последний полив: {last_watering}")
        print(f"Следующий полив: {next_watering}")
        print(get_watering_status(next_watering, today))
    elif answer == "нет":
        print("Полив не отмечен.")
    else:
        print("Нужно ввести да или нет. Полив не отмечен.")


if __name__ == "__main__":
    main()
