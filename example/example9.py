#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Han Xiao <artex.xh@gmail.com> <https://hanxiao.github.io>

# NOTE: First install bert-as-service via
# $
# $ pip install bert-serving-server
# $ pip install bert-serving-client
# $

# using BertClient in sync way

import sys
import time

from bert_serving.client import BertClient

if __name__ == '__main__':
    port = 6006
    port_out = 6007
    bc = BertClient(port=port, port_out=port_out, show_server_config=True, timeout=-1)
    # encode a list of strings
    # with open('README.md') as fp:
    #     data = [v for v in fp if v.strip()][:512]
    #     num_tokens = sum(len([vv for vv in v.split() if vv.strip()]) for v in data)

    # show_tokens = len(sys.argv) > 3 and bool(sys.argv[3])
    data = ['aaaaaaaaa']
    output = bc.encode(data)  # warm-up GPU
    print(output)

