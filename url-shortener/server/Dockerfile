FROM amazonlinux:2

RUN yum install -y shadow-utils wget tar gzip gcc make && \
    wget https://www.sqlite.org/2019/sqlite-autoconf-3270100.tar.gz && \
    tar xvfz sqlite-autoconf-3270100.tar.gz && \
    cd sqlite-autoconf-3270100 && \
    ./configure --prefix=/usr/local && \
    make && \
    make install && \
    mv /usr/bin/sqlite3 /usr/bin/sqlite3_old && \
    ln -s /usr/local/bin/sqlite3 /usr/bin/sqlite3

RUN yum install -y openssl11-devel bzip2-devel libffi-devel zip && \
    cd /opt && \
    wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz && \
    tar xzf Python-3.9.6.tgz

RUN /opt/Python-3.9.6/configure --enable-optimizations

RUN make altinstall && \
    rm -f /opt/Python-3.9.6.tgz

RUN python3.9 -m pip install --upgrade pip

WORKDIR /shorten-url/app

COPY ./pyproject.toml ./poetry.lock ./

RUN python3.9 -m pip install poetry \
    && python3.9 -m poetry export --without-hashes -f requirements.txt --output requirements.txt

RUN python3.9 -m pip install -r requirements.txt

COPY ./bin ./
COPY ./src ./

RUN mkdir -p /shorten-url/db
RUN mkdir -p /shorten-url/log
RUN chmod 777 /shorten-url/db /shorten-url/log

RUN groupadd -r shorten-url && useradd -r -g shorten-url shorten-url
USER shorten-url

ENTRYPOINT ["sh", "-c", "./main.sh"]
