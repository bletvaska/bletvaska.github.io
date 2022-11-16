FROM python:3.10-slim

LABEL author="mirek <mirek@cnl.sk>"

COPY project/dist/supa-0.1.0-py3-none-any.whl /tmp/

RUN pip install /tmp/supa-0.1.0-py3-none-any.whl

EXPOSE 8000

CMD [ "supa" ]
