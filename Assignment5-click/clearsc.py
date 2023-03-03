# clearsc command for clearing the screen
import click

@click.command()
def cli():
    '''
        Clears the screen
    '''
    click.clear()

if __name__=='__main__':
    cli()