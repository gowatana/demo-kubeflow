# demo-kubeflow

Run Jupyter Notebook (Kubeflow TensorFlow Full)
```
docker run -it -p 80:8888 -v $(pwd):/workspace kubeflownotebookswg/jupyter-tensorflow-full:v1.6.0
```

Run Jupyter Notebook (NGC TensorFlow)
```
docker run -it -p 80:8888 -v $(pwd):/workspace kubeflowmnist2024001.azurecr.io/notebook-demo/jupyter:ngc
```
