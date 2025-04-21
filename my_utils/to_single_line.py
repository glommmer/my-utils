import os
import sys
from pathlib import Path

sys.path.append(str(Path(os.path.realpath(__file__)).parent))

import re
from my_utils import get_outer_brackets


def to_single_line(text: str) -> str:
    text = re.sub(r"\\[\n\r]+", " ", text)
    text = re.sub(r"\s+\.", ".", text)

    multiline_pattern = re.compile(r'""".*?"""', flags=re.DOTALL)
    multiline_matches = multiline_pattern.findall(text)
    for match in multiline_matches:
        singleline = re.sub(r"\n\s*", " ", match)
        tmp_match_asis = re.search(r'"""(.+)"""', singleline).group(1)
        if '"' in tmp_match_asis:
            tmp_match_tobe = tmp_match_asis.replace('"', "'")
            singleline = singleline.replace(tmp_match_asis, tmp_match_tobe, 1)
        text = text.replace(match, singleline)
    text = text.replace('"""', '"')
    text = re.sub(r" +", " ", text)

    bracket_objects = get_outer_brackets(text)
    if bracket_objects:
        for obj in bracket_objects:
            obj = re.escape(obj)
            match = re.search(obj, text, flags=re.DOTALL).group()
            if "\n" in match:
                singleline = match.replace("\n", " ")
                text = text.replace(match, singleline, 1)
    return text


if __name__ == "__main__":
    foo = """
        \"\"\"
        SELECT *
          FROM TABLE
        \"\"\"
        spark = SparkSession\
                .builder\
                .getOrCreate()
        s3.head_object(
            Bucket="My-Bucket",
            Key="path/to/key",
        )
    """
    var = to_single_line(foo)
    print(var)
