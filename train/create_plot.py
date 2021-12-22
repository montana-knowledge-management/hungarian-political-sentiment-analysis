import matplotlib.pyplot as plt
import numpy as np
from importlib_resources import files


def mm2px(x):
    """
    Convert millimeters to pixels
    """
    return int(3.7795275591 * x)


def mm2inch(x):
    """
    Convert millimeters to inches
    """
    return 0.03937007874 * x


def get_width_height(type_='onehalf', aspect=(16, 10), unit='px'):
    """
    This function returns the width and the height of a figure in pixels based on the Elsevier
    reccomendations on figure sizes.
    https://www.elsevier.com/authors/policies-and-guidelines/artwork-and-media-instructions/artwork-sizing
    Parameters:
        type_: The type of the figure, can be "minimal",
               "single", "onehalf", "full", "double"
        aspect: This iterable specifies the aspect ratio of the figure.
    """
    width, height = 0, 0
    types = {'minimal': 30, 'single': 90, 'onehalf': 140, 'full': 190, 'double': 360}
    units = {'px': mm2px,
             'inch': mm2inch
             }

    if type_ not in types.keys():
        raise ValueError(f'Invalid keyword argument. Got {type_=}. '
                         'Accepted values are: "minimal", "single",'
                         '"onehalf", "full", "double".')

    scaley = aspect[0] / aspect[1]
    width = types[type_]
    height = width / scaley

    if unit == 'mm':
        return width, height
    else:
        return units[unit](width), units[unit](height)


