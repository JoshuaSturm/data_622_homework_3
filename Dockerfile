FROM python:3.6


RUN pip install --upgrade pip
	
	
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN git clone https://github.com/JoshuaSturm/data_622_homework_3 /usr/src/app/homework3/
EXPOSE 5000
CMD [ "python", "/usr/src/app/homework3/pull_data.py" ]