import torch
import torch.autograd

x = torch.arange(4.0)
print("x = {}".format(x))

x.requires_grad_(True)  # Enable gradient tracking for x
print("x.grad = ", x.grad)  # Corrected the print statement - print the value of x.grad

y = 2 * torch.dot(x, x)
print("x = ", x)
print("y = ", y)

# Backpropagation to compute gradients
y.backward()
print("x.grad = ", x.grad)  # Print the gradients of x
