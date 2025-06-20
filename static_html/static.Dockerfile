FROM python:3.13.4-slim-bullseye

WORKDIR /app
# RUN mkdir -p /static_folder 
# COPY ./static_html /static_folder


COPY ./src .
# RUN echo "hello" > index.html

# build
# docker build -f Dockerfile -t pyapp .
# run
# docker run -it pyapp


# docker build -f Dockerfile -t deathgod020/ai-py-app-test:latest .
# docker push deathgod020/ai-py-app-test:latest
# docker run -it -p 3000:8000 pyapp
CMD ["python", "-m", "http.server", "8000"]