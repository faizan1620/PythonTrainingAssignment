import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument('firstnum')
@click.argument('secondnum')
def sum(firstnum,secondnum):
    '''
       Return sum of two nos
    '''
    click.echo(int(firstnum)+int(secondnum))

@cli.command()
@click.argument('firstnum')
@click.argument('secondnum')
def difference(firstnum,secondnum):
    '''
       Return difference of two nos
    '''
    click.echo(int(firstnum)-int(secondnum))

@cli.command()
@click.argument('firstnum')
@click.argument('secondnum')
def product(firstnum,secondnum):
    '''
       Return multiplication of two nos
    '''
    click.echo(int(firstnum)*int(secondnum))

@cli.command()
@click.argument('firstnum')
@click.argument('secondnum')
def divide(firstnum,secondnum):
    '''
       Return division of two nos
    '''
    if int(secondnum) == 0:
        click.echo('Not divisible by 0')
        return
    click.echo(int(firstnum)/int(secondnum))


if __name__=="__main__":
    cli()