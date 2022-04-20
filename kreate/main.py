#Import Click Lib
import click

#Import Tabulate
import tabulate

#Import Kreate_Create Modules
import os
import sys
import time

#Template Modules
from generate import gen

#Functions
def lang_table():
    table_data = [
        ['Python', 'Under Dev'],
        ['Website', 'Under Dev',],
        ['PHP', 'Under Dev'],
        ['Go', 'Under Dev'],
        ['NodeJS', 'Under Dev'],
        ['Ruby', 'Under Dev'],
        ['C#', 'Under Dev'],
        ['C++', 'Under Dev'],
        ['Rust', 'Under Dev']
    ]
    
    print(tabulate.tabulate(table_data, headers=["Lang", "Support"]))

def create_prj():
    #Step1:
    prj_name = input("Project Name: ")
    #Step2:
    prj_vers = input("Version (1.0.0): ")
    #Step4:
    print(
        "Select a Language: " + "\n" +
        "1. Python" + "\n"
        "2. Website" + "\n"
        "3. PHP" + "\n"
        "4. Go" + "\n"
        "5. NodeJS" + "\n"
        "6. Ruby" + "\n"
        "7. C#" + "\n"
        "8. C++" + "\n"
        "9. Rust" + "\n"
    )
    prj_lang = input('Select a Language: ')
    
    #Step4(Logic)
    if prj_lang == 1:   #Python
        gen.python()
    elif prj_lang == 2: #Website
        gen.website()
    elif prj_lang == 3: #PHP
        gen.php()
    elif prj_lang == 4: #Go
        gen.go()
    elif prj_lang == 5: #NodeJS
        gen.nodejs()
    elif prj_lang == 6: #Ruby
        gen.ruby()
    
    print("Generating " + prj_name + "@V." + prj_vers)
    time.sleep(2)
    
    #Print All:
    os.system('cls')
    print("[Project Name]: " + prj_name + "\n" + "[Project Version]: " + prj_vers + "\n" + "[Project Language]: " + prj_lang)
    


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
@click.option('--create', default=1, help='Create a new project!')
def create(create):
    click.echo(create_prj())
    
cli.add_command(langs)
cli.add_command(create)

cli()