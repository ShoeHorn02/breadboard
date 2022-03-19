# pull official base image
FROM node:14.18.1-alpine

# set working directory
WORKDIR /react

# add `/react/node_modules/.bin` to $PATH
ENV PATH /react/node_modules/.bin:$PATH

# install react dependencies
COPY package*.json /react
RUN npm install
COPY . /react
EXPOSE 3000
CMD ["npm", "start"]
