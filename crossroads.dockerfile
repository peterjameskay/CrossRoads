FROM python:3

LABEL maintainer:"peterjameskay@gmail.com"

WORKDIR C:\Users\peter\Desktop\Bash\Python\CrossRoads

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD [ "python3", "script.py" ]