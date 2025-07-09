FROM maven:3.8.4-openjdk-11 AS build
WORKDIR /app
COPY . .
RUN mvn clean package

FROM adoptopenjdk/openjdk11
EXPOSE 8080
ENV APP_HOME /usr/src/app
COPY --from=build /app/target/*.jar $APP_HOME/app.jar
WORKDIR $APP_HOME
ENTRYPOINT ["java","-jar","app.jar"]