def setup_matplotlib():
    plt.style.use(["default", "seaborn-bright"])
    w, h = get_width_height(type_='double', aspect=(16, 9), unit='inch')
    plt.rcParams["figure.figsize"] = w, h
    plt.rcParams["lines.linewidth"] = 1

    SMALL_SIZE = 8
    MEDIUM_SIZE = 12
    BIGGER_SIZE = 14

    plt.rc("font", size=MEDIUM_SIZE)  # controls default text sizes
    plt.rc("axes", titlesize=MEDIUM_SIZE)  # fontsize of the axes title
    plt.rc("axes", labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
    plt.rc("xtick", labelsize=MEDIUM_SIZE)  # fontsize of the tick labels
    plt.rc("ytick", labelsize=MEDIUM_SIZE)  # fontsize of the tick labels
    plt.rc("legend", fontsize=MEDIUM_SIZE)  # legend fontsize
    plt.rc("figure", titlesize=BIGGER_SIZE)  # fontsize of the figure title


"""
##########
matplotlib beállításához csak a setup_matplotlib függvényt kell 1 x meghívni

### cikkből a színek
kék: lightblue
piros: firebrick
"""
edgecolor = 'k'
alpha = 1.0
setup_matplotlib()
dir_media = files("resources")


def print_diamond_standard_points():
    bar_width = 0.33
    points_hand_diamond = [172, 160, 151]
    points_with_machine_diamond = [213, 241, 183]
    humans_hand = ["Szerkesztő1", "Szerkesztő2", "Szerkesztő3"]
    humans_machine = ["Szerkesztő4", "Szerkesztő5", "Szerkesztő6"]
    machine = ["Gép"]
    points_machine_diamond = [170]
    plt.bar(humans_hand, points_hand_diamond, color="lightblue", width=bar_width)
    plt.bar(humans_machine, points_with_machine_diamond, color="firebrick", width=bar_width)
    plt.bar(machine, points_machine_diamond, color="lightgreen", width=bar_width)


def print_golden_standard_points():
    bar_width = 0.33
    points_hand = [177, 159, 166]
    points_with_machine = [197, 230, 187]
    humans_hand = ["Szerkesztő1", "Szerkesztő2", "Szerkesztő3"]
    humans_machine = ["Szerkesztő4", "Szerkesztő5", "Szerkesztő6"]
    machine = ["Gép"]
    points_machine = [165]
    plt.bar(humans_hand, points_hand, color="lightblue", width=bar_width)
    plt.bar(humans_machine, points_with_machine, color="firebrick", width=bar_width)
    plt.bar(machine, points_machine, color="lightgreen", width=bar_width)


def plot_both_standards_points():
    bar_width = 0.33
    points_hand = [177, 159, 166]
    points_hand_diamond = [172, 160, 151]
    points_with_machine = [197, 230, 187]  #
    points_with_machine_diamond = [213, 241, 183]
    humans_hand = ["Szerkesztő1", "Szerkesztő2", "Szerkesztő3"]
    humans_machine = ["Szerkesztő4", "Szerkesztő5", "Szerkesztő6"]
    machine = ["Gép"]
    bar_width = 0.33
    r_1 = [x for x in range(len(humans_hand + humans_machine + machine))]
    r_2 = [x + bar_width for x in r_1]
    points_machine = [165]
    points_machine_diamond = [170]

    plt.bar(r_1[:3], points_hand, color="lightblue", width=bar_width, label="Kézzel golden")
    plt.bar(r_1[3:6], points_with_machine, color="firebrick", width=bar_width, label="Címkézett golden")
    plt.bar(r_1[-1], points_machine, color="lightgreen", width=bar_width, label="Gép golden")
    plt.bar(r_2[:3], points_hand_diamond, color="blue", width=bar_width, label="Kézzel diamond")
    plt.bar(r_2[3:6], points_with_machine_diamond, color="red", width=bar_width, label="Címkézett diamond")
    plt.bar(r_2[-1], points_machine_diamond, color="green", width=bar_width, label="Gép diamond")


def plot_at_least_x_good_labels(x: int):
    labels = ["Szerkesztő címkézett",
              "Szerkesztő kézzel",
              "Jogász címkézett",
              "Jogász kézzel",
              "Laikus címkézett",
              "Laikus kézzel",
              "Gép"]
    if x == 2:
        # Legalabb 2 adatok
        szerkeszto_gepi = [55.55555556, 83.33333333, 30]  #
        szerkeszto_kezi = [38.0952381, 35.13513514, 38.46153846]  #
        jogasz_gepi = [43.33333333, 66.66666667, 45.71428571]
        jogasz_kezi = [50, 70.58823529, 26.66666667]
        laikus_gepi = [53.33333333, 28.57142857, 35.71428571]
        laikus_kezi = [9.090909091, 17.14285714, 42.85714286]
        gep = [34.06593407]
    elif x == 3:
        # legalabb 3 adatok
        szerkeszto_gepi = [60, 80, 60]  #
        szerkeszto_kezi = [40, 30, 10.25641026]  #
        jogasz_gepi = [33.33333333, 100, 25]
        jogasz_kezi = [36.36363636, 50, 33.33333333]
        laikus_gepi = [66.66666667, 50, 66.66666667]
        laikus_kezi = [0, 25, 33.33333333]
        gep = [12.82051282]

    all_data = []
    all_data.append(szerkeszto_gepi)
    all_data.append(szerkeszto_kezi)
    all_data.append(jogasz_gepi)
    all_data.append(jogasz_kezi)
    all_data.append(laikus_gepi)
    all_data.append(laikus_kezi)
    all_data.append(gep)
    means = [np.mean(data) for data in all_data]
    colors = [plt.get_cmap("viridis")(elem) for elem in np.linspace(0.0, 1.0, num=len(all_data))]
    for idx, data in enumerate(all_data):
        if idx != len(all_data) - 1:
            if idx == 0:
                plt.scatter([idx], means[idx], color="firebrick", marker="x", label="Átlag")
            else:
                plt.scatter([idx], means[idx], color="firebrick", marker="x")
        plt.scatter([idx] * len(data), data, label=labels[idx], color=colors[idx])
    plt.title("Legalább két címke találati aránya golden standard", size=20)
    ###########################################################################################
    ## kódba a plot után
    plt.grid(b=True, which="major", color="#666666", linestyle="-", linewidth=0.8)
    plt.grid(b=True, which="minor", color="#999999", linestyle=":", linewidth=0.5, alpha=0.5)
    plt.minorticks_on()
    plt.xlabel("")
    plt.ylabel("Találati arány [%]", size=12)
    plt.legend()
    plt.xticks([r for r in range(0, len(labels))], labels)
    # [r + bar_width / 2 for r in range(7)], humans_hand + humans_machine + machine)
    # plt.savefig(dir_media / ".pdf", bbox_inches="tight")
    plt.show()


def performancia_44_doc(mode="ds", lang="en"):
    """

    :param mode: ds: diamond súlyozott
                 dsn: diamond súlyozás nélkül
                 gs: golden súlyozott
                 gsn: golden súlyozott nélkül
    :return:
    """
    if lang == "hu":
        labels = ["Szerkesztő címkézett",
                  "Szerkesztő kézzel",
                  "Gép"]
    elif lang == "en":
        labels = ["Editors on labeled documents",
                  "Editors",
                  "Gép"]

    if mode == "ds":
        # diamond_súlyozott
        szerkeszto_gepi = [65.72534116, 70.11436471, 66.43847213]  #
        szerkeszto_kezi = [70.0734502, 55.1369863, 61.63711043]  #
        gep = [59.23, 58.22, 58.72]
    elif mode == "dsn":
        # diamond súlyozás nélkül
        szerkeszto_gepi = [72.32666667, 67, 68.54666667]  #
        szerkeszto_kezi = [78.05333333, 51.66666667, 62.15333333]  #
        gep = [60.29, 41, 48.81]
    elif mode == "gs":
        # golden súlyozott
        szerkeszto_gepi = [61.25536752, 74.42424242, 66.05196137]  #
        szerkeszto_kezi = [72.91715297, 60.84848485, 66.25741083]  #
        gep = [57.49, 60, 58.72]
    elif mode == "gsn":
        # golden súlyozás nélkül
        szerkeszto_gepi = [59.61666667, 74.88333333, 65.35]  #
        szerkeszto_kezi = [71.57333333, 64.83666667, 68.01666667]  #
        gep = [52.94, 49.32, 51.06]

    colors = [plt.get_cmap("viridis")(elem) for elem in np.linspace(0.0, 1.0, num=len(gep))]
    bar_width = 0.25
    r_1 = [x for x in range(len(labels))]
    r_2 = [x + bar_width for x in r_1]
    r_3 = [x + bar_width for x in r_2]

    plt.bar(r_1, szerkeszto_gepi, color=colors[0], width=bar_width, label="Címkézett")
    plt.bar(r_2, szerkeszto_kezi, color=colors[1], width=bar_width, label="Kézzel")
    plt.bar(r_3, gep, color=colors[2], width=bar_width, label="Gép")
    if mode == "ds":
        # diamond_súlyozott
        plt.title("Első 44 dokumentumon súlyozott performancia, diamond standard", size=20)
    elif mode == "dsn":
        # diamond súlyozás nélkül
        plt.title("Első 44 dokumentumon súlyozás nélküli performancia, diamond standard", size=20)
    elif mode == "gs":
        # golden súlyozott
        plt.title("Első 44 dokumentumon súlyozott performancia, golden standard", size=20)
    elif mode == "gsn":
        # golden súlyozás nélkül
        plt.title("Első 44 dokumentumon súlyozás nélküli performancia, golden standard", size=20)

    ###########################################################################################
    ## kódba a plot után
    plt.grid(b=True, which="major", color="#666666", linestyle="-", linewidth=0.8)
    plt.grid(b=True, which="minor", color="#999999", linestyle=":", linewidth=0.5, alpha=0.5)
    plt.minorticks_on()
    plt.xlabel("")
    plt.ylabel("Találati arány [%]", size=12)
    plt.legend()
    plt.xticks([r + bar_width for r in range(len(labels))], ["Precision", "Recall", "F1"], size=10)
    if mode == "ds":
        # diamond_súlyozott
        plt.savefig(dir_media / "sulyozott_diamond_standard_44_dok_p_r_f1.png", bbox_inches="tight")
    elif mode == "dsn":
        # diamond súlyozás nélkül
        plt.savefig(dir_media / "sulyozatlan_diamond_standard_44_dok_p_r_f1.png", bbox_inches="tight")
    elif mode == "gs":
        # golden súlyozott
        plt.savefig(dir_media / "sulyozott_golden_standard_44_dok_p_r_f1.png", bbox_inches="tight")
    elif mode == "gsn":
        # golden súlyozás nélkül
        plt.savefig(dir_media / "sulyozatlan_golden_standard_44_dok_p_r_f1.png", bbox_inches="tight")

    plt.show()


def rare_labels_performance():
    labels = ["Szerkesztő címkézett",
              "Szerkesztő kézzel",
              "Gép"]

    # ritka címke
    szerkeszto_gepi = [61.76, 74.22, 65.64]
    szerkeszto_kezi = [68.66, 51.51, 58.48]
    jogasz_gepi = [53.28, 74.13, 61.59]
    jogasz_kezi = [56.85, 56.73, 56.37]
    laikus_gepi = [50.98, 75.32, 60.49]
    laikus_kezi = [58.08, 48.15, 49.98]
    gep = [55.36, 63.27, 59.05]

    colors = [plt.get_cmap("viridis")(elem) for elem in np.linspace(0.0, 1.0, num=7)]
    bar_width = 1 / 8
    r_1 = [x for x in range(len(labels))]
    r_2 = [x + bar_width for x in r_1]
    r_3 = [x + bar_width for x in r_2]
    r_4 = [x + bar_width for x in r_3]
    r_5 = [x + bar_width for x in r_4]
    r_6 = [x + bar_width for x in r_5]
    r_7 = [x + bar_width for x in r_6]

    plt.bar(r_1, szerkeszto_gepi, color=colors[0], width=bar_width, label="Szerkesztő címkézett")
    plt.bar(r_2, szerkeszto_kezi, color=colors[1], width=bar_width, label="Szerkesztő kézzel")
    plt.bar(r_3, jogasz_gepi, color=colors[2], width=bar_width, label="Jogász címkézett")
    plt.bar(r_4, jogasz_kezi, color=colors[3], width=bar_width, label="Jogász kézzel")
    plt.bar(r_5, laikus_gepi, color=colors[4], width=bar_width, label="Laikus címkézett")
    plt.bar(r_6, laikus_kezi, color=colors[5], width=bar_width, label="Laikus kézzel")
    plt.bar(r_7, gep, color=colors[6], width=bar_width, label="Gép")

    plt.title("Ritka címkéken performancia, golden standard", size=20)
    ###########################################################################################
    ## kódba a plot után
    plt.grid(b=True, which="major", color="#666666", linestyle="-", linewidth=0.8)
    plt.grid(b=True, which="minor", color="#999999", linestyle=":", linewidth=0.5, alpha=0.5)
    plt.minorticks_on()
    plt.xlabel("")
    plt.ylabel("Találati arány [%]", size=12)
    plt.legend()
    plt.xticks([r + 3 * bar_width for r in range(len(labels))], ["Precision", "Recall", "F1"], size=10)
    plt.savefig(dir_media / "ritka_cimkek_performancia.png", bbox_inches="tight")
    plt.show()


def cumulative_sum(times: list):
    actual = 0
    result = []
    for elem in times:
        actual += elem
        result.append(actual)
    return result


def calculate_point_vs_time(lang="en"):
    if lang == "en":
        labels = ["Editor 1",
                  "Editor 2",
                  "Editor 3",
                  "Editor with labels 1",
                  "Editor with labels 2",
                  "Editor with labels 3",
                  "Algorithm"]
    elif lang == "hu":
        labels = ["Szerkesztő kézzel 1",
                  "Szerkesztő kézzel 2",
                  "Szerkesztő kézzel 3",
                  "Szerkesztő címkézett 1",
                  "Szerkesztő címkézett 2",
                  "Szerkesztő címkézett 3",
                  "Gép"]
    else:
        raise ValueError("Language not defined, choose between 'hu' or 'en'!")

    szerkeszto_kezi_1_x = cumulative_sum([42.45, 31.40, 41.15, 30.77, 16.55, 17.68])
    szerkeszto_kezi_1_y = [72, 177, 218, 238, 276, 293]
    szerkeszto_kezi_2_x = cumulative_sum([55.47, 37.52, 42.27, 35.23, 9.52])
    szerkeszto_kezi_2_y = [61, 159, 193, 226, 237]
    szerkeszto_kezi_3_x = cumulative_sum([20.60, 14.95, 16.58, 14.83, 9.70, 13.30, 15.48, 12.45, 10.10, 11.25])
    szerkeszto_kezi_3_y = [74, 166, 211, 239, 270, 303, 362, 407, 470, 497]

    szerkeszto_gepi_1_x = cumulative_sum([132.20, 47.80])
    szerkeszto_gepi_1_y = [82, 197]
    szerkeszto_gepi_2_x = cumulative_sum([112.90, 62.65, 4.45])
    szerkeszto_gepi_2_y = [97, 230, 234]
    szerkeszto_gepi_3_x = cumulative_sum([56.28, 40.63, 23.67, 29.50, 19.82, 10.10])
    szerkeszto_gepi_3_y = [81, 187, 219, 252, 290, 300]
    gep_x = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 180]
    gep_y = [73, 165, 182, 204, 234, 307, 347, 391, 473, 488, 488]

    all_data = [(szerkeszto_kezi_1_x, szerkeszto_kezi_1_y), (szerkeszto_kezi_2_x, szerkeszto_kezi_2_y),
                (szerkeszto_kezi_3_x, szerkeszto_kezi_3_y), (szerkeszto_gepi_1_x, szerkeszto_gepi_1_y),
                (szerkeszto_gepi_2_x, szerkeszto_gepi_2_y), (szerkeszto_gepi_3_x, szerkeszto_gepi_3_y), (gep_x, gep_y)]

    colors = [plt.get_cmap("plasma")(elem) for elem in np.linspace(0.0, 1.0, num=len(all_data))]

    for idx, elem in enumerate(all_data):
        x = [0] + elem[0]
        y = [0] + elem[1]
        plt.plot(x, y, linestyle="-", label=labels[idx], color=colors[idx], marker="o", linewidth=2)

    # ###########################################################################################
    ## kódba a plot után
    plt.grid(b=True, which="major", color="#666666", linestyle="-", linewidth=0.8)
    plt.grid(b=True, which="minor", color="#999999", linestyle=":", linewidth=0.5, alpha=0.5)
    plt.minorticks_on()
    if lang == "en":
        plt.xlabel("Time [minutes]", size=12)
        plt.ylabel("Points (1-10 weighted)", size=12)
    else:
        plt.xlabel("Idő [perc]", size=12)
        plt.ylabel("Pontok (1-10 súlyozott)", size=12)

    plt.legend()
    # plt.xticks([r + 3 * bar_width for r in range(len(labels))], ["Precision", "Recall", "F1"], size=10)
    plt.savefig(dir_media / "time_vs_points_{}.png".format(lang), bbox_inches="tight")
    plt.show()


