#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Han Xiao <artex.xh@gmail.com> <https://hanxiao.github.io>

# NOTE: First install bert-as-service via
# $
# $ pip install serving-server
# $ pip install serving-client
# $

# visualizing a 12-layer BERT

import time
from collections import namedtuple

import numpy as np
import pandas as pd
# from MulticoreTSNE import MulticoreTSNE as TSNE
from transformer_serving.client import BertClient
from transformer_serving.server import BertServer
from transformer_serving.server.helper import get_args_parser





pool_layer = 1
subset_vec_all_layers = []
port = 6006
port_out = 6007

common = [
    '-model_dir', '/home/faith/torch_serving/ALBERT',
    '-num_worker', '1',
    '-port', str(port),
    '-port_out', str(port_out),
    '-max_seq_len', '20',
    # '-client_batch_size', '2048',
    '-max_batch_size', '256',
    # '-num_client', '1',
    # '-pooling_strategy', 'REDUCE_MEAN',
    '-pooling_layer', '-2',
    '-gpu_memory_fraction', '0.2',
    '-device','0',
    # '-http_port', '8125'
]
args = get_args_parser().parse_args(common)
print(args)

server = BertServer(args)
server.start()

# for pool_layer in range(1, 13):
#     setattr(args, 'pooling_layer', [-pool_layer])
#     server = BertServer(args)
#     server.start()
    # print('wait until server is ready...')
    # time.sleep(20)
    # print('encoding...')
    # bc = BertClient(port=port, port_out=port_out, show_server_config=True)
    # subset_vec_all_layers.append(bc.encode(subset_text))
    # bc.close()
    # server.close()
    # print('done at layer -%d' % pool_layer)

