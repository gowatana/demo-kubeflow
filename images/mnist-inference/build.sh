REGISTORY="kubeflowmnist2024001.azurecr.io"
REPO=mnist-demo
IMAGE_NAME=mnist-inference
TAG=v1
IMAGE_TAG=$REGISTORY/$REPO/$IMAGE_NAME:$TAG

docker build -t $IMAGE_TAG -f Dockerfile .
docker push $IMAGE_TAG

echo TAG: $IMAGE_TAG
