from talon.voice import Context, Key
import os
from ..utils import is_filetype, snake_text

FILETYPES = (".py",)


PREFIX = "py"
ctx = Context("python", func=is_filetype(FILETYPES))
# ctx = Context("python")

ctx.keymap(
    {
        "state any": ["any()", Key("left")],
        "dunder in it": "__init__",
        "dot pie": ".py",
        "dot pipe": ".py",
        "self assign <dgndictation> [over]": [
            "self.",
            snake_text,
            " = ",
            snake_text,
            "\n",
        ],
        "star arguments": "*args",
        "star star K wargs": "**kwargs",

    # add some python keywords
    PREFIX + "and": "and",
    PREFIX + "az": "as",
    PREFIX + "assert": "assert",
    PREFIX + "break": "break",
    PREFIX + "class": "class",
    PREFIX + "continue": "continue",
    PREFIX + "def": "def",
    PREFIX + "del": "del",
    PREFIX + "elif": "elif",
    PREFIX + " else ": "else",
    PREFIX + "except": "except",
    PREFIX + "exec": "exec",
    PREFIX + "finally": "finally",
    PREFIX + "for": "for",
    PREFIX + "from": "from",
    PREFIX + "global": "global",
    PREFIX + "global": "global",
    PREFIX + "if": "if",
    PREFIX + "import": "import",
    PREFIX + "import": "import",
    PREFIX + " in": "in",
    PREFIX + "is": "is",
    PREFIX + "lambda": "lambda",
    PREFIX + "not": "not",
    PREFIX + "or": "or",
    PREFIX + "pass": "pass",
    PREFIX + "print": "print",
    PREFIX + "raise": "raise",
    PREFIX + "return": "return",
    PREFIX + " try": "try",
    PREFIX + "while": "while",
    PREFIX + "with": "with",
    PREFIX + "yield": "yield",

    # add some standard library packages
    PREFIX + "datetime": "datetime",
    PREFIX + "string": "string",
    # numeric types
    PREFIX + "int": "int",
    PREFIX + "float": "float",

    # set types
PREFIX + "set": "set",
PREFIX + "frozenset": "frozenset",
    # sequence types
PREFIX + "list": "list",
PREFIX + "tuple": "tuple",
PREFIX + "range": "range",
    #mapping types
PREFIX + "dict": "dict",

    # binary sequence types
PREFIX + "bytes": "bytes",
PREFIX + "bytearray": "bytearray",
    PREFIX + "memoryview": "memoryview",
    # context manager types
    PREFIX + "with": "with",
    # data types
    PREFIX + "datetime": "datetime",
    PREFIX + "calendar": "calendar",
    PREFIX + "collections": "collections",
    PREFIX + "collectionsabc": "collections.abc",

    PREFIX + "if main": "if __name__==__main__:"\
                 +os.linesep+ " main()",

    })
# TODO: defined function
# |ctx.keymap({


# |"def defun(m):[<dgndictation>] [over]":[
# |    name = '_'.join(m.dgndictation[0]),
# |    insert(f'def {name}():\n\t')],

    # ()}
# |)

# TODO: defined class
# TODO: python-ast
# TODO: don't overload tab for quinn snippet navigation
