REG="kubeflowmnist2024001.azurecr.io/mnist-demo"
IMAGE_TRAIN=train-model
IMAGE_PREDICT=predict-model

IMAGE_TRAIN_TAG=$REG/$IMAGE_TRAIN:no-entory-tfimage
IMAGE_PREDICT_TAG=$REG/$IMAGE_PREDICT:no-entory-tfimage

docker build -t $IMAGE_TRAIN_TAG -f Dockerfile.train .
docker build -t $IMAGE_PREDICT_TAG -f Dockerfile.predict .

docker push $IMAGE_TRAIN_TAG
socker push $IMAGE_PREDICT_TAG

echo TAG:
echo $IMAGE_TRAIN_TAG
echo $IMAGE_PREDICT_TAG

