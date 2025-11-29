import typer

from src.fibos import fibo, fibo_recursive
from src.factorials import factorial, factorial_recursive
from src.bubble_sort import bubble_sort
from src.quick_sort import quick_sort
from src.counting_sort import counting_sort
from src.radix_sort import radix_sort
from src.bucket_sort import bucket_sort
from src.heap_sort import heap_sort
from src.stack_list import StackOnList
from src.benchmark import benchmark_sorts
from src.generators import *

app = typer.Typer(help="Lab3 algorithms: sorts, fibonacci, factorial, stack")


@app.command("fibo")
def fib(n: int, r: bool = typer.Option(False, "-r", "--recursive", help="Использовать рекурсию")):
    typer.echo(f"Result: {fibo_recursive(n) if r else fibo(n)}")


@app.command("factorial")
def fact(n: int, r: bool = typer.Option(False, "-r", "--recursive", help="Использовать рекурсию")):
    typer.echo(f"Result: {factorial_recursive(n) if r else factorial(n)}")


@app.command("sort")
def sort(name: str, array: str):
    """
    name: bubble, quick, counting, radix, bucket, heap
    array: числа через пробел, напр. "2 4 1 8"
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

@app.command("stack")
def stack():
    stck = StackOnList()
    while True:
        typer.echo("\nStack commands: push <x>, pop, peek, min, len, empty, print, exit")
        line = input("> ").strip().split()
        if not line:
            continue
        cmd, *args = line

        try:
            match cmd:
                case "push":
                    if not args:
                        typer.echo("Usage: push <int>")
                        continue
                    value = int(args[0])
                    stck.push(value)
                    typer.echo(f"pushed {value}")
                case "pop":
                    typer.echo(f"popped: {stck.pop()}")
                case "peek":
                    typer.echo(f"peek: {stck.peek()}")
                case "min":
                    typer.echo(f"minimal: {stck.min()}")
                case "len":
                    typer.echo(f"length: {len(stck)}")
                case "empty" | "is_empty":
                    typer.echo(f"is empty: {stck.is_empty()}")
                case "print":
                    typer.echo(f"stack: {stck.lst}")
                case "exit":
                    break
                case _:
                    typer.echo("Unknown stack command")
        except IndexError as err:
            typer.echo(f"{err}")
        except ValueError:
            typer.echo(f"Value must to be integer")

@app.command("benchmark")
def bench(n: int = 10000) -> dict[str, dict[str, float]]:
    arrays = {
        "random": rand_int_array(n, 0, 1000),
        "reversed": reverse_sorted(n),
        "many_duplicates": many_duplicates(n)
    }

    algos = {
        "bubble": bubble_sort,
        "quick": quick_sort,
        "counting": counting_sort,
        "radix": radix_sort,
        "bucket": bucket_sort,
        "heap": heap_sort,
    }

    results = benchmark_sorts(arrays, algos)

    for arr_name, times in results.items():
        print(f"\n=== {arr_name} ===")
        for algo_name, t in times.items():
            print(f"{algo_name:8s}: {t:.6f} s")

    return results

if __name__ == "__main__":
    app()