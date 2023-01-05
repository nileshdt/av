# userService/Dockerfile

FROM node:15

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

EXPOSE 50054
CMD [ "node", "index.js" ]