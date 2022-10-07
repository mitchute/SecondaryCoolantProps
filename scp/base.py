from abc import ABC, abstractmethod


class BaseFluid(ABC):
    """
    A fluid base class that provides convenience methods that can be accessed in derived classes
    """

    def __init__(self, conc: float = 0.0) -> None:
        """
        A constructor for a base fluid, that takes a concentration as an argument.
        Derived classes can decide how to handle the concentration argument and 
        their own constructor interface as needed to construct and manage that
        specific derived class.
        :param conc: Concentration, in percent, from 0 to 100
        """
        self.c = conc
        self.c_min = 0.0
        self.c_max = 100.0
        self.temp_min = 0.0
        self.temp_max = 100.0

    @abstractmethod
    def fluid_name(self) -> str:
        """
        An abstract method that needs to return the fluid name in derived fluid classes
        :return: string name of the fluid
        """
        pass

    def _set_concentration_limits(self, c_min, c_max) -> None:
        """
        A worker function to override the default concentration min/max values
        :param c_min: The minimum concentration value to allow, ranging from 0.0 to 100.0
        :param c_max: The maximum concentration value to allow, ranging from 0.0 to 100.0
        :return: Nothing
        """
        self.c_min = c_min
        self.c_max = c_max

    def _check_concentration(self, conc: float) -> float:
        """
        An internal worker function that checks the given concentration against limits
        :param conc: The concentration to check, ranging from 0.0 to 100.0
        :return: A validated concentration value, pulled to within limits
        """
        n = self.fluid_name()
        if conc < self.c_min:
            msg = f'Fluid "{n}", concentration must be greater than {self.c_min:0.2f}\n'
            msg += f"Resetting concentration to {self.c_min:0.2f}"
            UserWarning(msg)
            return self.c_min
        elif conc > self.c_max:
            msg = f'Fluid "{n}", concentration must be less than {self.c_max:0.2f}'
            msg += f"Resetting concentration to {self.c_max:0.2f}"
            UserWarning(msg)
            return self.c_max
        else:
            return conc

    def _set_temperature_limits(self, temp_min, temp_max) -> None:
        """
        A worker function to override the default temperature min/max values
        :param temp_min: The minimum temperature value to allow, in degrees Celsius
        :param temp_max: The maximum temperature value to allow, ranging from 0.0 to 100.0
        :return: Nothing
        """
        self.temp_min = temp_min
        self.temp_max = temp_max

    def _check_temperature(self, temp: float) -> float:
        """
        An internal worker function that checks the given temperature against limits
        :param temp: The temperature to check, in degrees Celsius
        :return: A validated temperature value, in degrees Celsius
        """
        fl_name = self.fluid_name()
        if temp < self.c_min:
            msg = f'Fluid "{fl_name}", temperature must be greater than {self.temp_min:0.2f}'
            msg += f"Resetting temperature to {self.temp_min:0.2f}"
            UserWarning(msg)
            return self.c_min
        elif temp > self.c_max:
            msg = (
                f'Fluid "{fl_name}", temperature must be less than {self.temp_max:0.2f}'
            )
            msg += f"Resetting temperature to {self.temp_max:0.2f}"
            UserWarning(msg)
            return self.temp_max
        else:
            return temp

    @staticmethod
    def _viscosity_water(temp: float) -> float:
        """
        Returns the viscosity of water.  This is currently used in other fluid
        property routines, so it lives here in the base class.  Ideally, it would
        live in the water derived class and only be used there.
        :param temp: Fluid temperature in degrees Celsius
        :return: The (SOMETHING) viscosity of water in (UNITS)
        """
        am0 = -3.30233
        am1 = 1301
        am2 = 998.333
        am3 = 8.1855
        am4 = 0.00585
        am5 = 1.002
        am6 = -1.3272
        am7 = -0.001053
        am8 = 105
        am10 = 0.68714
        am11 = -0.0059231
        am12 = 2.1249e-05
        am13 = -2.69575e-08
        if temp < 20:
            exponent = (am0 + am1 / (am2 + (temp - 20) * (am3 + am4 * (temp - 20))))
            return (10 ** exponent) * 0.1
        if temp > 100:
            return (am10 + temp * am11 + (temp ** 2) * am12 + (temp ** 3) * am13) * 0.001
        return (
                       am5 * 10 ** ((temp - 20) * (am6 + (temp - 20) * am7) / (temp + am8))
               ) * 0.001

    @abstractmethod
    def viscosity(self, temp: float) -> float:
        """
        Abstract method; derived classes should override to return the (SOMETHING)
        viscosity of that fluid.
        :param temp: Fluid temperature, in degrees Celsius
        :return: Returns the (SOMETHING) viscosity in (UNITS)
        """
        pass

    def mu(self, temp: float) -> float:
        """
        Convenience function for returning the (SOMETHING) viscosity by the common letter 'mu'
        :param temp: Fluid temperature, in degrees Celsius
        :return: Returns the (SOMETHING) viscosity -- which one is mu? in (UNITS)
        """
        return self.viscosity(temp)

    @abstractmethod
    def specific_heat(self, temp: float) -> float:
        """
        Abstract method; derived classes should override to return the specific heat
        of that fluid.
        :param temp: Fluid temperature, in degrees Celsius
        :return: Returns the specific heat in J/kg-K
        """
        pass

    def cp(self, temp: float) -> float:
        """
        Convenience function for returning the specific heat by the common shorthand 'cp'
        :param temp: Fluid temperature, in degrees Celsius
        :return: Returns the specific heat in J/kg-K
        """
        return self.specific_heat(temp)

    @abstractmethod
    def density(self, temp: float) -> float:
        """
        Abstract method; derived classes should override to return the density
        of that fluid.
        :param temp: Fluid temperature, in degrees Celsius
        :return: Returns the density in kg/m3
        """
        pass

    def rho(self, temp: float) -> float:
        """
        Convenience function for returning the density by the common shorthand 'rho'
        :param temp: Fluid temperature, in degrees Celsius
        :return: Returns the density, in kg/m3
        """
        return self.density(temp)

    @abstractmethod
    def conductivity(self, temp: float) -> float:
        """
        Abstract method; derived classes should override to return the thermal
        conductivity of that fluid.
        :param temp: Fluid temperature, in degrees Celsius
        :return: Returns the thermal conductivity in W/m-K
        """
        pass

    def k(self, temp: float) -> float:
        """
        Convenience function for returning the thermal conductivity by the common shorthand 'k'
        :param temp: Fluid temperature, in degrees Celsius
        :return: Returns the thermal conductivity, in W/m-K
        """
        return self.conductivity(temp)

    def prandtl(self, temp: float) -> float:
        """
        Returns the Prandtl number for this fluid
        :param temp: Fluid temperature, in degrees Celsius
        :return: Returns the dimensionless Prandtl number
        """
        return self.cp(temp) * self.mu(temp) / self.k(temp)

    def pr(self, temp: float = 0.0) -> float:
        """
        Convenience function for returning the Prandtl number by the common shorthand 'pr'
        :param temp: Fluid temperature, in degrees Celsius
        :return: Returns the dimensionless Prandtl number
        """
        return self.prandtl(temp)

    def thermal_diffusivity(self, temp: float) -> float:
        """
        Returns the thermal diffusivity for this fluid
        :param temp: Fluid temperature, in degrees Celsius
        :return: Returns the thermal diffusivity in m2/s
        """
        return self.k(temp) / (self.rho(temp) * self.cp(temp))

    def alpha(self, temp: float) -> float:
        """
        Convenience function for returning the thermal diffusivity by the common shorthand 'alpha'
        :param temp: Fluid temperature, in degrees Celsius
        :return: Returns the thermal diffusivity in m2/s
        """
        return self.thermal_diffusivity(temp)
