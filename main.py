import requests

def get_country_info():
    print("ПОШУК ІНФОРМАЦІЇ ПРО КРАЇНИ")
    country_name = input("Введіть назву країни англійською мовою: ").strip()

    if not country_name:
        print("Назва країни не може бути порожньою!")
        return

    url = f"https://restcountries.com/v3.1/name/{country_name}"

    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()[0]
            
            name = data.get("name", {}).get("common", "Немає даних")
            capital_list = data.get("capital", ["Немає даних"])
            capital = ", ".join(capital_list)
            population = data.get("population", "Немає даних")
            region = data.get("region", "Немає даних")
            
            currencies_data = data.get("currencies", {})
            currency_info = "Немає даних"
            if currencies_data:
                curr_code = list(currencies_data.keys())[0]
                curr_name = currencies_data[curr_code].get("name", "")
                curr_symbol = currencies_data[curr_code].get("symbol", "")
                currency_info = f"{curr_name} ({curr_symbol}) [{curr_code}]"

            print("\n" + "=" * 30)
            print(f"Країна: {name}")
            print(f"Столиця: {capital}")
            print(f"Населення: {population:,} чол.")
            print(f"Регіон: {region}")
            print(f"Валюта: {currency_info}")
            print("=" * 30)

        elif response.status_code == 404:
            print(
                f"\nПомилка 404: Країну '{country_name}' не знайдено. Перевірте правильність написання."
            )
        elif response.status_code == 401:
            print("\nПомилка 401: Помилка авторизації (невірний токен).")
        else:
            print(
                f"\nЩось пішло не так. Статус-код сервера: {response.status_code}"
            )

    except requests.exceptions.RequestException as e:
        print(f"\nПомилка з'єднання з інтернетом або сервером: {e}")


if __name__ == "__main__":
    get_country_info()