import typer

app = typer.Typer()


@app.command()
def hi(name: str):
    print(f"hi {name}")


def main():
    app()