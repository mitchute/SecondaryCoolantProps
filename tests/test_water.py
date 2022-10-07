from unittest import TestCase

from scp.water import Water
from tests.utilities import abs_error_passes as err


class TestWater(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.w = Water()

    def test_viscosity(self):
        self.assertTrue(err(self.w.viscosity(0), 0.001786896922, 0.01))
        self.assertTrue(err(self.w.viscosity(25), 0.000890469512, 0.01))
        self.assertTrue(err(self.w.viscosity(50), 0.000546859910, 0.01))
        self.assertTrue(err(self.w.viscosity(75), 0.000378127367, 0.01))
        self.assertTrue(err(self.w.viscosity(100), 0.000281878425, 0.01))
