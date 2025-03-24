FROM node:18-slim

WORKDIR /app

COPY package*.json ./

RUN npm install --omit=dev

COPY . .

EXPOSE 8080

# Start the app with opentelemetry instrumentation
CMD ["node", "--require", "./instrumentation.js", "app.js"]