# performancia_44_doc(mode="dsn")

# x = [2000, 1000, 500, 200, 100, 50, 0]
# pos_18_acc = np.array([0.85, 0.83, 0.81, 0.8, 0.71, 0.7, 0.68])*100
# pos_50_acc = np.array([0.79, 0.74, 0.74, 0.75, 0.83, 0.83, 0.84])*100
# pos_88_acc = np.array([0.82, 0.85, 0.78, 0.56, 0.8, 0.83, 0.47])*100
# pos_18_f1 = np.array([0.84, 0.81, 0.79, 0.78, 0.65, 0.64, 0.63])*100
# pos_50_f1 = np.array([0.79, 0.74, 0.74, 0.75, 0.81, 0.81, 0.82])*100
# pos_88_f1 = np.array([0.82, 0.85, 0.78, 0.54, 0.79, 0.82, 0.40])*100
# pos_18_pu = [67.59128978, 73.50091075, 80.54291417, 82.01626016, 103.1755023, 103.8542885, 100.5468271]
# pos_50_pu = [43.74101014, 52.94270601, 51.17670165, 45.55582692, 54.02276848, 54.79768525, 52.98650526]
# pos_88_pu = [31.61015818, 32.19580157, 38.28343824, 45.78346139, 46.11246856, 48.93538644, 38.53866116]
# colors = [plt.get_cmap("viridis")(elem) for elem in np.linspace(0.0, 1.0, num=3)]
# fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
#
# ax1.plot(x, pos_18_acc, color=colors[0], linestyle="-", marker="o", linewidth=1.5, label="18 pozitív minta")
# ax1.plot(x, pos_50_acc, color=colors[1], linestyle="-", marker="o", linewidth=1.5, label="50 pozitív minta")
# ax1.plot(x, pos_88_acc, color=colors[2], linestyle="-", marker="o", linewidth=1.5, label="88 pozitív minta")
# ax1.grid(b=True, which="major", color="#666666", linestyle="-", linewidth=0.8)
# ax1.grid(b=True, which="minor", color="#999999", linestyle=":", linewidth=0.5, alpha=0.5)
# ax1.minorticks_on()
# # ax1.set_xlabel("Tokens used to reduce correlation [-]", size=16)
# ax1.set_ylabel("Pontosság [%]", size=16)
# ax1.legend(fontsize=12)
#
# ax2.plot(x, pos_18_f1, color=colors[0], linestyle="-", marker="o", linewidth=1.5, label="18 pozitív minta")
# ax2.plot(x, pos_50_f1, color=colors[1], linestyle="-", marker="o", linewidth=1.5, label="50 pozitív minta")
# ax2.plot(x, pos_88_f1, color=colors[2], linestyle="-", marker="o", linewidth=1.5, label="88 pozitív minta")
# ax2.grid(b=True, which="major", color="#666666", linestyle="-", linewidth=0.8)
# ax2.grid(b=True, which="minor", color="#999999", linestyle=":", linewidth=0.5, alpha=0.5)
# ax2.minorticks_on()
# # ax2.set_xlabel("Tokens used to reduce correlation [-]", size=16)
# ax2.set_xlabel("Szűréshez használt feature-ök száma [db]", size=16)
# ax2.set_ylabel("F1 mérték [%]", size=16)
# ax2.legend(fontsize=12)
#
# ax3.plot(x, pos_18_pu, color=colors[0], linestyle="-", marker="o", linewidth=1.5, label="18 pozitív minta")
# ax3.plot(x, pos_50_pu, color=colors[1], linestyle="-", marker="o", linewidth=1.5, label="50 pozitív minta")
# ax3.plot(x, pos_88_pu, color=colors[2], linestyle="-", marker="o", linewidth=1.5, label="88 pozitív minta")
# ax3.grid(b=True, which="major", color="#666666", linestyle="-", linewidth=0.8)
# ax3.grid(b=True, which="minor", color="#999999", linestyle=":", linewidth=0.5, alpha=0.5)
# ax3.minorticks_on()
# # ax3.set_xlabel("Tokens used to reduce correlation [-]", size=16)
# ax3.set_ylabel("PU metrika [-]", size=16)
# ax3.legend(fontsize=12)
# fig.x_label("Tokens used to reduce correlation [-]", size=16)


