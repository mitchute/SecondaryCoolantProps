from abc import abstractmethod
from typing import Tuple

from scp.base_fluid import BaseFluid

# Ideally the type hints would cause the coefficient returns to return this, but it is
#  bulky and I haven't been able to get a new typing NewType to work properly, so for now
#  they just return a plain Tuple.
# Tuple[
#     Tuple[float, float, float, float],
#     Tuple[float, float, float, float],
#     Tuple[float, float, float, float],
#     Tuple[float, float, float],
#     Tuple[float, float],
#     float
# ]


class BaseMelinder(BaseFluid):
    _ij_pairs = (
        (0, 0), (0, 1), (0, 2), (0, 3),
        (1, 0), (1, 1), (1, 2), (1, 3),
        (2, 0), (2, 1), (2, 2), (2, 3),
        (3, 0), (3, 1), (3, 2),
        (4, 0), (4, 1),
        (5, 0)
    )

    def __init__(self, t_min: float, t_max: float, conc: float, c_min: float, c_max: float):
        super().__init__(t_min, t_max, conc, c_min, c_max)
        self.c_base = None
        self.t_base = None
        self.freeze_point = None

    @abstractmethod
    def calc_freeze_point(self, conc: float) -> float:
        pass

    def _f_prop(self, c_arr: Tuple[Tuple[float]], temp: float) -> float:
        temp = self._check_temperature(temp)

        xxm = self.c - self.c_base
        yym = temp - self.t_base
        x_xm = [xxm ** p for p in range(6)]
        y_ym = [yym ** p for p in range(4)]

        f_ret = 0.0

        for i, j in BaseMelinder._ij_pairs:
            f_ret += c_arr[i][j] * x_xm[i] * y_ym[j]

        return f_ret

    @abstractmethod
    def coefficient_viscosity(self) -> Tuple: pass

    @abstractmethod
    def coefficient_specific_heat(self) -> Tuple: pass

    @abstractmethod
    def coefficient_conductivity(self) -> Tuple: pass

    @abstractmethod
    def coefficient_density(self) -> Tuple: pass

    def viscosity(self, temp: float) -> float:
        """
        Calculate the dynamic viscosity of the mixture

        @param temp: Fluid temperature, in degrees Celsius
        @return: Dynamic viscosity, in N/m2-s, or Pa-s
        """

        return self._f_prop(self.coefficient_viscosity(), temp)

    def specific_heat(self, temp: float) -> float:
        """
        Calculates the specific heat of the mixture

        @param temp: Fluid temperature, in degrees Celsius
        @return: Specific heat, in J/kg-K
        """

        return self._f_prop(self.coefficient_specific_heat(), temp)

    def conductivity(self, temp: float) -> float:
        """
        Calculates the thermal conductivity of the mixture

        @param temp: Fluid temperature, in degrees Celsius
        @return: Thermal conductivity, in W/m-K
        """

        return self._f_prop(self.coefficient_conductivity(), temp)

    def density(self, temp: float) -> float:
        """
        Calculates the density of the mixture

        @param temp: Fluid temperature, in degrees Celsius
        @return: Density, in kg/m3
        """

        return self._f_prop(self.coefficient_density(), temp)
