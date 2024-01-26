REGISTORY="kubeflowmnist2024001.azurecr.io"
REPO=notebook-demo
IMAGE_NAME=jupyter
TAG=ngc-01

IMAGE_TAG=$REGISTORY/$REPO/$IMAGE_NAME:$TAG

docker build -t $IMAGE_TAG -f Dockerfile.${IMAGE_NAME}_${TAG} .
docker push $IMAGE_TAG

echo TAG: $IMAGE_TAG

