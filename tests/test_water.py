from unittest import TestCase

from scp.water import Water


class TestWater(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.w = Water()

    def test_viscosity(self):
        self.assertAlmostEqual(self.w.viscosity(0), 0.001786896922, 4)
        self.assertAlmostEqual(self.w.viscosity(25), 0.000890469512, 4)
        self.assertAlmostEqual(self.w.viscosity(50), 0.000546859910, 4)
        self.assertAlmostEqual(self.w.viscosity(75), 0.000378127367, 4)
        self.assertAlmostEqual(self.w.viscosity(100), 0.000281878425, 4)
