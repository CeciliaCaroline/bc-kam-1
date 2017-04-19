import requests
import click


@click.command()
@click.option('--city', prompt='Enter your city',
              help='Name of the city.')
def cli(city):
    r = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=c23bdd3c920067eecb8bd0fa3ab4b6dc')

    if r.status_code == 200:
        weather_json = r.json()

        main = weather_json['main']
        temp = str(main['temp'])
        pressure = str(main['pressure'])
        humidity = str(main['humidity'])

        wind = weather_json['wind']
        wind_speed = str(wind['speed'])

        city = weather_json['name']

        weather_today = '\nToday`s weather in ' + city + ' is \n' + 'Temperature: ' + temp + '\n' + 'Pressure: ' + pressure \
                        + '\n' + 'Humidity: ' + humidity + '\n' + 'Wind speed: ' + wind_speed + '\n\n' + '----Thank you---'

        click.echo(weather_today)
    else:
        click.echo("An error occurred, please check your input")
