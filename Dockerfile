FROM continuumio/miniconda3

RUN mkdir wd
WORKDIR /wd

ENV DASH_DEBUG_MODE True
COPY app/requirements.txt .

RUN conda install -c conda-forge --file requirements.txt --yes

COPY app/ ./app
COPY data/ ./data

WORKDIR /wd/app/
EXPOSE 8020

CMD gunicorn --workers=1 --threads=2 -b 0.0.0.0:$PORT app:server
#----------------------------------------------------------------
#make reqs file
#conda list -e > requirements.txt
#----------------------------------------------------------------
#add to heroku
#TODO make new project
#heroku container:login
#heroku container:push web
#heroku container:release web
#heroku ps:scale web=1
#----------------------------------------------------------------
#local testing
#docker build -t personal .
#docker run -p 8020:8020 -e PORT=8020 personal
#----------------------------------------------------------------
