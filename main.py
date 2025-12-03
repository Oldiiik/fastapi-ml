from fastapi import FastAPI
import torch
from typing import List

app = FastAPI()

# Load your PyTorch model at startup
# Replace 'MyModel' with your actual class if needed
class MyModel(torch.nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        # dummy architecture; adjust if needed
        self.linear = torch.nn.Linear(10, 1)

    def forward(self, x):
        return self.linear(x)

# Load the model
model = MyModel()
model.load_state_dict(torch.load("model.pkl", map_location=torch.device("cpu")))
model.eval()

@app.post("/predict")
async def predict(features: List[float]):
    """
    features: list of floats, e.g. [1.2, 3.4, 5.6, ...]
    returns: prediction from your PyTorch model
    """
    # Convert input to tensor
    x = torch.tensor([features], dtype=torch.float32)
    with torch.no_grad():
        y = model(x).numpy().tolist()
    return {"prediction": y[0]}
