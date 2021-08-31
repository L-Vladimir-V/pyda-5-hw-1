FROM continuumio/miniconda3:latest

LABEL mainteiner="Vladimir Leshnevskij"

RUN set -x \
    && apt-get update -yqq \
    && apt-get upgrade -yqq \
    && python3 -m venv /env \
    && . /env/bin/activate \
    && pip install -U pip \
    && pip install mlflow boto3 pymysql \
    && apt-get purge -yqq \
    && apt-get autoremove -yqq \
    && apt-get clean \
    && rm -rf \
        /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/* \
        /usr/share/man \
        /usr/share/doc \
        /usr/share/doc-base

COPY app /app

RUN chmod +x /app/1.sh

CMD ["/app/1.sh"]
