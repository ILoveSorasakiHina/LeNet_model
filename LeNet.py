import torch
import torch.nn as nn
import torch.nn.functional as F


class LeNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1,6,kernel_size = 5)
        self.pool1 = nn.AvgPool2d(kernel_size = 2,stride = 2)
        self.conv2 = nn.Conv2d(6,16,kernel_size = 5)
        self.pool2 = nn.AvgPool2d(kernel_size = 2,stride = 2)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)
    
    def forward(self,input):
        x = self.pool1(F.relu(self.conv1(x)))
        x = self.pool2(F.relu(self.conv2(x)))
        x = torch.flatten(x,1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)

        return input

net = LeNet()
print(net)