###################################################################
# x = ["20000", "1000", "500"]
# bar_width = 1 / 4
# r_1 = [x for x in range(len(x))]
# r_2 = [x + bar_width for x in r_1]
# r_3 = [x + bar_width for x in r_2]
#
# pos_18_f1 = np.array([0.63, 0.77, 0.77]) * 100
# pos_50_f1 = np.array([0.82, 0.32, 0.33]) * 100
# pos_88_f1 = np.array([0.4, 0.33, 0.4]) * 100
#
# pos_18_acc = np.array([0.68, 0.8, 0.8]) * 100
# pos_50_acc = np.array([0.84, 0.42, 0.43]) * 100
# pos_88_acc = np.array([0.47, 0.43, 0.47]) * 100
#
# pos_18_pu = [100.55, 32.51, 26.32]
# pos_50_pu = [52.99, 36.06, 25.07]
# pos_88_pu = [38.54, 35.8, 29.46]
#
# colors = [plt.get_cmap("viridis")(elem) for elem in np.linspace(0.0, 1.0, num=3)]
# fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
#
# ax1.bar(r_1, pos_18_acc, color=colors[0], width=bar_width, label="18 pozitív minta")  # linestyle="-", marker="o", linewidth=1.5,
# ax1.bar(r_2, pos_50_acc, color=colors[1], width=bar_width, label="50 pozitív minta")  # linestyle="-", marker="o", linewidth=1.5,
# ax1.bar(r_3, pos_88_acc, color=colors[2], width=bar_width, label="88 pozitív minta")  # linestyle="-", marker="o", linewidth=1.5,
# ax1.grid(b=True, which="major", color="#666666", linestyle="-", linewidth=0.8)
# ax1.grid(b=True, which="minor", color="#999999", linestyle=":", linewidth=0.5, alpha=0.5)
# ax1.minorticks_on()
# ax1.set_xticks([r + bar_width for r in range(len(x))])
# ax1.set_xticklabels(x)
# # ax1.set_xlabel("Tokens used to reduce correlation [-]", size=16)
# ax1.set_ylabel("Pontosság [%]", size=16)
#
# # ax1.legend(fontsize=12)
#
# ax2.bar(r_1, pos_18_f1, color=colors[0], width=bar_width, label="18 pozitív minta")  # linestyle="-", marker="o", linewidth=1.5,
# ax2.bar(r_2, pos_50_f1, color=colors[1], width=bar_width, label="50 pozitív minta")  # linestyle="-", marker="o", linewidth=1.5,
# ax2.bar(r_3, pos_88_f1, color=colors[2], width=bar_width, label="88 pozitív minta")  # linestyle="-", marker="o", linewidth=1.5,
# ax2.grid(b=True, which="major", color="#666666", linestyle="-", linewidth=0.8)
# ax2.grid(b=True, which="minor", color="#999999", linestyle=":", linewidth=0.5, alpha=0.5)
# ax2.minorticks_on()
# ax2.set_xticks([r + bar_width for r in range(len(x))])
# ax2.set_xticklabels(x)
# # ax2.set_xlabel("Tokens used to reduce correlation [-]", size=16)
# ax2.set_xlabel("Legrelevánsabb feature-ök száma [db]", size=16)
# ax2.set_ylabel("F1 mérték [%]", size=16)
# # ax2.legend(fontsize=12)
#
# ax3.bar(r_1, pos_18_pu, color=colors[0], width=bar_width, label="18 pozitív minta")
# ax3.bar(r_2, pos_50_pu, color=colors[1], width=bar_width,  label="50 pozitív minta")
# ax3.bar(r_3, pos_88_pu, color=colors[2], width=bar_width, label="88 pozitív minta")
# ax3.grid(b=True, which="major", color="#666666", linestyle="-", linewidth=0.8)
# ax3.grid(b=True, which="minor", color="#999999", linestyle=":", linewidth=0.5, alpha=0.5)
# ax3.minorticks_on()
# ax3.set_xticks([r + bar_width for r in range(len(x))])
# ax3.set_xticklabels(x)
# # ax3.set_xlabel("Tokens used to reduce correlation [-]", size=16)
# ax3.set_ylabel("PU metrika [-]", size=16)
# ax3.legend(fontsize=12)
###################################################################


