# Backend Health Service

A small Python backend service built with Flask. It includes a home route, a health-check endpoint, and environment-based configuration.

## Features

- `GET /` — returns a welcome message.
- `GET /health` — returns the service health and active environment.
- Configuration through environment variables and a local `.env` file.
- Simple application factory (`create_app`) for easier extension and testing.

## Requirements

- Python 3.9 or newer
- pip

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/backend-health-service.git
   cd backend-health-service
   ```

2. Create and activate a virtual environment:

   **Windows (PowerShell):**
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   **macOS / Linux:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create your local environment file:

   **Windows (PowerShell):**
   ```powershell
   Copy-Item .env.example .env
   ```

   **macOS / Linux:**
   ```bash
   cp .env.example .env
   ```

5. Start the server:

   ```bash
   python app.py
   ```

   The API runs at `http://127.0.0.1:5000` by default.

## API endpoints

### `GET /`

Example response:

```json
{
  "message": "Welcome to Backend Health Service",
  "status": "running"
}
```

### `GET /health`

Example response:

```json
{
  "status": "healthy",
  "service": "Backend Health Service",
  "environment": "development"
}
```

A successful health check returns HTTP status code `200`.

## Environment variables

| Variable | Default | Description |
|---|---|---|
| `APP_NAME` | `Backend Health Service` | Name returned by the API |
| `APP_ENV` | `development` | Environment label |
| `HOST` | `127.0.0.1` | Host interface for the local server |
| `PORT` | `5000` | Server port |
| `FLASK_DEBUG` | `false` | Enables Flask debug mode when set to `true` |

Copy `.env.example` to `.env` and change values as needed. Do not commit `.env` because it may contain secrets.

## Quick test

With the server running, open these URLs in your browser:

- http://127.0.0.1:5000/
- http://127.0.0.1:5000/health

Or use curl:

```bash
curl http://127.0.0.1:5000/health
```

## License

This project is available under the MIT License.
