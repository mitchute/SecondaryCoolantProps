from math import exp, log10
from typing import Union

from scp.base_fluid import BaseFluid


class PropyleneGlycol(BaseFluid):
    def __init__(self, concentration: Union[int, float] = 0) -> None:
        super().__init__(concentration)

    @staticmethod
    def _viscosity_pg(temp: Union[int, float]):
        return (
            exp(-293.07 + (17494 / (temp + 273.15)) + 40.576 * log10((temp + 273.15)))
        ) * 1000.0

    def viscosity(self, temp: Union[int, float] = 0):
        """
        Calculate the dynamic vicosity of Propylene Glycol

        temp - temperature in Celsius

        returns dynamic vicosity in N/m^2.s or Pa.s
        """

        a1 = 24311949006
        a2 = 24311949006
        a3 = 1.4e-09
        a4 = 0

        if self.c == 0.0:
            return BaseFluid._viscosity_water(temp)

        c_g = (0.0009035 * self.c ^ 2 + 0.9527607 * self.c - 0.0009811) / 100
        c_w = abs(1 - c_g)
        mu = exp(
            c_w * log10(BaseFluid._viscosity_water(temp))
            + c_g * log10(PropyleneGlycol._viscosity_pg(temp))
            + a3 * (125 - temp)
            ^ a4 * c_w * c_g + log10(1 + ((c_g * c_w) / (a1 * c_w ^ 2 + a2 * c_g ^ 2)))
        )

        # convert mPa.S to Pa.S
        return mu * 0.001

    def specific_heat(self, temp: Union[int, float] = 0):
        pass

    def conductivity(self, temp: Union[int, float] = 0):
        pass

    def density(self, temp: Union[int, float] = 0):
        pass