# labels = ["F1",
#           "Pontosság",
#           "Fedés"]
#
# # ritka címke
# lstm = [60.25, 47.5, 96.88]
# bert_1000 = [63.75, 66.0, 61.5]
# bert = [92.38, 93.13, 92.0]
#
# colors = [plt.get_cmap("viridis")(elem) for elem in np.linspace(0.0, 1.0, num=3)]
# bar_width = 1 / 4
# r_1 = [x for x in range(len(labels))]
# r_2 = [x + bar_width for x in r_1]
# r_3 = [x + bar_width for x in r_2]
#
#
# plt.bar(r_1, lstm, color=colors[0], width=bar_width, label="LSTM")
# plt.bar(r_2, bert_1000, color=colors[1], width=bar_width, label="BERT 1000 mondaton")
# plt.bar(r_3, bert, color=colors[2], width=bar_width, label="BERT teljes adaton")
###########################################################################################
labels = ["spaCy", "hunspell", "hungarian-stemmer"]
# example data
x = [10, 25, 50, 100, 250, 500, 720]
y_spacy = [0.12,
           0.18,
           0.91,
           7.15,
           39.11,
           62.10,
           66.70
           ]
y_hunspell = [0.14,
              0.25,
              1.37,
              8.95,
              39.57,
              60.76,
              66.06
              ]
