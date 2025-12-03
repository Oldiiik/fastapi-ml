# Use slim Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements (other deps) and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install PyTorch CPU version directly from PyTorch wheel
RUN pip install --no-cache-dir torch==2.1.2+cpu torchvision==0.16.2+cpu torchaudio==2.1.2+cpu \
    -f https://download.pytorch.org/whl/cpu/torch_stable.html

# Copy the rest of your app
COPY . .

# Expose port for FastAPI
EXPOSE 8000

# Run FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
