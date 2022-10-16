from typing import Tuple

from scp.base_melinder import BaseMelinder


class EthyleneGlycol(BaseMelinder):
    """
    A derived fluid class for ethylene glycol and water mixtures
    """

    def coefficient_viscosity(self) -> Tuple:
        return (
            (4.7050e-01, -2.5500e-02, 1.7820e-04, -7.6690e-07),
            (2.4710e-02, -1.1710e-04, 1.0520e-06, -1.6340e-08),
            (3.3280e-06, 1.0860e-06, 1.0510e-08, -6.4750e-10),
            (1.6590e-06, 3.1570e-09, 4.0630e-10),
            (3.0890e-08, 1.8310e-10),
            (-1.8650e-09,),
        )

    def coefficient_specific_heat(self) -> Tuple:
        return (
            (3.7370e03, 2.9300e00, -4.6750e-03, -1.3890e-05),
            (-1.7990e01, 1.0460e-01, -4.1470e-04, 1.8470e-7),
            (-9.9330e-02, 3.5160e-04, 5.1090e-06, -7.1380e-08),
            (2.6100e-03, -1.1890e-06, -1.6430e-7),
            (1.5370e-05, -4.2720e-07),
            (-1.6180e-06,),
        )

    def coefficient_conductivity(self) -> Tuple:
        return (
            (4.7200e-01, 8.9030e-04, -1.0580e-06, -2.7890e-09),
            (-4.2860e-03, -1.4730e-05, 1.0590e-07, -1.1420e-10),
            (1.7470e-05, 6.8140e-08, -3.6120e-09, 2.3650e-12),
            (3.0170e-08, -2.4120e-09, 4.0040e-11),
            (-1.3220e-09, 2.5550e-11),
            (2.6780e-11,),
        )

    def coefficient_density(self) -> Tuple:
        return (
            (1.0340e03, -4.7810e-01, -2.6920e-03, 4.7250e-06),
            (1.3110e00, -6.8760e-03, 4.8050e-05, 1.6900e-08),
            (7.4900e-05, 7.8550e-05, -3.9950e-07, 4.9820e-09),
            (-1.0620e-04, 1.2290e-06, -1.1530e-08),
            (-9.6230e-07, -7.2110e-08),
            (4.8910e-08,),
        )

    def __init__(self, x: float) -> None:
        """
        Constructor for an ethylene glycol mixture instance

        @param x: Concentration fraction, from 0 to 0.6
        """

        super().__init__(0.0, 100, x, 0.0, 0.6)
        self.t_min = self.t_freeze = self.calc_freeze_point(x)

        self.x_base = 30.8462
        self.t_base = 31.728

    def calc_freeze_point(self, x: float) -> float:
        """
        Calculate the freezing point temperature of the mixture

        Based on a curve fit of the Ethylene Glycol freezing points
        listed in Chapter 31, Table 4 of the ASHRAE Handbook of Fundamentals, 2009

        @param x: Concentration fraction, from 0 to 0.6
        """

        # should return 0 C for low concentrations
        if x < 0.05:
            return 0

        # polynomial fit
        # t_f = a + b * conc + c * conc**2 + d * conc**3
        x = self._check_concentration(x)
        coefficient_freeze = [5.4792e-02, -2.9922e-01, -2.7478e-03, -9.5960e-05]
        c_pow = [x**p for p in range(4)]
        return sum(i * j for i, j in zip(coefficient_freeze, c_pow))

    @property
    def fluid_name(self) -> str:
        """
        Returns a descriptive title for this fluid
        @return: "EthyleneGlycol"
        """
        return "EthyleneGlycol"
