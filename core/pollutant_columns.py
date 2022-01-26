from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from utils import DataAnalysis
from constants import pollutants
import seaborn as sns
import numpy as np

dataframe = DataAnalysis().file_reader("raw_data/AirQualityUCI.csv")

co = (DataAnalysis().data_formatter(dataframe, "CO(GT)"))["CO(GT)"].values
pt08_S1 = (DataAnalysis().data_formatter(dataframe, "PT08.S1(CO)"))[
    "PT08.S1(CO)"
].values
nmhc_gt = (DataAnalysis().data_formatter(dataframe, "NMHC(GT)"))["NMHC(GT)"].values
c6h6_gt = (DataAnalysis().data_formatter(dataframe, "C6H6(GT)"))["C6H6(GT)"].values
pt08_s2 = (DataAnalysis().data_formatter(dataframe, "PT08.S2(NMHC)"))[
    "PT08.S2(NMHC)"
].values
nox = (DataAnalysis().data_formatter(dataframe, "NOx(GT)"))["NOx(GT)"].values
pt08_s3 = (DataAnalysis().data_formatter(dataframe, "PT08.S3(NOx)"))[
    "PT08.S3(NOx)"
].values
no2_gt = (DataAnalysis().data_formatter(dataframe, "NO2(GT)"))["NO2(GT)"].values
pt08_s4 = (DataAnalysis().data_formatter(dataframe, "PT08.S4(NO2)"))[
    "PT08.S4(NO2)"
].values
pt08_s5 = (DataAnalysis().data_formatter(dataframe, "PT08.S5(O3)"))[
    "PT08.S5(O3)"
].values


palette = list(reversed(sns.color_palette("Spectral", 9).as_hex()))
labels = pollutants.values()


fig = plt.figure(figsize=(7, 5))
axes = fig.add_subplot(1, 1, 1)
axes.set_xlim(0, 3000)
plt.style.use("seaborn")
axes.set_xlabel("Billion Ton")


def animate(i):
    y1 = co[i]
    y2 = pt08_S1[i]
    y3 = nmhc_gt[i]
    y4 = c6h6_gt[i]
    y5 = pt08_s2[i]
    y6 = nox[i]
    y7 = pt08_s3[i]
    y8 = no2_gt[i]
    y9 = pt08_s4[i]
    y10 = pt08_s5[i]

    plt.barh(
        range(10), sorted([y1, y2, y3, y4, y5, y6, y7, y8, y9, y10]), color=palette
    )
    tickdic = {
        "CO": y1,
        "PT08_S1": y2,
        "NMHC": y3,
        "C6H6": y4,
        "PT08_S2": y5,
        "NOX": y6,
        "PT08_S3": y7,
        "NO2": y8,
        "PT08_S4": y9,
        "PT08_S5": y10,
    }
    sorted_tickdic = sorted(tickdic.items(), key=lambda x: x[1])

    tcks = [i[0] for i in sorted_tickdic]

    plt.title(f"Pollutant Emissions, Day: {i} ", color=("blue"))
    plt.yticks(np.arange(10), tcks)


print("ESPERE UN MOMENTO, GUARDANDO ANIMACIÓN, ESTO PUEDE TARDAR ALGUNOS SEGUNDOS...")
anim = FuncAnimation(
    fig,
    animate,
    frames=200,
)
anim.save("animacion_pollutants.mp4")
