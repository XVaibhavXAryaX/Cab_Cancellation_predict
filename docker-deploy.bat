@echo off
REM Docker Deployment Script for Cab Cancellation Prediction (Windows)
REM Usage: docker-deploy.bat [build|run|stop|clean|logs]

setlocal enabledelayedexpansion

set IMAGE_NAME=cab-cancellation-predict
set CONTAINER_NAME=cab-cancellation-predict
set PORT=5000

echo 🚕 Cab Cancellation Prediction - Docker Deployment
echo ==================================================

if "%1"=="build" (
    echo 🔨 Building Docker image...
    docker build -t %IMAGE_NAME% .
    echo ✅ Image built successfully!
    goto :eof
)

if "%1"=="run" (
    echo 🚀 Running container...
    docker run -d --name %CONTAINER_NAME% -p %PORT%:5000 -v %cd%/artifacts:/app/artifacts -v %cd%/logs:/app/logs -v %cd%/images:/app/images --restart unless-stopped %IMAGE_NAME%
    echo ✅ Container started! Access at http://localhost:%PORT%
    goto :eof
)

if "%1"=="compose" (
    echo 🚀 Running with Docker Compose...
    docker-compose up -d
    echo ✅ Services started! Access at http://localhost:%PORT%
    goto :eof
)

if "%1"=="stop" (
    echo 🛑 Stopping container...
    docker stop %CONTAINER_NAME% 2>nul
    docker rm %CONTAINER_NAME% 2>nul
    echo ✅ Container stopped!
    goto :eof
)

if "%1"=="compose-stop" (
    echo 🛑 Stopping Docker Compose services...
    docker-compose down
    echo ✅ Services stopped!
    goto :eof
)

if "%1"=="clean" (
    echo 🧹 Cleaning up Docker resources...
    docker stop %CONTAINER_NAME% 2>nul
    docker rm %CONTAINER_NAME% 2>nul
    docker rmi %IMAGE_NAME% 2>nul
    docker system prune -f
    echo ✅ Cleanup completed!
    goto :eof
)

if "%1"=="logs" (
    echo 📋 Container logs:
    docker logs -f %CONTAINER_NAME%
    goto :eof
)

if "%1"=="compose-logs" (
    echo 📋 Docker Compose logs:
    docker-compose logs -f
    goto :eof
)

if "%1"=="status" (
    echo 📊 Container status:
    docker ps -a | findstr %CONTAINER_NAME% || echo Container not found
    goto :eof
)

if "%1"=="shell" (
    echo 🐚 Opening shell in container...
    docker exec -it %CONTAINER_NAME% /bin/bash
    goto :eof
)

if "%1"=="test" (
    echo 🧪 Testing the application...
    timeout /t 5 /nobreak >nul
    curl -f http://localhost:%PORT%/health || echo ❌ Health check failed
    echo ✅ Test completed!
    goto :eof
)

echo Usage: %0 {build^|run^|compose^|stop^|compose-stop^|clean^|logs^|compose-logs^|status^|shell^|test}
echo.
echo Commands:
echo   build        - Build Docker image
echo   run          - Run container with docker run
echo   compose      - Run with Docker Compose
echo   stop         - Stop container
echo   compose-stop - Stop Docker Compose services
echo   clean        - Clean up Docker resources
echo   logs         - Show container logs
echo   compose-logs - Show Docker Compose logs
echo   status       - Show container status
echo   shell        - Open shell in container
echo   test         - Test application health
echo.
echo Example workflow:
echo   %0 build
echo   %0 run
echo   %0 test
goto :eof 