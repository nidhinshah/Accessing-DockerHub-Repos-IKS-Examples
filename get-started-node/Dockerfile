FROM node:6-alpine

ADD views /app/views
ADD package.json /app
ADD server.js /app

RUN cd /app; npm install

EXPOSE 3000

WORKDIR "/app"
CMD [ "npm", "start" ]
