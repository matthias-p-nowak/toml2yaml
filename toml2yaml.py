#!/usr/bin/python3
import tomli, yaml, sys, json

def convert(fn: str):
    print(f"converting {fn}")
    if not fn.endswith('.toml'):
        print(f"{fn} does not end with '.toml'")
        return
    with open(fn,'r') as inp:
        data=tomli.load(inp)
    # print(f"got {data}")
    fn2=fn.replace('.toml','.yaml')
    with open(fn2,'wt') as out:
        yaml.safe_dump(data,out)
    print(f"wrote {fn2}")


if __name__ == "__main__":
    for fn in sys.argv[1:]:
        convert(fn)
