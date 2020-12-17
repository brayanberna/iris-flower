# Iris flower - Desarrollado en Django (Python)
Proyecto de práctica utilizando redes neuronales.
## Live Preview:
- **https://flower-iris.herokuapp.com/**
## Herramientas usadas en el proyecto:
- **[Python 3.7](https://www.python.org/)**  Lenguaje de programación.
- **[Django](https://www.djangoproject.com/)**  Framework de desarrollo web de código abierto, escrito en Python.
- **[Font Awesome](https://fontawesome.com/icons?d=gallery)**  Framework de iconos vectoriales.
- **[TensorFlow](https://www.tensorflow.org/)** Biblioteca de código abierto para Machine Learning. <br> <br>
![](https://repository-images.githubusercontent.com/312633712/b9680b00-26e2-11eb-8dcd-3a87f7dbae91)
![Imagen2](https://user-images.githubusercontent.com/61950433/99163032-fa601f80-26e2-11eb-98aa-6a1cca9d7cec.PNG)
# Explicación
- Este proyecto utiliza el aprendizaje automático para clasificar las flores de iris por especie. Se estructura de la siguiente forma:
  - 1. Importa y analiza el conjunto de datos.
  - 2. Selecciona el tipo de modelo.
  - 3. Entrena al modelo.
  - 4. Se evalúa la efectividad del modelo.
  - 5. Utilice el modelo entrenado para hacer predicciones.
  
- Necesitamos seleccionar el tipo de modelo a entrenar. Hay muchos tipos de modelos y elegir uno bueno requiere experiencia. Este proyecto utiliza una red neuronal para resolver el problema de clasificación de Iris. Las redes neuronales pueden encontrar relaciones complejas entre las características y la etiqueta. Es un gráfico muy estructurado, organizado en una o más capas ocultas . Cada capa oculta consta de una o más neuronas . Hay varias categorías de redes neuronales y este proyecto utiliza una red neuronal densa o completamente conectada : las neuronas de una capa reciben conexiones de entrada de todas las neuronas de la capa anterior. Por ejemplo, en la Figura se ilustra una red neuronal densa que consta de una capa de entrada, dos capas ocultas y una capa de salida: <br> <br>

![full_network](https://user-images.githubusercontent.com/61950433/99177807-b291c600-26eb-11eb-963c-a20f7dfe370e.png)

- Cuando el modelo de la red neuronal de la Figura  se entrena y se alimenta con un ejemplo sin etiquetar, arroja tres predicciones: la probabilidad de que esta flor sea la especie de Iris dada. Esta predicción se llama inferencia . Para este ejemplo, la suma de las predicciones de salida es 1.0. En la Figura, esta predicción se desglosa como: 0.02 para Iris setosa , 0.95 para Iris versicolor y 0.03 para Iris virginica . Esto significa que el modelo predice, con un 95% de probabilidad, que una flor de ejemplo sin etiquetar es una Iris versicolor .
