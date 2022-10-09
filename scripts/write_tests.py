from itertools import product

from CoolProp.CoolProp import PropsSI

props = {
    'V': 'viscosity',
    'C': 'specific_heat',
    'D': 'density',
    'L': 'conductivity'
}


def write(fluid, property, test_cases, err_tol):
    for t in test_cases:
        temp = t[0]
        fl_str = ""
        try:
            conc = t[1]
            fl_str = f"{fluid}[{conc:0.4f}]"
            print(f"# T: {temp} [C], Conc: {conc} [-], ErrTol: {err_tol*100:0.1f}%")
        except IndexError:
            print(f"# T: {temp} [C], ErrTol: {err_tol*100:0.1f}%")
            fl_str = fluid

        print(f"# PropsSI('{property}', 'P', 101325, 'T', 273.15 + {temp}, '{fl_str.upper()}')")
        p = PropsSI(property, 'P', 101325, 'T', 273.15 + temp, fl_str)
        delta = p * err_tol
        print(f'self.assertAlmostEqual(self.p.{props[property]}({temp:0.1f}), {p:0.3e}, delta={delta:0.3e})')
        print()


if __name__ == "__main__":
    temp_range = [1, 5, 10, 25, 50, 75, 90, 95, 99]
    # write('Water', 'V', product(temp_range), 0.01)
    # write('Water', 'C', product(temp_range), 0.01)
    # write('Water', 'D', product(temp_range), 0.01)
    # write('Water', 'L', product(temp_range), 0.01)
    # write('INCOMP::MPG', 'V', product(temp_range, [0.0]), 0.02)
    write('INCOMP::MPG', 'V', product(temp_range, [0.2]), 0.01)
