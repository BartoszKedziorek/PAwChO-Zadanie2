# wybranie bazowego obrazu
FROM python:3.11.9-slim-bookworm

# autor obrazu
LABEL org.opencontainers.image.authors="Kędziorek s97633@pollub.edu.pl"

# ustawienie zmiennej środowiskowej zawierającej katalog aplikacji
ENV APPDIR=/home/app/webapp  

# stworzenie katatlogu aplikacji
RUN mkdir -p $APPDIR  

# przejście do katalogu aplikacji
WORKDIR $APPDIR 

# ustawienie zmiennych środowiskowych
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# instalacja zależności  
RUN pip install --upgrade pip && \
    apt update && \
    apt-get -y install curl

# skopiowanie plików projektu 
COPY /serwer-light/. $APPDIR

# instalacja wszystkich zależności  
RUN pip install -r requirements.txt

# oznaczenie wystawianego portu  
EXPOSE 8000  

# wystartowanie serwera  
CMD python mserwer/manage.py runserver 0.0.0.0:8000

HEALTHCHECK CMD curl --fail http://localhost:8000 || exit 1