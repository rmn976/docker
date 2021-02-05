FROM alpine
RUN apk add python3 py3-pip vim 
RUN mkdir /app
ADD app_test.py /app
RUN touch /app/requirements.txt
RUN echo "virtualenv" >> /app/requirements.txt
RUN echo "flask" >> /app/requirements.txt
RUN python3 -m pip freeze
RUN python3 -m pip install -r /app/requirements.txt
CMD python3 /app/app_test.py