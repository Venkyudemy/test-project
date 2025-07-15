# Build stage
FROM eclipse-temurin:17-jdk AS builder
WORKDIR /workspace/app

# Copy only necessary build files first (cache optimization)
COPY pom.xml .
COPY mvnw* ./
COPY .mvn/ .mvn/

# Install dependencies
RUN ./mvnw dependency:go-offline -B

# Copy source code
COPY src src

# Build application
RUN ./mvnw package -DskipTests

# Runtime stage
FROM eclipse-temurin:17-jre
WORKDIR /app

# Copy built artifact
COPY --from=builder /workspace/app/target/*.jar app.jar

# Expose application port
EXPOSE 8080

# Run the application
ENTRYPOINT ["java", "-jar", "app.jar"]
