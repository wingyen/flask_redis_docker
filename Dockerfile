FROM python:3.8-alpine
WORKDIR /app
ENV FLASK_APP=./app/main.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
ENV PATH=/app/.virtualenvs/bin:$PATH
RUN pip3 install -r requirements.txt
EXPOSE 5000
COPY . .

ENV FLASK_DEBUG 1
CMD ["flask", "run"]