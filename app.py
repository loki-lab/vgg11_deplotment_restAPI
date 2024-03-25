from flask import Flask, request, jsonify
import torch

from static.models import VGG11
from static.inference import InferenceModel

from static.utils import load_model, transform_image

app = Flask(__name__)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/vgg11_cat_and_dog', methods=['POST'])
def inference():
    weight_path = "static/weights/best_model.pt"
    model = load_model(weight_path, model_arch=VGG11(num_classes=2))
    infer = InferenceModel(model, device=device, transform=transform_image)

    if request.method == 'POST':
        image = request.files['image']
        image = image.read()
        output = infer.predict(image)

        return jsonify({"result": str(output)})


if __name__ == '__main__':
    app.run()
