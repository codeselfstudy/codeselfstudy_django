"""
This script was intended to be run just once, but it's left here in case
anyone wants to use it to generate other kinds of fixtures.
"""
languages = [
    "agda",
    "bf",
    "c",
    "cfml",
    "clojure",
    "cobol",
    "coffeescript",
    "commonlisp",
    "coq",
    "cpp",
    "crystal",
    "csharp",
    "dart",
    "elixir",
    "elm",
    "erlang",
    "factor",
    "forth",
    "fortran",
    "fsharp",
    "go",
    "groovy",
    "haskell",
    "haxe",
    "idris",
    "java",
    "javascript",
    "julia",
    "kotlin",
    "lean",
    "lua",
    "nasm",
    "nim",
    "objc",
    "ocaml",
    "perl",
    "php",
    "powershell",
    "prolog",
    "purescript",
    "python",
    "r",
    "racket",
    "raku",
    "reason",
    "ruby",
    "rust",
    "scala",
    "shell",
    "solidity",
    "sql",
    "swift",
    "typescript",
    "vb",
]


def render_yaml(pk, language_name):
    return f"""
- model: languages.language
  pk: {pk}
  fields:
      name: {language_name}
      description:
    """.strip()


if __name__ == "__main__":
    output = []
    for idx, lang in enumerate(languages):
        output.append(render_yaml(idx + 1, lang))

    with open("languages.yaml", "w") as f:
        f.write("\n".join(output))
