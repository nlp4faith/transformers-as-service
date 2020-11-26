<h1 align="center">transformer-as-service</h1>

<p align="center">Using transformer pretrained model as a sentence encoding service, i.e. mapping a variable-length sentence to a fixed-length vector.</p>

Thanks for the idea from [bert-as-serivce](https://github.com/hanxiao/bert-as-service)





docker run --runtime nvidia -dit -p 5555:5555 -p 5556:5556 -p 8125:8125 -v /smb/AI_models/transformer/ALBERT:/model --name ts_serving --entrypoint serving-start -t 10.11.32.52:8000/transformer-as-service -http_port 8125 -num_worker 32 -http_max_connect 500 -model_dir /model -device_map 0 1