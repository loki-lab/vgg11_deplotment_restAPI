import torch
from torchvision import transforms
from PIL import Image
import io


def load_model(path, model_arch):
    weight = torch.load(path)
    model = model_arch
    model.load_state_dict(weight)

    return model


def transform_image(image):
    transform = transforms.Compose([transforms.Resize((224, 224), antialias=True),
                                    transforms.ToTensor(),
                                    transforms.Normalize((0.5,), (0.5,))])

    img = Image.open(io.BytesIO(image))

    return transform(img).unsqueeze(0)
