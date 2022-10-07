from typing import Union
from abc import abstractmethod, ABC
from warnings import WarningMessage


class BaseFluid(ABC):
    def __init__(self, concentration: Union[int, float] = 0.0) -> None:
        self.c = concentration
        self.c_min = 0.0
        self.c_max = 100.0
        self.temp_min = 0.0
        self.temp_max = 100.0

    def _set_concentration_limits(self, c_min, c_max) -> None:
        self.c_min = c_min
        self.c_max = c_max

    def _check_concentration(
        self, concentration: Union[int, float], fluid_name: str
    ) -> Union[int, float]:
        if concentration < self.c_min:
            msg = f'Fluid "{fluid_name}", concentration must be greater than {self.c_min:0.2f}\n'
            msg += f"Resetting concentration to {self.c_min:0.2f}"
            UserWarning(msg)
            return self.c_min
        elif concentration > self.c_max:
            msg = f'Fluid "{fluid_name}", concentration must be less than {self.c_max:0.2f}'
            msg += f"Resetting concentration to {self.c_max:0.2f}"
            UserWarning(msg)
            return self.c_max
        else:
            return concentration

    def _set_temperature_limits(self, temp_min, temp_max) -> None:
        self.temp_min = temp_min
        self.temp_max = temp_max

    def _check_temperature(
        self, temperature: Union[int, float], fluid_name: str
    ) -> Union[int, float]:
        if temperature < self.c_min:
            msg = f'Fluid "{fluid_name}", temperature must be greater than {self.temp_min:0.2f}'
            msg += f"Resetting temperature to {self.temp_min:0.2f}"
            UserWarning(msg)
            return self.c_min
        elif temperature > self.c_max:
            msg = f'Fluid "{fluid_name}", temperature must be less than {self.temp_max:0.2f}'
            msg += f"Resetting temperature to {self.temp_max:0.2f}"
            UserWarning(msg)
            return self.temp_max
        else:
            return temperature

    @staticmethod
    def _viscosity_water(temperature: Union[int, float]):

        AM0 = -3.30233
        AM1 = 1301
        AM2 = 998.333
        AM3 = 8.1855
        AM4 = 0.00585
        AM5 = 1.002
        AM6 = -1.3272
        AM7 = -0.001053
        AM8 = 105
        A10 = 0.68714
        A11 = -0.0059231
        A12 = 2.1249e-05
        A13 = -2.69575e-08

        if temperature < 20:
            return (
                10
                ** (
                    AM0
                    + AM1
                    / (AM2 + (temperature - 20) * (AM3 + AM4 * (temperature - 20)))
                )
                * 100
            ) * 0.001

        if temperature > 100:
            return (
                A10
                + temperature * A11
                + (temperature**2) * A12
                + (temperature**3) * A13
            ) * 0.001

        return (
            AM5
            * 10
            ** (
                (temperature - 20)
                * (AM6 + (temperature - 20) * AM7)
                / (temperature + AM8)
            )
        ) * 0.001

    @abstractmethod
    def viscosity(self, temperature: Union[int, float] = 0.0):
        pass

    def mu(self, temperature: Union[int, float] = 0.0):
        return self.viscosity(temperature)

    @abstractmethod
    def specific_heat(self, temperature: Union[int, float] = 0.0):
        pass

    def cp(self, temperature: Union[int, float] = 0.0):
        return self.specific_heat(temperature)

    @abstractmethod
    def density(self, temperature: Union[int, float] = 0.0):
        pass

    def rho(self, temperature: Union[int, float] = 0.0):
        return self.density(temperature)

    @abstractmethod
    def conductivity(self, temperature: Union[int, float] = 0.0):
        pass

    def k(self, temperature: Union[int, float] = 0.0):
        return self.conductivity(temperature)

    def prandtl(self, temperature: Union[int, float] = 0.0):
        return self.cp(temperature) * self.mu(temperature) / self.k(temperature)

    def pr(self, temperature: Union[int, float] = 0.0):
        return self.prandtl(temperature)

    def thermal_diffusivity(self, temperature: Union[int, float] = 0.0):
        self.k(temperature) / (self.rho(temperature) * self.cp(temperature))

    def alpha(self, temperature: Union[int, float] = 0.0):
        return self.thermal_diffusivity(temperature)
