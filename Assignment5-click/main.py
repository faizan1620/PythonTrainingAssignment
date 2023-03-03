import click

@click.command()
@click.argument('name')
@click.option('--number', prompt='Number count please', help='number of greetings')
def main(name,number):
    '''
    Print Hello from {name} upto {number} times
    '''
    for i in range(int(number)):
        click.echo(click.style(f'Hello from {name}', bg='red', fg='white'))  # Formatting output text using click

if __name__=="__main__":
    main()

