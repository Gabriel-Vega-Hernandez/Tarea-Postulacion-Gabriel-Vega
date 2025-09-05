# Tarea Dev Junior - Ruuf

## 🎯 Objetivo

El objetivo de este ejercicio es poder entender tus habilidades como programador/a, la forma en que planteas un problema, cómo los resuelves y finalmente cómo comunicas tu forma de razonar y resultados.

## 🛠️ Problema

El problema a resolver consiste en encontrar la máxima cantidad de rectángulos de dimensiones "a" y "b" (paneles solares) que caben dentro de un rectángulo de dimensiones "x" e "y" (techo).

## 🚀 Cómo Empezar

### Opción 1: Solución en TypeScript
```bash
cd typescript
npm install
npm start
```

### Opción 2: Solución en Python
```bash
cd python
python3 main.py
```

## ✅ Casos de Prueba

Tu solución debe pasar los siguientes casos de prueba:
- Paneles 1x2 y techo 2x4 ⇒ Caben 4
- Paneles 1x2 y techo 3x5 ⇒ Caben 7
- Paneles 2x2 y techo 1x10 ⇒ Caben 0

---

## 📝 Tu Solución

Como mencione en la zona de supuestos, mi código funciona bajo la asumpción de que al rellenar el techo con la mayor cantidad posible de paneles en una orientación y luego colocar todos los paneles que quepan en la otra orientación, se obtendrá la máxima cantidad de paneles para un techo dado. Con lo anterior en mente el código inicia creando dos grillas de ceros con las dimensiones del techo pues una se rellenará de manera horizontal primero mientras que la otra partirá llenándose de manera vertical. También se crea un contador de paneles para cada grilla, de esta manera podemos tomar la grilla con el mayor número de paneles como resultado final.

A continuación, creamos dos tuplas que nos permitiran discernir si es posible colocar al menos 1 panel en una cierta orientación, pues si al menos uno de los elementos de estas tuplas es 0, eso quiere decir que la dimensión del techo es menor que la del panel en esa orientación y por tanto no es posible colocarlo.

El siguiente paso consiste en colocar todos los paneles posibles en las orientaciones correspondientes. Para esto se hace uso de la función `panel_positioning()` que chequea la grilla a intervalos dados por el tamaño del panel y agrega un panel nuevo cuando corresponda mediante la función `add_panel()`. Esta última función hace un par de chequeos, como revisar que no haya otro panel en el espacio a rellenar mediante la función `check_availability()` y que el panel no se salga del techo, antes de reemplazar los elementos de la grilla por el número de panel correspondiente.

Una vez se tienen ambas grillas que representan nuestro techo, se compara cuál de las dos tiene el mayor número de paneles y se retorna dicho número. También hay un print() que permite ver la disposición de los paneles en consola.

---

## 💰 Bonus (Opcional)

Si completaste alguno de los ejercicios bonus, explica tu solución aquí:

### Bonus Implementado

Implemente el bonus 1, un techo triangular, asumiendo que la base sería roof_width y la altura roof_height.


### Explicación del Bonus

Hubo tres alteraciones que se realizaron para resolver el bonus:
- Se agregó un booleano para decidir qué tipo de techo se requiere
- Se agregó una sección que modifica las grillas de techo para rellenar los espacios no válidos con -1 y dejar una forma triangular de ceros.
- Se modificó la función panel_positioning() de tal manera que si el techo no es rectangular, chequee todos los espacios de la grilla y no solo en intervalos del tamaño de los paneles.

Una vez hecho esto, la logica es la misma que en el caso rectangular.


---

## 🤔 Supuestos y Decisiones

Hubo dos suposiciones que se hicieron para resolver el ejercicio:
- Los paneles solo pueden ir de manera horizontal o vertical, pues el agregar rotaciones adicionales aumenta la dificultad de una manera muy alta para el tiempo dado.
- Llenar el espacio con todos los paneles posibles en una dirección y luego en la otra resultará en la máxima cantidad de paneles. No estoy seguro de si es el caso, pero como no pude pensar en ningún contraejemplo decidí asumir que sería suficiente.


