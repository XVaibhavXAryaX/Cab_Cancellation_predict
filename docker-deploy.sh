#!/bin/bash

# Docker Deployment Script for Cab Cancellation Prediction
# Usage: ./docker-deploy.sh [build|run|stop|clean|logs]

set -e

IMAGE_NAME="cab-cancellation-predict"
CONTAINER_NAME="cab-cancellation-predict"
PORT="5000"

echo "🚕 Cab Cancellation Prediction - Docker Deployment"
echo "=================================================="

case "$1" in
    "build")
        echo "🔨 Building Docker image..."
        docker build -t $IMAGE_NAME .
        echo "✅ Image built successfully!"
        ;;
    
    "run")
        echo "🚀 Running container..."
        docker run -d \
            --name $CONTAINER_NAME \
            -p $PORT:5000 \
            -v $(pwd)/artifacts:/app/artifacts \
            -v $(pwd)/logs:/app/logs \
            -v $(pwd)/images:/app/images \
            --restart unless-stopped \
            $IMAGE_NAME
        echo "✅ Container started! Access at http://localhost:$PORT"
        ;;
    
    "compose")
        echo "🚀 Running with Docker Compose..."
        docker-compose up -d
        echo "✅ Services started! Access at http://localhost:$PORT"
        ;;
    
    "stop")
        echo "🛑 Stopping container..."
        docker stop $CONTAINER_NAME || true
        docker rm $CONTAINER_NAME || true
        echo "✅ Container stopped!"
        ;;
    
    "compose-stop")
        echo "🛑 Stopping Docker Compose services..."
        docker-compose down
        echo "✅ Services stopped!"
        ;;
    
    "clean")
        echo "🧹 Cleaning up Docker resources..."
        docker stop $CONTAINER_NAME || true
        docker rm $CONTAINER_NAME || true
        docker rmi $IMAGE_NAME || true
        docker system prune -f
        echo "✅ Cleanup completed!"
        ;;
    
    "logs")
        echo "📋 Container logs:"
        docker logs -f $CONTAINER_NAME
        ;;
    
    "compose-logs")
        echo "📋 Docker Compose logs:"
        docker-compose logs -f
        ;;
    
    "status")
        echo "📊 Container status:"
        docker ps -a | grep $CONTAINER_NAME || echo "Container not found"
        ;;
    
    "shell")
        echo "🐚 Opening shell in container..."
        docker exec -it $CONTAINER_NAME /bin/bash
        ;;
    
    "test")
        echo "🧪 Testing the application..."
        sleep 5
        curl -f http://localhost:$PORT/health || echo "❌ Health check failed"
        echo "✅ Test completed!"
        ;;
    
    *)
        echo "Usage: $0 {build|run|compose|stop|compose-stop|clean|logs|compose-logs|status|shell|test}"
        echo ""
        echo "Commands:"
        echo "  build        - Build Docker image"
        echo "  run          - Run container with docker run"
        echo "  compose      - Run with Docker Compose"
        echo "  stop         - Stop container"
        echo "  compose-stop - Stop Docker Compose services"
        echo "  clean        - Clean up Docker resources"
        echo "  logs         - Show container logs"
        echo "  compose-logs - Show Docker Compose logs"
        echo "  status       - Show container status"
        echo "  shell        - Open shell in container"
        echo "  test         - Test application health"
        echo ""
        echo "Example workflow:"
        echo "  ./docker-deploy.sh build"
        echo "  ./docker-deploy.sh run"
        echo "  ./docker-deploy.sh test"
        exit 1
        ;;
esac 