import sys

from textkit.slug import slugify


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if not args:
        print("uso: textkit <texto>", file=sys.stderr)
        return 2
    print(slugify(" ".join(args)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
