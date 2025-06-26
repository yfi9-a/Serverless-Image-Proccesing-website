FROM public.ecr.aws/lambda/python:3.11

# Install Pillow
RUN pip install pillow

# Copy function code
COPY lambda_function.py ./

CMD ["lambda_function.lambda_handler"]