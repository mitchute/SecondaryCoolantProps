from math import exp, log

from scp.base import BaseFluid
from scp.water import Water


class PropyleneGlycol(BaseFluid):
    """
    A derived fluid class for propylene glycol and water mixtures
    """

    def __init__(self, concentration: float) -> None:
        """
        Constructor for a propylene glycol mixture instance, taking the amount of concentration
        as the only argument

        @param concentration: Glycol concentration, from 0.0 to 100.0
        """
        super().__init__(concentration)
        self.water = Water()
        self._set_concentration_limits(0.0, 0.6)

    def fluid_name(self) -> str:
        """
        Returns a descriptive title for this fluid
        @return: "PropyleneGlycol"
        """
        return "PropyleneGlycol"

    def _viscosity_pg(self, temp: float) -> float:
        """
        Internal worker function that can give the viscosity of pure propylene glycol.
        These doc strings should have citations I think.

        @param temp: Fluid temperature, in degrees Celsius
        @return: Viscosity something
        """

        self._check_temperature(temp)

        return exp(-293.07 + (17494 / (temp + 273.15)) + 40.576 * log((temp + 273.15)))

    def viscosity(self, temp: float) -> float:
        """
        Calculate the dynamic viscosity of this Propylene Glycol mixture.

        Viscosity equations for water at 1 atm., from CRC Handbook (op.cit.), page F-51.

        @param temp: Fluid temperature, in degrees Celsius
        @return: Dynamic viscosity, in N/m2-s, or Pa-s
        """

        self._check_temperature(temp)

        b = 24311949006
        c = 24311949006
        d = 1.4e-09
        e = 0

        c_100 = self.c * 100

        c_g = (0.0009035 * c_100 ** 2 + 0.9527607 * c_100 - 0.0009811) / 100.0
        c_w = abs(1 - c_g)
        mu_w = self.water.mu(temp) * 1000  # Convert to Centipoise
        mu_pg = self._viscosity_pg(temp) * 1000  # convert to Centipoise
        t1 = c_w * log(mu_w)
        t2 = c_g * log(mu_pg)
        t3 = d * (125 - temp) ** e * c_w * c_g
        t4 = log(1 + ((c_g * c_w) / (b * c_w ** 2 + c * c_g ** 2)))
        mu = exp(t1 + t2 + t3 + t4) / 1000

        return mu

    def specific_heat(self, temp: float) -> float:
        """
        Calculates the specific heat of this Propylene Glycol mixture.

        @param temp: Fluid temperature, in degrees Celsius
        @return: Specific heat, in J/kg-K
        """

        self._check_temperature(temp)

        return -1

    def conductivity(self, temp: float) -> float:
        """
        Calculates the thermal conductivity of this Propylene Glycol mixture.

        @param temp: Fluid temperature, in degrees Celsius
        @return: Thermal conductivity, in W/m-K
        """

        self._check_temperature(temp)

        return -1

    def density(self, temp: float) -> float:
        """
        Calculates the density of this Propylene Glycol mixture.

        @param temp: Fluid temperature, in degrees Celsius
        @return: Density, in kg/m3
        """

        self._check_temperature(temp)

        return -1
