
from transformer_serving.server.http import BertHTTPProxy


if __name__ == "__main__":
    from transformer_serving.server.helper import get_args_parser
    port = 5555
    port_out = 5556
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
        '-device', '0',
        '-http_port', '8125'
    ]
    args = get_args_parser().parse_args(common)
    print(args)
    proc_proxy = BertHTTPProxy(args)
    proc_proxy.start()