y_hunstem = [0.15,
             0.40,
             1.91,
             10.67,
             42.60,
             62.24,
             67.14,
             ]

y_err_spacy = [0.38,
               0.41,
               1.14,
               2.99,
               3.47,
               2.07,
               1.45
               ]
y_err_hunspell = [0.40,
                  0.47,
                  1.29,
                  3.08,
                  3.59,
                  2.42,
                  2.00
                  ]
y_err_hunstem = [0.44,
                 0.63,
                 1.61,
                 3.43,
                 3.35,
                 2.13,
                 1.59
                 ]

# First illustrate basic pyplot interface, using defaults where possible.
# plt.figure()
colors = [plt.get_cmap("viridis")(elem) for elem in np.linspace(0.0, 1.0, num=3)]
plt.errorbar(x, y_spacy, yerr=y_err_spacy, label=labels[0], marker='o', capsize=5, color=colors[0])
plt.errorbar(x, y_hunspell, yerr=y_err_hunspell, label=labels[1], marker='o', capsize=5, color=colors[1])
plt.errorbar(x, y_hunstem, yerr=y_err_hunstem, label=labels[2], marker='o', capsize=5, color=colors[2])
# plt.title("")

plt.title("Átlagos F1 értékek különböző szótövezés esetén, 100 futtatásból", size=20)
###########################################################################################
## kódba a plot után
plt.grid(b=True, which="major", color="#666666", linestyle="-", linewidth=0.8)
plt.grid(b=True, which="minor", color="#999999", linestyle=":", linewidth=0.5, alpha=0.5)
plt.minorticks_on()
plt.xlabel("Undor halmaz számossága [db]", size=15)
plt.ylabel("F1 [%]", size=15)
# plt.xscale("log")
plt.legend()
# plt.xticks([r + bar_width for r in range(len(labels))], labels, size=15)
# plt.savefig(dir_media / "NER_performancia_hu.png", bbox_inches="tight")
plt.show()

# labels = [
#     "Tf-idf szűrés nélkül",
#     "Tf-idf + legrelevánsabb 2000 feature szűrve",
#     "Tf-idf + legrelevánsabb 50 feature szűrve",
#     "Tf-idf + Phraser dokumentumokon tanítva",
#     "Tf-idf + Phraser mondatokon tanítva",
#     "Doc2Vec feature reduction nélkül",
#     "Doc2Vec + feature reduction",
#     "W2V átl.",
#     "W2V IDF súlyozott + feature reduction",
#     "W2V IDF súlyozott + jogszabály szűrt",
#     "W2V IDF súlyozott nem szűrt",
#     "LSTM első 200 szó"]
#
# # ritka címke
# training_times = [133.52, 222.58, 225.02, 186.78, 190.33, 5801, 625.35, 274.95, 429.27, 457.91, 533.3, 1885.36]
#
# colors = [plt.get_cmap("viridis")(elem) for elem in np.linspace(0.0, 1.0, num=len(training_times))]
# # bar_width = 1 /
# # r_1 = [x for x in range(len(labels))]
# # r_2 = [x + bar_width for x in r_1]
# # r_3 = [x + bar_width for x in r_2]
# i = 0
# for tim, lab in zip(training_times, labels):
#     plt.bar(i, tim, color=colors[i], label=lab)
#     i += 1
# # plt.bar(labels, training_times, color=colors[0])#, width=bar_width, label="LSTM")
# # plt.bar(r_2, bert_1000, color=colors[1], width=bar_width, label="BERT on 1000 sentences")
# # plt.bar(r_3, bert, color=colors[2], width=bar_width, label="BERT on full training data")
#
# plt.title("Tanítási idők a különböző módszerek esetében", size=20)
# ###########################################################################################
# ## kódba a plot után
# plt.grid(b=True, which="major", color="#666666", linestyle="-", linewidth=0.8)
# plt.grid(b=True, which="minor", color="#999999", linestyle=":", linewidth=0.5, alpha=0.5)
# plt.minorticks_on()
# plt.xlabel("")
# plt.ylabel("Tanítási idő [s]", size=15)
# # plt.legend()
# plt.xticks([r for r in range(len(labels))], labels, size=12, rotation=15, ha="right")
# # plt.xticks([r + bar_width for r in range(len(labels))], labels, size=15)
# plt.savefig(dir_media / "tanitasi_idok.pdf", bbox_inches="tight")
# plt.show()


# labels = [
#     "18 pozitív",
#     "50 pozitív",
#     "88 pozitív"]
#
# x = [50, 100, 200, 500, 1000, 2000]
# pos_18 = [36, 71, 137, 319, 629, 1270]
# pos_50 = [8, 13, 22, 60, 126, 214]
# pos_88 = [7, 10, 14, 30, 62, 127]
# data = [pos_18, pos_50, pos_88]
# colors = [plt.get_cmap("viridis")(elem) for elem in np.linspace(0.0, 1.0, num=len(labels))]
# i = 0
# for dat, lab in zip(data, labels):
#     plt.plot(x, dat, color=colors[i], label=lab, linestyle="-", marker="o", linewidth=1.5)
#     i += 1
#
# plt.title("Közös szavak száma Egyenlő bánásmód és Munkaviszony megszüntetése", size=20)
# ###########################################################################################
# ## kódba a plot után
# plt.grid(b=True, which="major", color="#666666", linestyle="-", linewidth=0.8)
# plt.grid(b=True, which="minor", color="#999999", linestyle=":", linewidth=0.5, alpha=0.5)
# plt.minorticks_on()
# plt.xlabel("Szűréshez használt szavak száma [db]")
# plt.ylabel("Közös szavak száma [db]", size=15)
# plt.savefig(dir_media / "szurt_szavak_szama.pdf", bbox_inches="tight")
# plt.legend()
# plt.show()

