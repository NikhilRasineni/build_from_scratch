from torch import nn
import torch

class PositionalEncoding(nn.Module):
    def __init__(self,d_model:int,sequence_len:int,dropout: float):
        super().__init__()
        self.d_model = d_model
        self.sequence_len = sequence_len
        self.drop_out =  dropout

    def forward(self):
        pe_matrix = torch.zeros(self.sequence_len,self.d_model)
        pass

