import * as fs from 'fs';
import { panel_positioning } from './functions';

import express from 'express';
import cors from 'cors';

interface TestCase {
    panelW: number;
    panelH: number;
    roofW: number;
    roofH: number;
    expected: number;
}

interface TestData {
    testCases: TestCase[];
}

function calculatePanels(
    panelWidth: number,
    panelHeight: number,
    roofWidth: number,
    roofHeight: number
): [number, number[][]] {

    const rectangular: boolean = true;

    // Definimos dos grilla que representan nuestro techo, actualmente no tienen ningun espacio disponible
    let roof_1: number[][];
    let roof_2: number[][];

    // En caso de que el techo sea rectangular, llenamos toda la grilla con espacios disponibles
    if (rectangular){
        roof_1 = Array.from({ length: roofHeight }, () => Array(roofWidth).fill(0));
        roof_2 = Array.from({ length: roofHeight }, () => Array(roofWidth).fill(0));
    }

    // En caso de que el techo sea triangular, llenamos la grilla con espacios disponibles en forma de triangulo
    else {
        roof_1 = Array.from({ length: roofHeight }, () => Array(roofWidth).fill(-1));
        roof_2 = Array.from({ length: roofHeight }, () => Array(roofWidth).fill(-1));
        const center = Math.floor(roofWidth / 2);
        for (let i = 0; i < roofHeight; i++) {
            const left = Math.max(center - i, 0);
            const right = Math.min(center + i + 1, roofWidth);
            for (let j = left; j < right; j++) {
                roof_1[i][j] = 0;
                roof_2[i][j] = 0;
            }

        }
    }


    // Contadores para cuatos paneles hemos agregado
    let n_total_1: number = 0;
    let n_total_2: number = 0;

    // Sirve para determinar si es posible orientar los paneles de manera horizontal y/o vertical
    const horizontal: [number, number] = [Math.floor(roofWidth / panelWidth), Math.floor(roofHeight / panelHeight)];
    const vertical: [number, number] = [Math.floor(roofWidth / panelHeight), Math.floor(roofHeight / panelWidth)];

    // Agregamos todos los paneles posibles que quepan de manera horizontal
    if (horizontal[0]!=0 && horizontal[1]!=0){
        [n_total_1, roof_1] = panel_positioning([panelWidth, panelHeight], roof_1, n_total_1);
    }

    // Agregamos todos los paneles posibles que quepan de manera vertical en el espacio restante
    if (vertical[0]!=0 && vertical[1]!=0){
        [n_total_1, roof_1] = panel_positioning([panelHeight, panelWidth], roof_1, n_total_1);

        // Rellenamos el segundo techo en la otra direccion, para ver si una de las dos permite mas paneles
        [n_total_2, roof_2] = panel_positioning([panelHeight, panelWidth], roof_2, n_total_2);
    }
    
    if (horizontal[0]!=0 && horizontal[1]!=0){
            [n_total_2, roof_2] = panel_positioning([panelWidth, panelHeight], roof_2, n_total_2);
    }

    // Revisamos cual configuracion es mejor
    if (n_total_1 >= n_total_2){
        return [n_total_1, roof_1];
    } else {
        return [n_total_2, roof_2];
    }

}

function main(): void {
    console.log("🐕 Wuuf wuuf wuuf 🐕");
    console.log("================================\n");
    
    runTests();
}

function runTests(): void {
    const data: TestData = JSON.parse(fs.readFileSync('test_cases.json', 'utf-8'));
    const testCases = data.testCases;
    
    console.log("Corriendo tests:");
    console.log("-------------------");

    let list_of_roofs: number[][][] = [];
    
    testCases.forEach((test: TestCase, index: number) => {
        let [result, roof] = calculatePanels(test.panelW, test.panelH, test.roofW, test.roofH);
        const passed = result === test.expected;
        list_of_roofs.push(roof);
        console.log(roof);
        
        console.log(`Test ${index + 1}:`);
        console.log(`  Panels: ${test.panelW}x${test.panelH}, Roof: ${test.roofW}x${test.roofH}`);
        console.log(`  Expected: ${test.expected}, Got: ${result}`);
        console.log(`  Status: ${passed ? "✅ PASSED" : "❌ FAILED"}\n`);
    });

    const app = express();
    const port = 3000;

    app.use(cors());

    app.get('/array', (_req, res) => {
        res.json(list_of_roofs);
    });
    
    app.listen(port, () => {
        console.log(`Server running at http://localhost:${port}`);
    });
}

main();