################################################################################
# labels = [
#     "1-gram, 88 dok., 1k feature",
#     "1,2-gram, 88 dok., 20k feature",
#     "1-gram, 88 dok., 20k feature",
#     "1,2-gram, 18 dok., 20k feature"]
#
# x = [5, 10, 15, 20, 25, 30, 50]
# x_1 = [5, 10, 15]
# # f1
# egy_gram_88_dok_1k_f1 = [0.8, 0.93, 0.9]
# egyket_gram_88_dok_20k_f1 = [0.91, 0.92, 0.93, 0.93, 0.92, 0.91, 0.94]
# egy_gram_88_dok_20k_f1 = [0.32, 0.52, 0.73, 0.78, 0.71, 0.84, 0.9]
# egyket_gram_18_dok_20k_f1 = [0.51, 0.55, 0.75, 0.84, 0.83, 0.84, 0.87]
# # acc
# egy_gram_88_dok_1k_acc = [0.8,
#                           0.93,
#                           0.9]
# egyket_gram_88_dok_20k_acc = [0.91,
#                               0.92,
#                               0.94,
#                               0.94,
#                               0.93,
#                               0.92,
#                               0.94]
# egy_gram_88_dok_20k_acc = [0.41,
#                            0.54,
#                            0.73,
#                            0.79,
#                            0.71,
#                            0.84,
#                            0.9]
# egyket_gram_18_dok_20k_acc = [0.54,
#                               0.57,
#                               0.75,
#                               0.84,
#                               0.83,
#                               0.85,
#                               0.87]
# # PU
# egy_gram_88_dok_1k_pu = [4.751656098,
#                          6.770878895,
#                          5.981174484]
# egyket_gram_88_dok_20k_pu = [4.958906447,
#                              4.117307923,
#                              6.492074245,
#                              6.141489395,
#                              7.395526286,
#                              10.21670654,
#                              9.852374405]
# egy_gram_88_dok_20k_pu = [1.076516875,
#                           1.35093612,
#                           2.089334268,
#                           1.77555559,
#                           2.150169188,
#                           2.380774475,
#                           4.105234542]
# egyket_gram_18_dok_20k_pu = [1.113996961,
#                              1.604744399,
#                              1.313206665,
#                              4.34138952,
#                              2.094261359,
#                              4.879653278,
#                              7.416965352]
#
# colors = [plt.get_cmap("viridis")(elem) for elem in np.linspace(0.0, 1.0, num=4)]
# fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
#
# ax1.plot(x_1, egy_gram_88_dok_1k_acc, color=colors[0], linestyle="-", marker="o", linewidth=1.5, label=labels[0])
# ax1.plot(x, egyket_gram_88_dok_20k_acc, color=colors[1], linestyle="-", marker="o", linewidth=1.5, label=labels[1])
# ax1.plot(x, egy_gram_88_dok_20k_acc, color=colors[2], linestyle="-", marker="o", linewidth=1.5, label=labels[2])
# ax1.plot(x, egyket_gram_18_dok_20k_acc, color=colors[3], linestyle="-", marker="o", linewidth=1.5, label=labels[3])
# ax1.grid(b=True, which="major", color="#666666", linestyle="-", linewidth=0.8)
# ax1.grid(b=True, which="minor", color="#999999", linestyle=":", linewidth=0.5, alpha=0.5)
# ax1.minorticks_on()
# # ax1.set_xlabel("Tokens used to reduce correlation [-]", size=16)
# ax1.set_ylabel("Pontosság [%]", size=16)
# ax1.legend(fontsize=12)
#
# ax2.plot(x_1, egy_gram_88_dok_1k_f1, color=colors[0], linestyle="-", marker="o", linewidth=1.5, label=labels[0])
# ax2.plot(x, egyket_gram_88_dok_20k_f1, color=colors[1], linestyle="-", marker="o", linewidth=1.5, label=labels[1])
# ax2.plot(x, egy_gram_88_dok_20k_f1, color=colors[2], linestyle="-", marker="o", linewidth=1.5, label=labels[2])
# ax2.plot(x, egyket_gram_18_dok_20k_f1, color=colors[3], linestyle="-", marker="o", linewidth=1.5, label=labels[3])
#
# ax2.grid(b=True, which="major", color="#666666", linestyle="-", linewidth=0.8)
# ax2.grid(b=True, which="minor", color="#999999", linestyle=":", linewidth=0.5, alpha=0.5)
# ax2.minorticks_on()
# # ax2.set_xlabel("Tokens used to reduce correlation [-]", size=16)
# ax2.set_xlabel("LDA topikok száma [db]", size=16)
# ax2.set_ylabel("F1 mérték [%]", size=16)
# # ax2.legend(fontsize=12)
#
# ax3.plot(x_1, egy_gram_88_dok_1k_pu, color=colors[0], linestyle="-", marker="o", linewidth=1.5, label=labels[0])
# ax3.plot(x, egyket_gram_88_dok_20k_pu, color=colors[1], linestyle="-", marker="o", linewidth=1.5, label=labels[1])
# ax3.plot(x, egy_gram_88_dok_20k_pu, color=colors[2], linestyle="-", marker="o", linewidth=1.5, label=labels[2])
# ax3.plot(x, egyket_gram_18_dok_20k_pu, color=colors[3], linestyle="-", marker="o", linewidth=1.5, label=labels[3])
# ax3.grid(b=True, which="major", color="#666666", linestyle="-", linewidth=0.8)
# ax3.grid(b=True, which="minor", color="#999999", linestyle=":", linewidth=0.5, alpha=0.5)
# ax3.minorticks_on()
# # ax3.set_xlabel("Tokens used to reduce correlation [-]", size=16)
# ax3.set_ylabel("PU metrika [-]", size=16)
# # ax3.legend(fontsize=12)
#
# # plt.title("Közös szavak száma Egyenlő bánásmód és Munkaviszony megszüntetése", size=20)
# ###########################################################################################
# # ## kódba a plot után
# # plt.grid(b=True, which="major", color="#666666", linestyle="-", linewidth=0.8)
# # plt.grid(b=True, which="minor", color="#999999", linestyle=":", linewidth=0.5, alpha=0.5)
# # plt.minorticks_on()
# # plt.xlabel("Szűréshez használt szavak száma [db]")
# # plt.ylabel("Közös szavak száma [db]", size=15)
# plt.savefig(dir_media / "lda_eredmenyek.pdf", bbox_inches="tight")
# # plt.legend()
# plt.show()

