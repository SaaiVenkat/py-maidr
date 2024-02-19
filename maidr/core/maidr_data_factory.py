from __future__ import annotations

from matplotlib.axes import Axes

from maidr.core.enum.plot_type import PlotType
from maidr.core.maidr_data import MaidrData
from maidr.core.plot.bar_data import BarData


class MaidrDataFactory:
    @staticmethod
    def create(axes: Axes, plot, plot_type: PlotType) -> MaidrData:
        if PlotType.BAR == plot_type:
            return BarData(axes, plot, plot_type)
        else:
            raise ValueError("Unsupported plot type: {0}".format(plot_type))