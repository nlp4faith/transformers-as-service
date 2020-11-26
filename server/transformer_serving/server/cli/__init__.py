def main():
    from transformer_serving.server import BertServer
    from transformer_serving.server.helper import get_run_args
    with BertServer(get_run_args()) as server:
        server.join()


def benchmark():
    from transformer_serving.server.benchmark import run_benchmark
    from transformer_serving.server.helper import get_run_args, get_benchmark_parser
    args = get_run_args(get_benchmark_parser)
    run_benchmark(args)


def terminate():
    from transformer_serving.server import BertServer
    from transformer_serving.server.helper import get_run_args, get_shutdown_parser
    args = get_run_args(get_shutdown_parser)
    BertServer.shutdown(args)
