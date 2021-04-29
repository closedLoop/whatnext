import typer
from colorama import init
from termcolor import colored
from colorama import Fore, Back, Style
from tabulate import tabulate
import pyfiglet

# Coloring https://pypi.org/project/colorama/
init(autoreset=True)

# https://github.com/pwaller/pyfiglet
banner = pyfiglet.figlet_format("What Next")
print(colored(banner, "green"))

app = typer.Typer()

print(colored("Hello, World!", "green", "on_red"))
print(Fore.RED + "some red text")
print(Back.GREEN + "and with a green background")
print(Style.DIM + "and in dim text")
print(Style.RESET_ALL)
print("back to normal now")


# https://pypi.org/project/tabulate/
table = [
    ["Sun", 696000, 1989100000],
    ["Earth", 6371, 5973.6],
    ["Moon", 1737, 73.5],
    ["Mars", 3390, 641.85],
]
print(tabulate(table))


@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


def main():
    app()


if __name__ == "__main__":
    main()
