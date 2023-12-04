import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.modules.utils import _pair

class DepthwiseConv2d(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, depth_multiplier=1):
        super(DepthwiseConv2d, self).__init__()
        self.depthwise = nn.Conv2d(in_channels, in_channels * depth_multiplier, 
                                   kernel_size=kernel_size, groups=in_channels,
                                   padding='same')
        self.pointwise = nn.Conv2d(in_channels * depth_multiplier, out_channels,
                                   kernel_size=1)

    def forward(self, x):
        out = self.depthwise(x)
        out = self.pointwise(out)
        return out

class EEGNet(nn.Module):
    def __init__(self, nb_classes, Chans=64, Samples=128, dropoutRate=0.5, kernLength=64, F1=8, D=2, F2=16, norm_rate=0.25, dropoutType='Dropout'):
        super(EEGNet, self).__init__()
        
        if dropoutType == 'SpatialDropout2D':
            self.dropoutType = nn.Dropout2d
        elif dropoutType == 'Dropout':
            self.dropoutType = nn.Dropout
        else:
            raise ValueError('dropoutType must be one of SpatialDropout2D or Dropout, passed as a string.')

        self.block1 = nn.Sequential(
            nn.Conv2d(1, F1, (1, kernLength), padding='same', bias=False),
            nn.BatchNorm2d(F1),
            DepthwiseConv2d(F1, F1 * D, (Chans, 1), depth_multiplier=D),
            nn.BatchNorm2d(F1 * D),
            nn.ELU(),
            nn.AvgPool2d((1, 4)),
            self.dropoutType(dropoutRate)
        )

        self.block2 = nn.Sequential(
            DepthwiseConv2d(F1 * D, F2, (1, 16), padding='same'),
            nn.BatchNorm2d(F2),
            nn.ELU(),
            nn.AvgPool2d((1, 8)),
            self.dropoutType(dropoutRate)
        )

        self.classify = nn.Sequential(
            nn.Flatten(),
            nn.Linear(F2 * (Samples // 32), nb_classes),
            nn.Softmax(dim=1)
        )

    def forward(self, x):
        x = self.block1(x)
        x = self.block2(x)
        x = self.classify(x)
        return x

# Example usage:
# model = EEGNet(nb_classes=10, Chans=64, Samples=128)
# print(model)
