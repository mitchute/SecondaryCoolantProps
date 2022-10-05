from pathlib import Path
from sys import argv, path

# use the ghe import as a flag for determining whether we need to add to path
try:
    import ghe  # noqa: F401
except ImportError:
    # we are probably in VSCode or some other development setup
    # just add the root of the repo to path just like it will be in deployment
    root_dir = Path(__file__).parent.parent.resolve()
    path.insert(0, str(root_dir))

from ghe.library import MathLibrary


def main_cli():
    try:
        i = int(argv[1])
        m = MathLibrary(1)
        y = m.add(i)
        print(f"Thanks for using the GHE library!  We added 1 + {i} and got {y}")
        return y
    except IndexError:
        print("Bad command line, need to pass one argument, an integer")
    except ValueError:
        print("Bad command line argument, needs to be an integer")


if __name__ == "__main__":
    main_cli()
