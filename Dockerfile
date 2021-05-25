#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
#
#COPY ./app /app
#
##CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
#
#


#docker build -t myimage .
#docker run -d --name mycontainer -p 80:80 myimage

#FROM python:3.7
#
#COPY ./app /app
#
#RUN pip install fastapi uvicorn mangum
#
#EXPOSE 80
#
##CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
#
#CMD ["app.main.handler"]

FROM public.ecr.aws/lambda/python:3.8

COPY ./app ./app

RUN pip install -r app/requirements.txt

CMD ["app.app.handler"]