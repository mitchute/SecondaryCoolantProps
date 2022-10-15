import sys
import argparse

from scp.ethyl_alcohol import EthylAlcohol
from scp.ethylene_glycol import EthyleneGlycol
from scp.methyl_alcohol import MethylAlcohol
from scp.propylene_glycol import PropyleneGlycol
from scp.water import Water


_valid_prop_strs = ["V", "C", "D", "L"]
_valid_fluid_strs = ["EA", "EG", "MA", "PG", "W"]


def _check_valid_prop(prop_str: str):
    if prop_str not in _valid_prop_strs:
        msg = f"PropStr not valid: {prop_str}"
        raise ValueError(msg)


def _check_valid_fluid(fluid_str: str):
    if fluid_str not in _valid_fluid_strs:
        msg = f"FluidStr not valid: {fluid_str}"
        raise ValueError(msg)


def SCProps(prop_str, temp, x_conc, fluid_str):

    prop_str = prop_str.upper()
    fluid_str = fluid_str.upper()

    _check_valid_prop(prop_str)
    _check_valid_fluid(fluid_str)

    if fluid_str == "EA":
        inst = EthylAlcohol(x_conc)
    elif fluid_str == "EG":
        inst = EthyleneGlycol(x_conc)
    elif fluid_str == "MA":
        inst = MethylAlcohol(x_conc)
    elif fluid_str == "PG":
        inst = PropyleneGlycol(x_conc)
    elif fluid_str == "W":
        inst = Water()
    else:
        inst = None
        raise NotImplementedError("Should never get here")

    if prop_str == "V":
        return inst.viscosity(temp)

    if prop_str == "C":
        return inst.specific_heat(temp)

    if prop_str == "D":
        return inst.density(temp)

    if prop_str == "L":
        return inst.conductivity(temp)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("PropStr", type=str, help=f"Property strings: {_valid_prop_strs}")
    parser.add_argument("Temp", type=float, help="Fluid temperature, in Celsius: [<100]")
    parser.add_argument("XConc", type=float, help="Concentration fraction: [0-1]")
    parser.add_argument("FluidStr", type=str, help=f"Fluid strings: {_valid_fluid_strs}")
    args = parser.parse_args()
    print(SCProps(args.PropStr, args.Temp, args.XConc, args.FluidStr))


if __name__ == "__main__":
    sys.exit(main())
