from . import propylene_glycol
from . import ethylene_glycol
from . import methyl_alcohol
from . import ethyl_alcohol
from . import water


class Fluid:

    fluids = {
        ('WATER',): water.Water,
        ('MPG', 'PROPYLENEGLYCOL'): propylene_glycol.PropyleneGlycol,
        ('MEG', 'ETHYLENEGLYCOL'): ethylene_glycol.EthyleneGlycol,
        ('MMA', 'METHYLALCOHOL'): methyl_alcohol.MethylAlcohol,
        ('ETHYLENEGLYCOL', 'MEA'): ethyl_alcohol.EthylAlcohol
    }

    @staticmethod
    def __new__(cls, fluid_name, *args, **kwargs):

        for key in Fluid.fluids:
            if fluid_name.upper() in key:
                return Fluid.fluids[key](**kwargs)
        else:
            raise ValueError("Unknown fluid type.")
