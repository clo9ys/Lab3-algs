import typer
from src.fibos import fibo, fibo_recursive
from src.factorials import factorial, factorial_recursive
from src.bubble_sort import bubble_sort
from src.quick_sort import quick_sort
from src.counting_sort import counting_sort
from src.radix_sort import radix_sort
from src.bucket_sort import bucket_sort
from src.heap_sort import heap_sort

app = typer.Typer(help="Lab3 algorithms: sorts, fibonacci, factorial, stack")

@app.command("fibo")
def fib(n: int, r: bool = typer.Option(False, '-r', '--recursive', help="Использовать рекурсию")):
    """Вычисляет число Фибоначчи"""
    typer.echo(f"Result: {fibo_recursive(n) if r else fibo(n)}")

@app.command("factorial")
def fact(n: int, r: bool = typer.Option(False, '-r', '--recursive', help="Использовать рекурсию")):
    """Вычисляет факториал"""
    typer.echo(f"Result: {factorial_recursive(n) if r else factorial(n)}")

@app.command("sort")
def sort(name: str, array: str):
    """
    Сортирует массив значений.
    name: bubble, quick, counting, radix
    array: например "2,4,1,8"
    """
    arr = list(map(int, array.strip().split()))
    match name:
        case "bubble":
            typer.echo(f"Result: {bubble_sort(arr)}")
        case "quick":
            typer.echo(f"Result: {quick_sort(arr)}")
        case "counting":
            typer.echo(f"Result: {counting_sort(arr)}")
        case "radix":
            typer.echo(f"Result: {radix_sort(arr)}")
        case "bucket":
            typer.echo(f"Result: {bucket_sort(arr)}")
        case "heap":
            typer.echo(f"Result: {heap_sort(arr)}")
        case _:
            typer.echo("Unknown sort type")

def interactive():
    """
    Интерактивный режим: выбор команды и ввод параметров, повторяется до выхода.
    """
    while True:
        typer.echo("\nChoose action:")
        typer.echo("1. Fibonacci")
        typer.echo("2. Factorial")
        typer.echo("3. Sorts")
        typer.echo("4. Stack")
        typer.echo("5. Exit")

        cmd = input("> ").strip()
        match cmd:
            case "1":
                n = int(input("Input number: "))
                r = input("Recursive? (y/N): ").strip().lower() == "y"
                fib(n, r)
            case "2":
                n = int(input("Input number: "))
                r = input("Recursive? (y/N): ").strip().lower() == "y"
                fact(n, r)
            case "3":
                typer.echo("Sorting types: bubble, quick, counting, radix")
                stype = input("Sorting type: ").strip()
                arr = input("Array: ").strip()
                sort(stype, arr)
            case "4":
                pass # stack
            case "5":
                typer.echo("Exit")
                break
            case _:
                typer.echo("Unknown command")

if __name__ == "__main__":
    interactive()
