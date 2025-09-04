from typing import List, Tuple, Dict
import json
import math, numpy as np # Los necesitare para mi solución


def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:

    # Definimos una grilla que representa nuestro techo vacio
    roof = np.zeros((roof_width, roof_height))

    # Contadores para cuatos paneles hemos agregado
    n_total = 0

    # Sirve para determinar si es posible orientar los paneles de manera horizontal y/o vertical
    Horizontal = math.floor(roof_width / panel_width), math.floor(roof_height  /panel_height)
    Vertical = math.floor(roof_width / panel_height), math.floor(roof_height / panel_width)

    # Sirve para ver si es mejor empezar colocando paneles de forma horizontal o vertical
    if (Horizontal[0] * Horizontal[1]) > (Vertical[0] * Vertical[1]):
        first_size = panel_width
        second_size = panel_height
    else:
        first_size = panel_height
        second_size = panel_width

    # Agregamos todos los paneles posibles que quepan de manera horizontal
    if 0 not in Horizontal:
        for i in list(range(0, len(roof), first_size)):
            for j in list(range(0, len(roof[0]), second_size)):
                add_count, roof = add_panel([i, j], [first_size, second_size], roof, n_total)
                n_total = n_total + (add_count  / (first_size * second_size))

    # Agregamos todos los paneles posibles que quepan de manera vertical en el espacio restante
    if 0 not in Vertical:
        for i in list(range(0, len(roof), second_size)):
            for j in list(range(0, len(roof[0]), first_size)):
                add_count, roof = add_panel([i, j], [second_size, first_size], roof, n_total)
                n_total = n_total + (add_count  / (first_size * second_size))

    else:
        pass

    print(roof)
    return n_total


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