################################################################################


# labels = [
#     "F1 mérték",
#     "Pontosság"]
# colors = [plt.get_cmap("viridis")(elem) for elem in np.linspace(0.0, 1.0, num=len(training_times))]
# # bar_width = 1 /
# # r_1 = [x for x in range(len(labels))]
# # r_2 = [x + bar_width for x in r_1]
# # r_3 = [x + bar_width for x in r_2]
# x = [0, 50, 100, 200, 500, 1000, 2000]
# pos_18 = [72, 69, 69, 80, 79, 84, 92]
# pos_88 = [348, 807, 1056, 2577, 2041, 1992, 3543]
# data = [pos_18, pos_88]
# colors = [plt.get_cmap("viridis")(elem) for elem in np.linspace(0.0, 1.0, num=len(labels))]
# i = 0
# for dat, lab in zip(data, labels):
#     plt.plot(x, dat, color=colors[i], label=lab, linestyle="-", marker="o", linewidth=1.5)
#     i += 1

# plt.title("", size=20)


################################################################################
# labels = [
#     "18 pozitív",
#     "88 pozitív"]
#
# x = [0, 50, 100, 200, 500, 1000, 2000]
# pos_18 = [72, 69, 69, 80, 79, 84, 92]
# pos_88 = [348, 807, 1056, 2577, 2041, 1992, 3543]
# data = [pos_18, pos_88]
# colors = [plt.get_cmap("viridis")(elem) for elem in np.linspace(0.0, 1.0, num=len(labels))]
# i = 0
# for dat, lab in zip(data, labels):
#     plt.plot(x, dat, color=colors[i], label=lab, linestyle="-", marker="o", linewidth=1.5)
#     i += 1
#
# # plt.title("", size=20)
# ###########################################################################################
# ## kódba a plot után
# plt.grid(b=True, which="major", color="#666666", linestyle="-", linewidth=0.8)
# plt.grid(b=True, which="minor", color="#999999", linestyle=":", linewidth=0.5, alpha=0.5)
# plt.minorticks_on()
# plt.yscale("log")
# plt.xlabel("Szűréshez használt szavak száma [db]")
# plt.ylabel("Pozitívként címkézett dokumentumok száma [db]", size=15)
# plt.savefig(dir_media / "pozitiv_dokumentumok_szama.pdf", bbox_inches="tight")
# plt.legend()
# plt.show()


# labels = [
#     "18 pozitív",
#     "50 pozitív",
#     "88 pozitív"]
#
# x = [0, 50, 100, 200, 500, 1000, 2000]
# pos_18_f1 = [0.63, 0.64, 0.65, 0.78, 0.79, 0.81, 0.84]
# pos_50_f1 = [0.82, 0.81, 0.81, 0.75, 0.74, 0.74, 0.79]
# pos_88_f1 = [0.40, 0.82, 0.79, 0.54, 0.78, 0.85, 0.82]
#
# data = [pos_18_f1, pos_50_f1, pos_88_f1]
# colors = [plt.get_cmap("viridis")(elem) for elem in np.linspace(0.0, 1.0, num=len(labels))]
# i = 0
# for dat, lab in zip(data, labels):
#     plt.plot(x, dat, color=colors[i], label=lab, linestyle="-", marker="o", linewidth=1.5)
#     i += 1
#
# # plt.title("", size=20)
# ###########################################################################################
# ## kódba a plot után
# plt.grid(b=True, which="major", color="#666666", linestyle="-", linewidth=0.8)
# plt.grid(b=True, which="minor", color="#999999", linestyle=":", linewidth=0.5, alpha=0.5)
# plt.minorticks_on()
# plt.yscale("log")
# plt.xlabel("Szűréshez használt szavak száma [db]")
# plt.ylabel("Pozitívként címkézett dokumentumok száma [db]", size=15)
# plt.savefig(dir_media / "pozitiv_dokumentumok_szama.pdf", bbox_inches="tight")
# plt.legend()
# plt.show()

# ###########################################################################################
## kódba a plot után
# plt.grid(b=True, which="major", color="#666666", linestyle="-", linewidth=0.8)
# plt.grid(b=True, which="minor", color="#999999", linestyle=":", linewidth=0.5, alpha=0.5)
# plt.minorticks_on()
# plt.xlabel("Number of tokens used to reduce correlation [-]", size=12)
# plt.ylabel("Accuracy [%]", size=12)
# plt.legend()
# plt.xticks([r + 3 * bar_width for r in range(len(labels))], ["Precision", "Recall", "F1"], size=10)
# plt.savefig(dir_media / "time_vs_points.pdf", bbox_inches="tight")
plt.show()

# # ha subplot van használva akkor a plt-t le kell cserélni:
# ax[].grid(b=True, which="major", color="#666666", linestyle="-", linewidth=0.8)
# ax[].grid(b=True, which="minor", color="#999999", linestyle=":", linewidth=0.5, alpha=0.5)
# ax[].minorticks_on()
# ax[].set_xlabel("")
# ax[].set_ylabel("")
# ax[].legend()
# plt.savefig(dir_media / ".pdf", bbox_inches="tight")
# plt.show()
