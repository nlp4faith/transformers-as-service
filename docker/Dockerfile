FROM pytorch/pytorch
RUN pip install transformer-as-service[http] && pip install  -i https://pypi.tuna.tsinghua.edu.cn/simple transformers
RUN mkdir -p /app
COPY ./entrypoint.sh /app
WORKDIR /app
ENTRYPOINT ["/app/entrypoint.sh"]
CMD []
HEALTHCHECK --timeout=5s CMD curl -f http://localhost:8125/status/server || exit 1
