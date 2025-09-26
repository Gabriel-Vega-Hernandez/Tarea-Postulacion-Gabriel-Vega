import numpy as np


def check_availability(panel_position: list, panel_size: list, roof: np.array) -> bool:

    for i in range(panel_size[0]):
        for j in range(panel_size[1]):
            # Me aseguro de que este espacion no este siendo ocupado por otro panel
            if roof[panel_position[0] + i, panel_position[1] + j] != 0:
                return False

    return True


def add_panel(panel_position: list, panel_size: list, roof: np.array, n_panel: int) -> tuple:

    count = 0

    # Primero me fijo en si un panel que parte en la posicion dada, es capaz de entrar en la grilla
    if panel_position[0] + panel_size[0] > (len(roof)) or panel_position[1] + panel_size[1] > (len(roof[0])):
        return count, roof
    elif not check_availability(panel_position, panel_size, roof):
        return count, roof
    else:
        for i in range(panel_size[0]):
            for j in range(panel_size[1]):
                # Relleno los espacion correspondientes con un nuevo panel
                roof[panel_position[0] + i, panel_position[1] + j] = n_panel + 1
                count += 1         

    return count, roof


def panel_positioning(panel_orientation: list, roof: np.array, n_panel: int, rectangularity: bool) -> tuple:

    if rectangularity:
        # Recorremos la grilla en intervalos del tamaño del panel
        for i in list(range(0, len(roof), panel_orientation[0])):
                for j in list(range(0, len(roof[0]), panel_orientation[1])):
                    add_count, roof = add_panel([i, j], [panel_orientation[0], panel_orientation[1]], roof, n_panel)
                    # add_count cuenta cada posicion ocupada por el panel en la grilla, asi que dividimos por el area
                    n_panel = n_panel + (add_count  / (panel_orientation[0] * panel_orientation[1]))

        return n_panel, roof
    else:
        # Recorremos toda la grilla
        for i in list(range(0, len(roof))):
                for j in list(range(0, len(roof[0]))):
                    add_count, roof = add_panel([i, j], [panel_orientation[0], panel_orientation[1]], roof, n_panel)
                    n_panel = n_panel + (add_count  / (panel_orientation[0] * panel_orientation[1]))

        return n_panel, roof