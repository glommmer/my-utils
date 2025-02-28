def remove_sql_comments(text: str, comment_string: str = "--") -> str:
    result = ""
    in_string = False
    escape_next = False
    text = text.replace(r"\r", "")
    quotes = ["'", '"']
    this_quote = ""
    for i in range(len(text)):
        if escape_next and text[i] != "\\":
            result += text[i]
            escape_next = False
        elif text[i] == "\\":
            result += text[i]
            escape_next = True
        elif not in_string and text[i: i + len(comment_string)] == comment_string:
            i = text.find("\n", i)
            if i == -1:
                break
        elif text[i] in quotes:
            if not in_string:
                in_string = True
                this_quote = text[i]
            elif in_string and text[i] == this_quote and not escape_next:
                in_string = False
            result += text[i]
        else:
            result += text[i]
    return result


if __name__ == "__main__":
    foo = """
        SELECT ID -- EMP ID
             , NM -- EMP NAME
             , CONCAT('#--', ID) AS KEY -- JOIN KEY
             , CONCAT('\\'', NM) AS DEC -- SOMETHING
          FROM EMP_TBL
    """
    for line in foo.splitlines():
        var = remove_sql_comments(line)
        print(var)