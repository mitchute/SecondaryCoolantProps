from typing import Tuple

from scp.base_melinder import BaseMelinder


class MethylAlcohol(BaseMelinder):
    """
    A derived fluid class for methyl alcohol and water mixtures
    """

    def coefficient_viscosity(self) -> Tuple:
        return (
            (1.1530e00, -3.8660e-02, 2.7790e-04, -1.5430e-06),
            (5.4480e-03, 1.0080e-04, -2.8090e-06, 9.8110e-09),
            (-5.5520e-04, 8.3840e-06, -3.9970e-08, -3.4660e-10),
            (3.0380e-06, -7.4350e-08, 7.4420e-10),
            (6.6690e-08, -9.1050e-10),
            (-8.4720e-10,),
        )

    def coefficient_specific_heat(self) -> Tuple:
        return (
            (3.8870e03, 7.2010e00, -8.9790e-02, -4.3900e-04),
            (-1.8500e01, 2.9840e-01, -1.8650e-03, -1.7180e-05),
            (-3.7690e-02, -1.1960e-02, 9.8010e-05, 6.6600e-07),
            (-3.7760e-03, -5.6110e-05, -7.8110e-07),
            (-1.5040e-04, 7.3730e-06),
            (6.4330e-06,),
        )

    def coefficient_conductivity(self) -> Tuple:
        return (
            (4.1750e-01, 7.2710e-04, 2.8230e-07, 9.7180e-09),
            (-4.4210e-03, -2.9520e-05, 7.3360e-08, 4.3280e-10),
            (2.0440e-05, 3.4130e-07, -3.6650e-09, -2.7910e-11),
            (2.9430e-07, -9.6460e-10, 3.1740e-11),
            (-8.6660e-10, -4.5730e-13),
            (-2.0330e-10,),
        )

    def coefficient_density(self) -> Tuple:
        return (
            (9.5810e02, -4.1510e-01, -2.2610e-03, 2.9980e-07),
            (-1.3910e00, -1.5100e-02, 1.1130e-04, -3.2640e-07),
            (-1.1050e-02, 1.8280e-04, -1.6410e-06, 1.5100e-08),
            (-1.2080e-04, 2.9920e-06, 1.4550e-09),
            (4.9270e-06, -1.3250e-07),
            (-7.7270e-08,),
        )

    def __init__(self, conc: float) -> None:
        """
        Constructor for an methyl alcohol mixture instance

        @param conc: concentration, in percent, from 0.0 to 60.0
        """

        super().__init__(0.0, 40.0, conc, 0.0, 60.0)
        self.t_min = self.t_freeze = self.calc_freeze_point(conc)

        self.c_base = 30.5128
        self.t_base = 3.5359

    def calc_freeze_point(self, conc: float) -> float:
        """
        Calculate the freezing point temperature of the mixture

        Based on a curve fit of the Methyl Alcohol freezing points
        Engineering Toolbox - https://www.engineeringtoolbox.com/methanol-water-d_987.html
        """

        # should return 0 C for low concentrations
        if conc < 0.05:
            return 0

        # polynomial fit
        # t_f = a + b * conc + c * conc**2 + d * conc**3
        conc = self._check_concentration(conc)
        coefficient_freeze = [6.9312e-01, -5.6953e-01, -1.2817e-02, 4.3210e-05]
        c_pow = [conc**p for p in range(4)]
        return sum(x * y for x, y in zip(coefficient_freeze, c_pow))

    def fluid_name(self) -> str:
        """
        Returns a descriptive title for this fluid
        @return: "MethylAlcohol"
        """
        return "MethylAlcohol"
