from typing import Union
from abc import abstractmethod, ABC
from warnings import WarningMessage


class BaseFluid(ABC):
    def __init__(self, conc: Union[int, float] = 0.0) -> None:
        self.c = conc
        self.c_min = 0.0
        self.c_max = 100.0
        self.temp_min = 0.0
        self.temp_max = 100.0

    def _set_concentration_limits(self, c_min, c_max) -> None:
        self.c_min = c_min
        self.c_max = c_max

    def _check_concentration(
        self, conc: Union[int, float], fl_name: str
    ) -> Union[int, float]:
        if conc < self.c_min:
            msg = f'Fluid "{fl_name}", concentration must be greater than {self.c_min:0.2f}\n'
            msg += f"Resetting concentration to {self.c_min:0.2f}"
            UserWarning(msg)
            return self.c_min
        elif conc > self.c_max:
            msg = (
                f'Fluid "{fl_name}", concentration must be less than {self.c_max:0.2f}'
            )
            msg += f"Resetting concentration to {self.c_max:0.2f}"
            UserWarning(msg)
            return self.c_max
        else:
            return conc

    def _set_temperature_limits(self, temp_min, temp_max) -> None:
        self.temp_min = temp_min
        self.temp_max = temp_max

    def _check_temperature(
        self, temp: Union[int, float], fl_name: str
    ) -> Union[int, float]:
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
    def _viscosity_water(temp: Union[int, float]):

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

        if temp < 20:
            return (
                10 ** (AM0 + AM1 / (AM2 + (temp - 20) * (AM3 + AM4 * (temp - 20))))
                * 100
            ) * 0.001

        if temp > 100:
            return (A10 + temp * A11 + (temp**2) * A12 + (temp**3) * A13) * 0.001

        return (
            AM5 * 10 ** ((temp - 20) * (AM6 + (temp - 20) * AM7) / (temp + AM8))
        ) * 0.001

    @abstractmethod
    def viscosity(self, temp: Union[int, float] = 0.0):
        pass

    def mu(self, temp: Union[int, float] = 0.0):
        return self.viscosity(temp)

    @abstractmethod
    def specific_heat(self, temp: Union[int, float] = 0.0):
        pass

    def cp(self, temp: Union[int, float] = 0.0):
        return self.specific_heat(temp)

    @abstractmethod
    def density(self, temp: Union[int, float] = 0.0):
        pass

    def rho(self, temp: Union[int, float] = 0.0):
        return self.density(temp)

    @abstractmethod
    def conductivity(self, temp: Union[int, float] = 0.0):
        pass

    def k(self, temp: Union[int, float] = 0.0):
        return self.conductivity(temp)

    def prandtl(self, temp: Union[int, float] = 0.0):
        return self.cp(temp) * self.mu(temp) / self.k(temp)

    def pr(self, temp: Union[int, float] = 0.0):
        return self.prandtl(temp)

    def thermal_diffusivity(self, temp: Union[int, float] = 0.0):
        self.k(temp) / (self.rho(temp) * self.cp(temp))

    def alpha(self, temp: Union[int, float] = 0.0):
        return self.thermal_diffusivity(temp)
