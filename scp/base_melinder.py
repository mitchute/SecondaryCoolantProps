from scp.base_fluid import BaseFluid


class BaseMelinder(BaseFluid):

    _ij_pairs = (
            (0, 0), (0, 1), (0, 2), (0, 3),
            (1, 0), (1, 1), (1, 2), (1, 3),
            (2, 0), (2, 1), (2, 2), (2, 3),
            (3, 0), (3, 1), (3, 2),
            (4, 0), (4, 1),
            (5, 0)
        )

    def __init__(self, conc: float, c_min: float, c_max: float, t_min: float, t_max: float):
        super().__init__(conc, c_min, c_max, t_min, t_max)
        self.xm = 30.8462
        self.ym = 31.728

    def _f_prop(self, c_arr, temp):

        temp = self._check_temperature(temp)

        xxm = self.c - self.xm
        yym = temp - self.ym
        x_xm = [xxm ** p for p in range(6)]
        y_ym = [yym ** p for p in range(4)]

        f_ret = 0.0

        for i, j in BaseMelinder._ij_pairs:
            f_ret += c_arr[i][j] * x_xm[i] * y_ym[j]

        return f_ret
