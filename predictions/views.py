from django.shortcuts import render
import tensorflow as tf
from tensorflow.keras.models import load_model

# Create your views here.

def index(request):
  if request.method == 'POST':
    modelo='predictions/modelos/modelo_entrenado.h5'
    pesos='predictions/modelos/pesos_modelo_entrenado.h5'
    model = load_model(modelo)
    model.load_weights(pesos)

    class_names = ['Iris setosa', 'Iris versicolor', 'Iris virginica']

    largo_sepalo = request.POST['largo_sepalo']
    ancho_sepalo = request.POST['ancho_sepalo']
    largo_petalo = request.POST['largo_petalo']
    ancho_petalo = request.POST['ancho_petalo']

    predict_dataset = tf.convert_to_tensor([
    [float(largo_sepalo), float(ancho_sepalo), float(largo_petalo), float(ancho_petalo)]
    ])
    predictions = model(predict_dataset, training=False)

    for i, logits in enumerate(predictions):
      class_idx = tf.argmax(logits).numpy()
      p = tf.nn.softmax(logits)[class_idx]
      name = class_names[class_idx]
      return render(request, 'index.html', {
            'name': name,
            'porcentaje': "{0:.1f}".format(100*p)
            })

  return render(request, 'index.html')