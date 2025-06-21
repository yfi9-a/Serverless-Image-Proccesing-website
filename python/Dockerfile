FROM public.ecr.aws/lambda/python:3.11
WORKDIR /lambda
COPY requirements.txt .
RUN pip install -r requirements.txt -t /lambda