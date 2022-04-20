#Import Click Lib
import click

#Import Tabulate
import tabulate

#Import Kreate_Create Modules
import os
import sys

#Functions
def lang_table():
    table_data = [
        ['Python', 'Supported'],
        ['Javascript', 'Unsuported',],
        ['NodeJS', 'Under Dev'],
    ]
    
    print(tabulate.tabulate(table_data, headers=["Lang", "Support"]))

def create_prj():
    #Step1:
    prj_name = input("Project Name: ")
    #Step2:
    


#Create Click Group
@click.group()
def cli():
    pass

# --langs
@click.command()
@click.option('--langs', default=1, help='Display a Language Support Table')
def langs(langs):
    click.echo(lang_table())
    
# --create-project
@click.command()
@click.option('--c', default=1, help='Create a new project!')
def create(create):
    click.echo('Create Command')
    
cli.add_command(langs)
cli.add_command(create)

cli()