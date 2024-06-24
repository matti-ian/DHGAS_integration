# integrated_model.py

import torch
import torch.nn as nn
from CommFormer.commformer.algorithms.mat.algorithm.cformer import CommFormer
from DHGAS.dhgas.models import load_model
from DHGAS.dhgas.data import load_data
import yaml
import box



class IntegratedModel(nn.Module):
    def __init__(self, config):
        super(IntegratedModel, self).__init__()
        # Initialize CommFormer model
        self.commformer_model = CommFormer(
            state_dim=config['commformer_params']['state_dim'],
            obs_dim=config['commformer_params']['obs_dim'],
            action_dim=config['commformer_params']['action_dim'],
            n_agent=config['commformer_params']['n_agent'],
            n_block=config['commformer_params']['n_block'],
            n_embd=config['commformer_params']['n_embd'],
            n_head=config['commformer_params']['n_head'],
            encode_state=config['commformer_params']['encode_state'],
            device=config['commformer_params']['device'],
            action_type=config['commformer_params']['action_type'],
            dec_actor=config['commformer_params']['dec_actor'],
            share_actor=config['commformer_params']['share_actor'],
            sparsity=config['commformer_params']['sparsity'],
            warmup=config['commformer_params']['warmup'],
            post_stable=config['commformer_params']['post_stable'],
            post_ratio=config['commformer_params']['post_ratio'],
            self_loop_add=config['commformer_params']['self_loop_add'],
            no_relation_enhanced=config['commformer_params']['no_relation_enhanced']
        )
        
        #load config file
        config = box.Box.from_yaml(filename='config.yaml')
        
        # Initialize DHGAS model
        dataset = load_data(config.dhgas_params)
        self.dhgas_model = load_model(config.dhgas_params, dataset)
        
        
        

    def forward(self, data):
        # Preprocess state data using DHGAS utility
        config = box.box_from_file(file='config.yaml',file_type='yaml')
        dataset = load_data(dataset= config.dhgas_params.dataset)
        # Forward pass through DHGAS model
        dhgas_output = self.dhgas_model(data)
        # Forward pass through CommFormer model with DHGAS output
        commformer_output = self.commformer_model(dhgas_output)
        return commformer_output
