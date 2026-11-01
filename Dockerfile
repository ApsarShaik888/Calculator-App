#downloads python base image
FROM python:3.10-slim

#Creates and uses /app inside container.
WORKDIR /app

#Copies your calculator code into container.
COPY . .

#run the calculator app code in container
CMD ["python","calculator.py"]



