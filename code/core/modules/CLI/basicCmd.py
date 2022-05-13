import click


@click.command()
def mgraf():
    click.echo('WELCOME TO MIND-GRAF!')

@click.command()
@click.option('-e',is_flag=True, show_default=True, default=False, help="Show Entities.")
@click.option('-r',is_flag=True, show_default=True, default=False, help="Show Avalibale Relations.")
@click.option("-f",is_flag=True, show_default=True, default=False, help="Show Avalibale Frames.")
def show(e,r,f):
    if e:
        click.echo('Showing Entities!')
    elif r:
        click.echo('Showing Relations!')
    elif f:
        click.echo('Showing Frames!')
    else: 
         click.echo('Options And/Or Argumets not provided. Use show --help for clarification! ')
    pass




@click.command()
@click.option('-c',is_flag=True, show_default=True, default=False, help="To Define Contexts.")
@click.option('-r',is_flag=True, show_default=True, default=False, help="To Define Relations.")
@click.option('-a',is_flag=True, show_default=True, default=False, help="To Define Attribiutes.")
@click.option('-p',is_flag=True, show_default=True, default=False, help="To Define Paths.")
def define(c,r,a,p):
    if c:
        click.echo('Defining Context!')
    elif r:
        click.echo('Defining Relations!')
    elif a:
        click.echo('Defining Attribiute!')
    elif p:
        click.echo('Defining Path!')
    pass





@click.command()
@click.option('-c',is_flag=True, show_default=True, default=False, help="To Remove Certain Contexts.")
@click.option('-r',is_flag=True, show_default=True, default=False, help="To Remove Certain Relations.")
@click.option('-a',is_flag=True, show_default=True, default=False, help="To Remove Certain Attribiutes.")
@click.option('-p',is_flag=True, show_default=True, default=False, help="To Remove Certain Paths.")
def remove(c,r,a,p):
    if c:
        click.echo('Removinf Context!')
    elif r:
        click.echo('Removing Relations!')
    elif a:
        click.echo('Removing Attribiute!')
    elif p:
        click.echo('Removing Path!')
    pass



@click.command()
@click.option('-all',is_flag=True, show_default=True, default=False, help="Clear KnowledgeBase.")
def clear(all):
    if all:
        click.echo('Clearing KB from all asseted attribiutes!')
  




@click.command()
@click.option('-b',is_flag=True, show_default=True, default=False, help="Trace Using Forward-Chaining.")
@click.option('-f',is_flag=True, show_default=True, default=False, help="Trace Using Backward-Chaining.")
def trace(b,f):
    if b:
        click.echo('Backward Chaining Applied')
    elif f:
        click.echo('Forward Chaining Applied')
  