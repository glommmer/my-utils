import re


def split_chained_assignment(text: str) -> str:
    if text.count("=") > 1 and "==" not in text:
        val = ""
        var_lst = []
        text_objs = text.split("=")
        for seq, obj in enumerate(text_objs):
            obj = obj.strip()
            if re.fullmatch(r"[a-zA-Z_]{1}\w*", obj):
                var_lst.append(obj)
            else:
                val = "=".join(text_objs[seq:])
                break
        if var_lst:
            text = "\n".join([f"{var} = {val}" for var in var_lst])
    return text


if __name__ == "__main__":
    foo = "a = b = c = 1"
    res = split_chained_assignment(foo)
    print(res, "\n")

    foo = "a = b = func(param='var')"
    res = split_chained_assignment(foo)
    print(res, "\n")

    foo = "if foo == 'var':"
    res = split_chained_assignment(foo)
    print(res, "\n")
