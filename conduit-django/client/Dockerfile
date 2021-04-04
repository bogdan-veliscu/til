# base image
FROM node:12-alpine

WORKDIR /code

ENV PATH /code/node_modules/.bin:$PATH

COPY package*.json ./

COPY . ./

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint
RUN chmod +x /usr/local/bin/docker-entrypoint

ENTRYPOINT ["docker-entrypoint"]

CMD ["npm", "start"]
