import torch


class InferenceModel:
    def __init__(self, model, transform, device):
        self.model = model
        self.transform = transform
        self.device = device

    def predict(self, img):
        img = self.transform(img)

        self.model.eval()
        output = self.model(img)

        _, predicted = torch.max(output.data, 1)

        return predicted.item()

    def show_arch(self):
        print(self.model)
