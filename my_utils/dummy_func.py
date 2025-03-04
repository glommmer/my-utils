from types import SimpleNamespace


def dummy_func(*args):
    """Return the input value as is"""
    if len(args) == 1:
        return args[0]
    return args


if __name__ == "__main__":
    _allowed = {
        "spark": SimpleNamespace(sql=dummy_func),
    }

    foo = " spark.sql('SELECT * FROM TABLE') "
    res = eval(foo, None, _allowed)

    print(res)
