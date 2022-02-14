FROM python:3.9-slim
RUN apt-get update

RUN mkdir dash_dir
WORKDIR dash_dir
COPY dash-plotly/requirements.txt .
COPY dash-plotly/ ./

RUN pip install -r requirements.txt
EXPOSE 8050
CMD ["python","dash-plotly-v1.py"]