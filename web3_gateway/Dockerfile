FROM node:14-alpine

WORKDIR /src
COPY package.json /src
EXPOSE 3000

ENV NODE_ENV=production
RUN npm install
COPY . /src
CMD ["node", "app.js"]