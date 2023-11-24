import torch
import math

dtype = torch.float
device = "cuda" if torch.cuda.is_available() else "cpu"
torch.set_default_device(device)

x = torch.linspace(-math.pi, math.pi, 2000, dtype = dtype)
y = torch.sin(x)

# Create random Tensors for weights. For a third order polynomial, we need
# 4 weights: y = a + b x + c x^2 + d x^3
a = torch.randn((), dtype = dtype, requires_grad = True)
b = torch.randn((), dtype = dtype, requires_grad = True)
c = torch.randn((), dtype = dtype, requires_grad = True)
d = torch.randn((), dtype = dtype, requires_grad = True)

learning_rate = 1e-6
for t in range(2000):
    y_pred = a + b * x + c * x **2 + d * x ** 3

    loss = (y_pred -y).pow(2).sum()
    if t % 100 == 99:
        print(t, loss.item())

    loss.backward()

    with torch.no_grad():
        a -= learning_rate * a.grad
        b -= learning_rate * b.grad
        c -= learning_rate * c.grad
        d -= learning_rate * d.grad

        a.grad = None
        b.grad = None
        c.grad = None
        d.grad = None

print(f"Result: y = {a.item()} + {b.item()}x + {c.item()}x^2 + {d.item()}x^3")

