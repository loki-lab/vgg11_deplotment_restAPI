import requests


if __name__ == "__main__":
    url = "http://127.0.0.1:8080/vgg11_cat_and_dog"

    response = requests.post(url, files={"image": open('./img/dog_01.jpg', 'rb')})

    print(response.json())
