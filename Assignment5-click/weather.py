import click

@click.command()
@click.option('--weather', type=click.Choice(['sunny','rainy','winter']))
def weather(weather):
    '''
    Print Weather
    '''
    print(f'Weather is {weather}')

if __name__=="__main__":
    weather()
