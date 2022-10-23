import click
from scp import fluid

# Add this to .bashrc for nice completion:  eval "$(_SCPROP_COMPLETE=bash_source scprop)"

_fluid_options = list(fluid.Fluid.fluids.keys())
fluid_options = click.Choice([_fluid_options[i][0]
                              for i in range(len(_fluid_options))])
properties = (
    "viscosity",
    "specific_heat",
    "density",
    "conductivity",
    "prandtl",
    "thermal_diffusivity",
)
prop_options = click.Choice(properties)
x_range = click.FloatRange(min=0.0, max=1.0)


@click.command(name="SecondaryCoolantPropsCommandLine")
@click.option(
    "-f",
    "--fluid",
    type=fluid_options,
    required=True,
    default="water",
    help="Which fluid to use?",
)
@click.option(
    "-x",
    "--concentration",
    type=x_range,
    required=False,
    default=0.0,
    help="Mixture concentration fraction. Default 0.0.",
)
@click.option(
    "-p",
    "--property",
    "fluid_prop",
    type=prop_options,
    required=True,
    help="Which fluid property to evaluate.",
)
@click.option(
    "-t",
    "--temperature",
    type=float,
    required=True,
    help="Fluid temperature, in degrees Celsius.",
)
@click.option(
    "-q",
    "--quick",
    is_flag=True,
    show_default=True,
    default=False,
    help="Just report the value, good for scripts",
)
def cli(fluid_name: str, concentration: float, fluid_prop: str, temperature: float, quick: bool):
    f = fluid.Fluid(fluid_name, concentration)

    value = getattr(f, fluid_prop)(temperature)
    units = getattr(f, f"{fluid_prop}_units")()
    if quick:
        print(value)
    else:
        print(f"Fluid:    {fluid}\nProperty: {fluid_prop}\nValue:    {value}\nUnits:    [{units}]")
