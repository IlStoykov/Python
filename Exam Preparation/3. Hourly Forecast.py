def forecast(*args):
    weather_dict = {}

    for item in args:
        location, weather = item[0], item[1]
        if location not in weather_dict:
           weather_dict[location] = weather

    result = {k:v for k, v in sorted(weather_dict.items(), key = lambda x: (x[1], x[0]))}
    sunny = ''
    cloudy = ''
    rainy = ''
    for k, v in result.items():
        if v == "Sunny":
            sunny += f"{k} - {v}\n"
        elif v == "Cloudy":
            cloudy += f"{k} - {v}\n"
        else:
            rainy += f"{k} - {v}\n"

    return sunny + cloudy + rainy

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

