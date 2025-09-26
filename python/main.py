from typing import List, Tuple, Dict
import json, math
import numpy as np
from functions import panel_positioning


def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:

    # Booleano que define si el techo es rectangular o en forma de triangulo isosceles
    rectangular = True

    # Definimos dos grilla que representan nuestro techo vacio
    if rectangular:
        roof_1 = np.zeros((roof_height, roof_width))
        roof_2 = np.zeros((roof_height, roof_width))

    # Para el caso de un techo con forma de triangulo isosceles, rellenamos la grilla con -1 en las posiciones que no existen
    else:
        roof_1 = np.ones((roof_height, roof_width)) * -1
        roof_2 = np.ones((roof_height, roof_width)) * -1
        center = roof_width // 2
        for i in range(roof_height):
            left = max(center - i, 0)
            right = min(center + i + 1, roof_width)
            roof_1[i, left:right] = 0
            roof_2[i, left:right] = 0

    # Contadores para cuatos paneles hemos agregado
    n_total_1 = 0
    n_total_2 = 0

    # Sirve para determinar si es posible orientar los paneles de manera horizontal y/o vertical
    Vertical = math.floor(roof_width / panel_width), math.floor(roof_height  /panel_height)
    Horizontal = math.floor(roof_width / panel_height), math.floor(roof_height / panel_width)

    # Agregamos todos los paneles posibles que quepan de manera horizontal
    if 0 not in Horizontal:
        n_total_1, roof_1 = panel_positioning([panel_width, panel_height], roof_1, n_total_1, rectangular)

    # Agregamos todos los paneles posibles que quepan de manera vertical en el espacio restante
    if 0 not in Vertical:
        n_total_1, roof_1 = panel_positioning([panel_height, panel_width], roof_1, n_total_1, rectangular)

        # Rellenamos el segundo techo en la otra direccion, para ver si una de las dos permite mas paneles
        n_total_2, roof_2 = panel_positioning([panel_height, panel_width], roof_2, n_total_2, rectangular)

    if 0 not in Horizontal:
        n_total_2, roof_2 = panel_positioning([panel_width, panel_height], roof_2, n_total_2, rectangular)

    # Revisamos cual configuracion es mejor
    if n_total_1 >= n_total_2:
        print(roof_1)
        return n_total_1
    else:
        print(roof_2)
        return n_total_2


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
