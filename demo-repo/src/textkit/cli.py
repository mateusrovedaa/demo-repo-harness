import sys

from textkit.slug import slugify


def main() -> int:
    if len(sys.argv) < 2:
        print("uso: textkit <texto>", file=sys.stderr)
        return 2
    print(slugify(" ".join(sys.argv[1:])))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
