FROM python:3.5
MAINTAINER swapnil
WORKDIR /calculator
ADD . /calculator
EXPOSE 4000
CMD ["python","calc.py"]
