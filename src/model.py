import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed, fc1_units=8, fc2_units=8, useDueling=True):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            fc1_units (int): Number of nodes in first hidden layer
            fc2_units (int): Number of nodes in second hidden layer
        """
        self.useDueling = useDueling

        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(state_size, fc1_units)
        self.fc2 = nn.Linear(fc1_units, fc2_units)
        if self.useDueling:
            self.fc3_value = nn.Linear(fc2_units, 1)
            self.fc3_advantage = nn.Linear(fc2_units, action_size)
        else:
            self.fc3 = nn.Linear(fc2_units, action_size)

    def forward(self, state):
        """Build a network that maps state -> action values."""
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))
        if self.useDueling:
            value = self.fc3_value(x)
            advantage = self.fc3_advantage(x)
            #print('\rvalue:', value, '\tadvantage:', advantage, end='')
            actionValues = value + advantage - advantage.mean()
            return actionValues
        else:
            return self.fc3(x)
