def get_weather(city):
    return f"The weather in {city} is sunny."

if __name__ == "__main__":
    city = input("Enter city: ")
    print(get_weather(city))
