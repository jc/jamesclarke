FROM python:2.7.15-alpine3.8

WORKDIR /usr/src
RUN wget https://github.com/jc/hyde/archive/jc.zip
RUN unzip jc.zip
WORKDIR /usr/src/hyde-jc
RUN pip install --no-cache-dir -r requirements.txt

CMD python hyde.py -g -s /usr/src/jamesclarke -d /public && python /usr/src/jamesclarke/gen-now-json.py /public /usr/src/jamesclarke
