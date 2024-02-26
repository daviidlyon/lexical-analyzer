import re
import sys

from constants import SYMBOLS_DICT, RESERVED_WORDS_LIST, SPECIAL_SYMBOLS_DICT


NUMBER_REGEX_PATTERN = r"^\d+\.?\d*$"

BOOLEANS_REGEX_PATTERN = r'"(true|false)"'

TXT_REGEX_PATTERN = r'".*?"'

SPECIAL_SYMBOLS_REGEX_PATTERN = r"(?:<=|>=|<>)"

SYMBOLS_REGEX_PATTERN = "|".join([re.escape(symbol[0]) for symbol in SYMBOLS_DICT])
SYMBOLS_REGEX_PATTERN = r"[" + SYMBOLS_REGEX_PATTERN + r"]"

ID_REGEX_PATTERN = r"^[^\W\d_]\w*$"

RESERVED_WORDS_REGEX_PATTERN = r"\b(?:" + "|".join(RESERVED_WORDS_LIST) + r")\b"

TOKEN_LIST = [
    ("tkn_number", re.compile(NUMBER_REGEX_PATTERN)),
    ("boolean", re.compile(BOOLEANS_REGEX_PATTERN, re.IGNORECASE)),
    ("tkn_text", re.compile(TXT_REGEX_PATTERN)),
    ("special_symbol", re.compile(SPECIAL_SYMBOLS_REGEX_PATTERN)),
    ("symbol", re.compile(SYMBOLS_REGEX_PATTERN)),
    ("reserved_word", re.compile(RESERVED_WORDS_REGEX_PATTERN)),
    ("id", re.compile(ID_REGEX_PATTERN)),
]


def classify_token(token, lex):
    if token == "special_symbol":
        return SPECIAL_SYMBOLS_DICT[lex]
    if token == "symbol":
        return SYMBOLS_DICT[lex]
    if token == "reserved_word":
        return lex
    if token == "boolean":
        new_string = lex[1:-1]
        return new_string.capitalize()
    return token


def aggregate_lex(token, lex):
    if token == "tkn_text":
        new_string = lex[1:-1]
        return new_string
    return lex


class Token:
    def __init__(self, token, lex, row, column):
        self.token = classify_token(token, lex)
        self.lex = aggregate_lex(token, lex)
        self.row = row
        self.column = column
        self.token_type = token

    def __str__(self):
        special_cases = ["special_symbol", "symbol", "reserved_word", "boolean"]
        if self.token_type in special_cases:
            return "<{}, {}, {}>".format(self.token, self.row, self.column)
        return "<{}, {}, {}, {}>".format(self.token, self.lex, self.row, self.column)


def lexical(user_input):
    lines = user_input.split("\n")
    abort_analysis = False
    for i in range(len(lines)):
        row = lines[i]
        j = 0

        while j < len(row):
            match = None
            # Ignore spaces
            if row[j] == " ":
                j += 1
                continue

            # Jump line if a comment is found
            if row[j] == "'":
                break

            line_end = len(row)
            break_loop = False
            while j <= line_end:
                word = row[j:line_end]

                for token_type, compiled_regex in TOKEN_LIST:
                    match = compiled_regex.match(word)
                    if match:
                        token_value = match.group()
                        token_end = match.end()
                        current_token = Token(token_type, token_value, i + 1, j + 1)

                        j += token_end

                        print(current_token)
                        break_loop = True
                        break

                if break_loop:
                    break
                line_end -= 1

            if not match:
                print(">>> Lexical Error (Line: {}, Pos: {})".format(i + 1, j + 1))
                abort_analysis = True
                break

        if abort_analysis:
            break


test_code = sys.stdin.read()
lexical(test_code)