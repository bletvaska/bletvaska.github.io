FROM python:3.10-slim
# FROM bletvaska/python

LABEL author="mirek <mirek@cnl.sk>"

COPY project/dist/supa-0.1.0-py3-none-any.whl /tmp/

RUN pip install /tmp/supa-0.1.0-py3-none-any.whl

HEALTHCHECK \
  --interval=10s \
  --timeout=3s \
  --retries=3 \
  --start-period=1s \
  CMD curl -f http://localhost:8000/health || exit 1

EXPOSE 8000

CMD [ "supa" ]
