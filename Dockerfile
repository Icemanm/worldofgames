FROM python
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir /app
WORKDIR /app
CMD python MainScores.py

