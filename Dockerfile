FROM alpine:latest


RUN apk update && apk upgrade && \ 
	apk add --no-cache python3-dev && \
	apk add --no-cache --virtual .build-deps g++ && \
	apk add --update --no-cache git
	
	
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN git clone https://github.com/cunyfalldata622s2/homework3-JoshuaSturm /usr/src/app/homework3/
EXPOSE 5000
CMD [ "python", "/usr/src/app/homework3/pull_data.py" ]