from math import exp, log10

from scp.base import BaseFluid


class PropyleneGlycol(BaseFluid):
    """
    A derived fluid class for propylene glycol and water mixtures
    """

    def __init__(self, concentration: float) -> None:
        """
        Constructor for a propylene glycol mixture instance, taking the amount of concentration
        as the only argument
        :param concentration: Glycol concentration, from 0.0 to 100.0
        """
        super().__init__(concentration)

    def fluid_name(self) -> str:
        """
        Returns a descriptive title for this fluid
        :return: Fluid name
        """
        return "PropyleneGlycol"

    @staticmethod
    def _viscosity_pg(temp: float) -> float:
        """
        Internal worker function that can give the viscosity of pure propylene glycol,
        I'm assuming.  These doc strings should have citations I think.
        :param temp: Fluid temperature, in degrees Celsius
        :return: Viscosity something
        """
        return (
            exp(-293.07 + (17494 / (temp + 273.15)) + 40.576 * log10((temp + 273.15)))
        ) * 1000.0

    def viscosity(self, temp: float) -> float:
        """
        Calculate the dynamic viscosity of this Propylene Glycol mixture
        :param temp: Fluid temperature, in degrees Celsius
        :return: Dynamic viscosity, in N/m2-s, or Pa-s
        """

        a1 = 24311949006
        a2 = 24311949006
        a3 = 1.4e-09
        a4 = 0

        if self.c == 0.0:
            # TODO: Will the formulation below not resolve to water as c goes to zero?
            return BaseFluid._viscosity_water(temp)

        c_g = (0.0009035 * self.c ** 2 + 0.9527607 * self.c - 0.0009811) / 100
        c_w = abs(1 - c_g)
        mu = exp(
            c_w * log10(BaseFluid._viscosity_water(temp))
            + c_g * log10(PropyleneGlycol._viscosity_pg(temp))
            + a3 * (125 - temp)
            ** a4 * c_w * c_g + log10(1 + ((c_g * c_w) / (a1 * c_w ** 2 + a2 * c_g ** 2)))
        )

        # convert mPa.S to Pa.S
        return mu * 0.001

    def specific_heat(self, temp: float) -> float:
        """
        Calculates the specific heat of this Propylene Glycol mixture
        :param temp: Fluid temperature, in degrees Celsius
        :return: Specific heat, in J/kg-K
        """
        return -1

    def conductivity(self, temp: float) -> float:
        """
        Calculates the thermal conductivity of this Propylene Glycol mixture
        :param temp: Fluid temperature, in degrees Celsius
        :return: Thermal conductivity, in W/m-K
        """
        return -1

    def density(self, temp: float) -> float:
        """
        Calculates the density of this Propylene Glycol mixture
        :param temp: Fluid temperature, in degrees Celsius
        :return: Density, in kg/m3
        """
        return -1
