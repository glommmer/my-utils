def get_outer_brackets(text: str) -> list:
    brackets = {"(": ")", "[": "]", "{": "}"}
    quotes = ["'", '"']
    bracket_objects = []
    in_bracket = False
    in_string = False
    start_index = 0
    opening_bracket_index = 0
    closing_bracket_index = 0
    closing_bracket = ""
    closing_quote = ""
    for idx, char in enumerate(text):
        if char in quotes:
            if not in_string:
                closing_quote = char
                in_string = True
            elif in_string and char == closing_quote:
                in_string = False
            continue
        if not in_string:
            if char in brackets:
                opening_bracket_index += 1
                if not in_bracket:
                    in_bracket = True
                    closing_bracket = brackets[char]
                    start_index = idx
            elif char in brackets.values():
                closing_bracket_index += 1
                if (
                    in_bracket
                    and char == closing_bracket
                    and opening_bracket_index == closing_bracket_index
                ):
                    opening_bracket_index = 0
                    closing_bracket_index = 0
                    in_bracket = False
                    end_index = idx + 1
                    bracket_objects.append(text[start_index:end_index])
    return bracket_objects


if __name__ == "__main__":
    foo = """
        foo = ["var1", "var2"]
        foo.append(var3.strip().upper())
        foo = {"(": ")", "[": "]", "{": "}"}
        foo.get("[", [1, 2, 3])
    """
    var = get_outer_brackets(foo)
    print(var)