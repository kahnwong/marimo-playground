import marimo

__generated_with = "0.10.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    foo = 3
    print(foo)
    return (foo,)


@app.cell
def _():
    import polars as pl

    return (pl,)


@app.cell
def _(pl):
    df = pl.DataFrame([{"a": 1, "b": "foo"}, {"a": 2, "b": "bar"}])
    print(df)
    return (df,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
