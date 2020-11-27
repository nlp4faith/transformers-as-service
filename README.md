<h1 align="center">transformer-as-service</h1>

<p align="center">Using transformer pretrained model as a sentence encoding service, i.e. mapping a variable-length sentence to a fixed-length vector.</p>

Thanks for the idea from [bert-as-serivce](https://github.com/hanxiao/bert-as-service)





serving-start -http_port 8125 -num_worker 32 -http_max_connect 500 -model_dir /model/transformer/ALBERT -device_map 0 1


sudo docker run  --rm -dit -p 5555:5555 -p 5556:5556 -p 8125:8125 -v /home/faith/transformer_model/ALBERT:/model --name ts_serving --entrypoint serving-start -t transformer-service -http_port 8125 -num_worker 32 -http_max_connect 500 -model_dir /model -device_map 0


docker run  --rm -dit -p 5555:5555 -p 5556:5556 -p 8125:8125 -v /smb/AI_models/transformer/ALBERT:/model --name ts_serving --entrypoint serving-start -t transformer-service -http_port 8125 -num_worker 32 -http_max_connect 500 -model_dir /model -device_map 0


curl -X POST -d '{"id": 123, "texts":["some texts"]}' -H "Content-Type: Application/json" 127.0.0.1:8125/encode  -vv

ab -c 500 -t 30 -p data.json -T 'application/json' -r  127.0.0.1:8125/encode

serving-start -http_port 8125 -num_worker 2 -http_max_connect 1000 -model_dir /home/faith/transformer_model/ALBERT -device_map 0