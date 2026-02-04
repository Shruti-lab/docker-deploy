FROM python:3.11-slim


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV USERNAME=myapp
ENV WORKING_DIR=/app

RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd ${USERNAME} && \
    useradd -g ${USERNAME} ${USERNAME}

RUN mkdir -p ${WORKING_DIR}
WORKDIR ${WORKING_DIR}


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


RUN chown -R ${USERNAME}:${USERNAME} ${WORKING_DIR}
RUN chmod -R u=rwx,g=rwx ${WORKING_DIR}
RUN chmod +x entrypoint.sh


USER ${USERNAME}


ENV FLASK_APP=run.py


EXPOSE 5000
RUN flask db init

ENTRYPOINT [ "./entrypoint.sh" ]




