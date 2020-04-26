FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY generate-covid-visualization.py .
CMD [ "python", "./generate-covid-visualization.py" ]
