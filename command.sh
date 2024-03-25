docker build . -t vgg11_cat_and_dog_restapi
docker run --rm -p 8080:5003 --name cat_and_dog_ai  vgg11_cat_and_dog_restapi
