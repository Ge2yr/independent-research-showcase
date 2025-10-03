""
Simple MNIST training script using PyTorch.

This script trains a small neural network on the MNIST dataset with a basic
training loop. It also includes a simple gradient norm monitor to detect
potential instability during training. No proprietary research is included.

Requires: torch, torchvision
Usage: python train_mnist.py
"""
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms

class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(28 * 28, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.flatten(x)
        x = self.relu(self.fc1(x))
        return self.fc2(x)

def gradient_norm(parameters):
    """Compute the total gradient norm."""
    total_norm = 0.0
    for p in parameters:
        if p.grad is not None:
            total_norm += p.grad.data.norm(2).item() ** 2
    return total_norm ** 0.5

def main():
    # Data loaders
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    train_dataset = datasets.MNIST('.', train=True, download=True, transform=transform)
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)

    model = SimpleNet()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    for epoch in range(3):  # Train for a few epochs
        model.train()
        for batch_idx, (data, target) in enumerate(train_loader):
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()

            # Monitor gradient norm
            grad_norm = gradient_norm(model.parameters())
            if grad_norm > 100:  # Arbitrary threshold for demonstration
                print(f"Warning: High gradient norm detected: {grad_norm:.2f} at batch {batch_idx}")

            if batch_idx % 100 == 0:
                print(f"Epoch {epoch} Batch {batch_idx}: Loss {loss.item():.4f}")

    print("Training complete.")

if __name__ == '__main__':
    main()
