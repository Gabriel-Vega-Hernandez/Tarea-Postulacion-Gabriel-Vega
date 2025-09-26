export function check_availability(panel_position: [number, number],
                            panel_size: [number, number],
                            roof: number[][]): boolean {

    for (let i = 0; i < panel_size[0]; i++) {
        for (let j = 0; j < panel_size[1]; j++) {
            // Me aseguro de que este espacion no este siendo ocupado por otro panel
            if (roof[panel_position[0] + i][panel_position[1] + j] != 0) {
                return false;
            }
        }
    }

    return true;
}

export function add_panel(panel_position: [number, number], panel_size: [number, number],
    roof: number[][], n_panel: number): [number, number[][]] {

    let count: number = 0;

    // Primero me fijo en si un panel que parte en la posicion dada, es capaz de entrar en la grilla
    if (panel_position[0] + panel_size[0] > roof.length || panel_position[1] + panel_size[1] > roof[0].length) {
        return [0, roof];
    }else if (!check_availability(panel_position, panel_size, roof)) {
        return [0, roof];
    } else {
        for (let i = 0; i < panel_size[0]; i++) {
            for (let j = 0; j < panel_size[1]; j++) {
                // Relleno los espacion correspondientes con un nuevo panel
                roof[panel_position[0] + i][panel_position[1] + j] = n_panel + 1;
                count += 1;
            }
        }
        return [count, roof];
    }
}

export function panel_positioning(panel_orientation: [number, number],
                           roof: number[][], n_panel: number): [number, number[][]] {
    // Recorremos toda la grilla
    for (let i=0; i < roof.length; i++) {
        for (let j=0; j < roof[0].length; j++) {
            let [add_count, updated_roof] = add_panel([i, j], [panel_orientation[0], panel_orientation[1]], roof, n_panel);
            n_panel += add_count / (panel_orientation[0] * panel_orientation[1]);
            roof = updated_roof;
        }
    }
    
    return [n_panel, roof];

}