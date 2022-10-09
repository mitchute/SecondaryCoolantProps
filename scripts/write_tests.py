from itertools import product

from CoolProp.CoolProp import PropsSI

props = {
    'V': 'viscosity',
    'C': 'specific_heat',
    'D': 'density',
    'L': 'conductivity'
}


def write(fluid, property, test_cases):
    for t in test_cases:
        fl_str = fluid
        try:
            conc_str = f'[{t[1]}]'
            fl_str += conc_str
        except IndexError:
            pass

        temp = t[0]
        print(f"# PropsSI('{property}', 'P', 101325, 'T', 273.15 + {temp}, '{fl_str.upper()}')")
        p = PropsSI(property, 'P', 101325, 'T', 273.15 + temp, fluid)
        delta = p * 0.01
        print(f'self.assertAlmostEqual(self.p.{props[property]}({temp:0.1f}), {p:0.3e}, delta={delta:0.3e})')
        print()


if __name__ == "__main__":
    temp_range = [1, 5, 10, 25, 50, 75, 90, 95, 99]
    conc_range = [0]
    write('water', 'L', product(temp_range))
