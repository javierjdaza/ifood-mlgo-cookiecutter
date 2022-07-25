# Basic Slim Python Image
FROM python:3.7-slim-stretch

RUN mkdir -p /opt/ml
WORKDIR /opt/ml/

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE


ADD dependencies dependencies/
ADD requirements.txt .
RUN pip install -r requirements.txt && rm -rf /root/.cache && rm -rf /dependencies/

COPY ./ /opt/ml/
ENV PATH="/opt/ml/sgmk:${PATH}"

RUN chmod +x /opt/ml/sgmk/*


EXPOSE 8080


