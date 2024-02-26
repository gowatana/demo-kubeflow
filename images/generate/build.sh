REGISTORY="kubeflowmnist2024001.azurecr.io"
REPO=llm-demo
IMAGE_NAME=generate
TAG=v2-minio
IMAGE_TAG=$REGISTORY/$REPO/$IMAGE_NAME:$TAG

docker build -t $IMAGE_TAG -f Dockerfile .
docker push $IMAGE_TAG

echo TAG: $IMAGE_TAG
