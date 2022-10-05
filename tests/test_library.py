from pathlib import Path
from sys import path
from unittest import TestCase

# use the ghe import as a flag for determining whether we need to add to path
try:
    import ghe
except ImportError:
    # we are probably in VSCode or some other development setup
    # just add the root of the repo to path just like it will be in deployment
    root_dir = Path(__file__).parent.parent.resolve()
    path.insert(0, str(root_dir))


from ghe.library import add

class TestLibraryAdd(TestCase):

    def test_add(self):
        y = add(2, 1)
        self.assertEqual(3, y)
