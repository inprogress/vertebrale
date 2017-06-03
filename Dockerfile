FROM frolvlad/alpine-python3

WORKDIR .
ADD . .
RUN pip install -r requirements.txt
RUN alembic upgrade head
EXPOSE 5000

ENTRYPOINT ["python3", "-m", "vertebrale"]
