# Build stage
FROM eclipse-temurin:17-jdk AS builder
WORKDIR /workspace/app

# Copy Maven wrapper and dependencies first (cache optimization)
COPY mvnw .
COPY .mvn .mvn
COPY pom.xml .
RUN ./mvnw dependency:go-offline

# Copy source code and build
COPY src src
RUN ./mvnw package -DskipTests

# Runtime stage
FROM eclipse-temurin:17-jre
WORKDIR /app

# Copy built artifact from builder stage
COPY --from=builder /workspace/app/target/*.jar app.jar

# Expose application port
EXPOSE 8080

# Run the application
ENTRYPOINT ["java", "-jar", "app.jar"]
