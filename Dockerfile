FROM python:3.10-slim-buster

RUN mkdir -p /custom-app
COPY ./api /custom-app/api

RUN pip3.10 install --no-cache-dir --upgrade -r /custom-app/api/requirements.txt

RUN adduser --system --no-create-home nonroot
RUN addgroup --system nonroot
RUN chown -R nonroot:nonroot /custom-app
USER nonroot

EXPOSE 5000

CMD ["python", "/custom-app/api/app2.py"]