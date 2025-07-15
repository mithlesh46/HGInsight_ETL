FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Install cron
RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

# Add crontab file
COPY docker/elt_cron /etc/cron.d/elt_cron
RUN chmod 0644 /etc/cron.d/elt_cron && crontab /etc/cron.d/elt_cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

CMD cron && tail -f /var/log/cron.log
