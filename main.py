from typing import List, Tuple, Dict
import json
import math, numpy as np # Los necesitare para mi solución


def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:

    # Definimos dos grilla que representan nuestro techo vacio
    roof_1 = np.zeros((roof_height, roof_width))
    roof_2 = np.zeros((roof_height, roof_width))

    # Contadores para cuatos paneles hemos agregado
    n_total_1 = 0
    n_total_2 = 0

    # Sirve para determinar si es posible orientar los paneles de manera horizontal y/o vertical
    Vertical = math.floor(roof_width / panel_width), math.floor(roof_height  /panel_height)
    Horizontal = math.floor(roof_width / panel_height), math.floor(roof_height / panel_width)

    # Agregamos todos los paneles posibles que quepan de manera horizontal
    if 0 not in Horizontal:
        n_total_1, roof_1 = panel_position([panel_width, panel_height], roof_1, n_total_1)

    # Agregamos todos los paneles posibles que quepan de manera vertical en el espacio restante
    if 0 not in Vertical:
        n_total_1, roof_1 = panel_position([panel_height, panel_width], roof_1, n_total_1)

        # Rellenamos el segundo techo en la otra direccion, para ver si una de las dos permite mas paneles
        n_total_2, roof_2 = panel_position([panel_height, panel_width], roof_2, n_total_2)
    
    if 0 not in Horizontal:
        n_total_2, roof_2 = panel_position([panel_width, panel_height], roof_2, n_total_2)

    else:
        pass
    
    # Revisamos cual configuracion es mejor
    if n_total_1 >= n_total_2:
        print(roof_1)
        return n_total_1
    else:
        print(roof_2)
        return n_total_2


def add_panel(panel_position: list, panel_size: list, roof: np.array, n_panel: int):

    count = 0
    
    # Primero me fijo en si un panel que parte en la posicion dada, es capaz de entrar en la grilla
    if panel_position[0] + panel_size[0] > (len(roof)) or panel_position[1] + panel_size[1] > (len(roof[0])):
        pass
    else:
        for i in range(panel_size[0]):
            for j in range(panel_size[1]):
                # Me aseguro de que este espacion no este siendo ocupado por otro panel
                if roof[panel_position[0] + i, panel_position[1] + j] != 0:
                    return count, roof
                # Relleno los espacion correspondientes con un nuevo panel
                else:
                    roof[panel_position[0] + i, panel_position[1] + j] = n_panel + 1
                    count += 1
    
    return count, roof


def panel_position(panel_orientation: list, roof: np.array, n_panel: int):

    # Recorremos la grilla en intervalos del tamaño del panel
    for i in list(range(0, len(roof), panel_orientation[0])):
            for j in list(range(0, len(roof[0]), panel_orientation[1])):
                add_count, roof = add_panel([i, j], [panel_orientation[0], panel_orientation[1]], roof, n_panel)
                # add_count cuenta cada posicion ocupada por el panel en la grilla, asi que dividimos por el area
                n_panel = n_panel + (add_count  / (panel_orientation[0] * panel_orientation[1]))
    
    return n_panel, roof


def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()
