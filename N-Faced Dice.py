def get_user_location():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        return data
    except requests.RequestException:
        return None

def main():
    user_location = get_user_location()
    if user_location:
        city = user_location.get('city')
        if city:
            name = input(f"Hello from {city}! What is your name? ")
            print(f"Hello, {name}!")
        else:
         name = input("Hello! What is your name? ")
         print(f"Hello, {name}!")
    else:
        name = input("Hello! What is your name? ")
        print(f"Hello, {name}!")

if name == "main":
    main()