import typer
from cli import fib, fact, sort, stack, bench

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
        typer.echo("5. Benchmark")
        typer.echo("6. Exit")

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
                typer.echo("Sorting types: bubble, quick, counting, radix, bucket, heap")
                stype = input("Sorting type: ").strip()
                arr = input("Array: ").strip()
                sort(stype, arr)
            case "4":
                stack()
            case "5":
                bench()
            case "6":
                typer.echo("Exit")
                break
            case _:
                typer.echo("Unknown command")

if __name__ == "__main__":
    interactive()