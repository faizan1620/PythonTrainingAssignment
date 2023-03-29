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
    try:
        click.echo(int(firstnum)+int(secondnum))
    except Exception as e:
        click.echo(e)

@cli.command()
@click.argument('firstnum')
@click.argument('secondnum')
def difference(firstnum,secondnum):
    '''
       Return difference of two nos
    '''
    try:
        click.echo(int(firstnum)-int(secondnum))
    except Exception as e:
        click.echo(e)

@cli.command()
@click.argument('firstnum')
@click.argument('secondnum')
def product(firstnum,secondnum):
    '''
       Return multiplication of two nos
    '''
    try:
        click.echo(int(firstnum)*int(secondnum))
    except Exception as e:
        click.echo(e)

@cli.command()
@click.argument('firstnum')
@click.argument('secondnum')
def divide(firstnum,secondnum):
    '''
       Return division of two nos
    '''
    try:
        if int(secondnum) == 0:
            click.echo('Not divisible by 0')
            return
        click.echo(int(firstnum)/int(secondnum))
    except Exception as e:
        click.echo(e)


if __name__=="__main__":
    cli()