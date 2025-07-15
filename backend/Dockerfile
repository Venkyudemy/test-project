# Build stage
FROM maven:3.9.10-eclipse-temurin-21 AS builder
WORKDIR /app
COPY . .

# Fix file name to match class name
RUN mv src/main/java/priacc/com/backend/BackendChatbot.java \
       src/main/java/priacc/com/backend/BackendApplication.java

RUN mvn clean package -DskipTests

# Runtime stage
FROM eclipse-temurin:21-jre-alpine
RUN addgroup -S spring && adduser -S spring -G spring
USER spring:spring
WORKDIR /app
COPY --from=builder /app/target/*.jar ./app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
