FROM docker.elastic.co/elasticsearch/elasticsearch:7.10.1

RUN elasticsearch-plugin install https://github.com/WorksApplications/elasticsearch-sudachi/releases/download/v2.1.0/analysis-sudachi-7.10.1-2.1.0.zip
RUN curl -Lo sudachi-dictionary-20211220-core.zip http://sudachi.s3-website-ap-northeast-1.amazonaws.com/sudachidict/sudachi-dictionary-20211220-core.zip && \
    unzip sudachi-dictionary-20211220-core.zip && \
    mkdir -p /usr/share/elasticsearch/config/sudachi/ && \
    mv sudachi-dictionary-20211220/system_core.dic /usr/share/elasticsearch/config/sudachi/ && \
    rm -rf sudachi-dictionary-20211220-core.zip sudachi-dictionary-20211220/

RUN curl -Lo sudachi-dictionary-20211220-full.zip http://sudachi.s3-website-ap-northeast-1.amazonaws.com/sudachidict/sudachi-dictionary-20211220-full.zip && \
    unzip sudachi-dictionary-20211220-full.zip && \
    mkdir -p /usr/share/elasticsearch/config/sudachi/ && \
    mv sudachi-dictionary-20211220/system_full.dic /usr/share/elasticsearch/config/sudachi/ && \
    rm -rf sudachi-dictionary-20211220-full.zip sudachi-dictionary-20211220/

COPY sudachi.json  /usr/share/elasticsearch/config/sudachi/
