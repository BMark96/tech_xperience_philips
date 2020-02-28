FROM tensorflow/tensorflow:latest-py3

RUN mkdir -p /model
RUN mkdir -p /data
RUN mkdir -p /prediction

ADD src/predict.py /
ADD model/model_philips.h5 /model/
ADD data /data

RUN pip install numpy pillow

CMD [ "python", "predict.py" ]