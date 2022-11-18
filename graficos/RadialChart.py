from math import pi
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

def radar_factory(num_vars, frame='circle'):
    # calcula ângulos de eixo uniformemente espaçados
    theta = [(2*pi) * (i / num_vars) for i in range(num_vars)]
    class RadarTransform(PolarAxes.PolarTransform):

        def transform_path_non_affine(self, path):
            # Caminhos com etapas de interpolação não unitárias correspondem a linhas de grade,
            # nesse caso forçamos a interpolação (para derrotar o PolarTransform
            # autoconversão para arcos circulares).
            if path._interpolation_steps > 1: path = path.interpolated(num_vars)
            return Path(self.transform(path.vertices), path.codes)

    class RadarAxes(PolarAxes):
        name = 'radar'
        PolarTransform = RadarTransform

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # gira o gráfico de forma que o primeiro eixo fique no topo
            self.set_theta_zero_location('N')

        def fill(self, *args, closed=True, **kwargs):
            """Substituir preenchimento para que a linha seja fechada por padrão"""
            return super().fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            """Substituir o gráfico para que a linha seja fechada por padrão"""
            lines = super().plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            if x[0] != x[-1]: 
                line.set_data(
                    (lambda x=x:x + [x[0]])([_x for _x in x]), 
                    (lambda y=y:y + [y[0]])([_y for _y in y])
                )

        def set_varlabels(self, labels):
            self.set_thetagrids([0, 72, 144, 216, 288] , labels)

        def _gen_axes_patch(self):
            # O patch Axes deve estar centrado em (0,5, 0,5) e de raio 0,5
            # nas coordenadas dos eixos.
            if frame == 'circle':
                return Circle((0.5, 0.5), 0.5)
            elif frame == 'polygon':
                return RegularPolygon((.5, .5), num_vars, radius=0.5, edgecolor="k")
            else:
                raise ValueError("Unknown value for 'frame': %s" % frame)

        def _gen_axes_spines(self):
            if frame == 'circle':
                return super()._gen_axes_spines()
            elif frame == 'polygon':
                # tipo_espinha deve ser 'esquerda'/'direita'/'topo'/'fundo'/'círculo'.                spine = Spine(axes=self,
                spine = Spine(axes=self, spine_type='circle', path=Path.unit_regular_polygon(num_vars))
                # unit_regular_polygon fornece um polígono de raio 1 centrado em
                # (0, 0), mas queremos um polígono de raio 0,5 centrado em (0,5,
                # 0.5) nas coordenadas dos eixos.
                spine.set_transform(Affine2D().scale(.5).translate(.5, .5) + self.transAxes)
                return {'polar': spine}
            else:
                raise ValueError("Unknown value for 'frame': %s" % frame)

    register_projection(RadarAxes)
    return theta


def example_data():
    # return [1,2,3,4,5]
    from random import random
    return [1 + random() * 4 for _ in range(5)]


def example_chart():
    N = 5
    theta = radar_factory(N, frame='polygon')
    data = example_data()
    print(data)
    spoke_labels = ['LG', 'PO', 'CU', 'DOR', 'SOFRIMENTO']

    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(projection='radar'))
    # fig.subplots_adjust(wspace= .5, hspace=0.20, top=0.85, bottom=0.05)

    colors = ['b']
    # Plot the four cases from the example data on separate axes
    # for ax, (title, case_data) in zip(axs.flat, data):
    ax.set_rgrids([1, 2, 3, 4, 5])
    ax.axes.get_yaxis().set_ticklabels([])
    ax.set_title('porra', weight='bold', size='medium', position=(0.5, 1), horizontalalignment='center', verticalalignment='center')
    # for d, color in zip(data, colors):
    ax.plot(theta, data, color=colors[0])
    ax.fill(theta, data, facecolor=colors[0], alpha=0.25, label='_nolegend_')
    ax.set_varlabels(spoke_labels)
    ax.set_ylim([1,5])
#leganda do grafico
    labels = ['SOFRIMENTO']
    legend = ax.legend(labels, loc=(0.8, .95), labelspacing=0.1, fontsize='small')
#Titulo do grafico
    fig.text(
        0.5, .96, '5-Factor Solution Profiles Across Four Scenarios',
        horizontalalignment='center', color='black', weight='bold', size='large'
    )

    plt.show()
    # return fig

    print ('Hello world')

