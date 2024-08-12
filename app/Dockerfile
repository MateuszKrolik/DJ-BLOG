FROM public.ecr.aws/lambda/python:3.12

COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN pip install -r requirements.txt --upgrade

# For local testing.
EXPOSE 8000

COPY src/ ${LAMBDA_TASK_ROOT}