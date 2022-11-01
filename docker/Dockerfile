FROM python:3.10-bullseye

RUN mkdir -p var/www/musicians
COPY . var/www/musicians/
RUN cd var/www/musicians && pip install --no-cache-dir -r requirements.txt

WORKDIR var/www/musicians

RUN chmod +x docker/docker-entrypoint.sh

ENTRYPOINT ["docker/docker-entrypoint.sh"]
