FROM node:10-alpine as angular
WORKDIR /app
COPY ./FrontEnd/medicar-front /app
# COPY package.json /app

RUN npm install --silent
CMD npm start

# CMD ng serve
# COPY . .
# RUN npm run build

# FROM nginx:alpine
# VOLUME /var/cache/nginx
# COPY --from=angular app/dist/requests-http /usr/share/nginx/html
# COPY ./config/nginx.conf /etc/nginx/conf.d/default.conf
