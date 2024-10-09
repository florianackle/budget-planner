Clone the project

```bash
  git clone https://github.com/florianackle/budget-planner.git
```

### start database
Go to the root directory an rund
```bash
  docker-compose up --build
```


### start backend
Go to the backend directory (/backend)

```bash
  cd budget-planner\backend
```

Install dependencies

```bash
  poetry install
```

Create .env file

```bash
  cp .venv .env
```

Start the server

```bash
  poetry run uvicorn app.main:app --reload
```

### start frontend
Go to the frontend directory (/frontend)

```bash
  cd budget-planner\frontend
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm start
```

### usage:

After running the commands above you can connect to the front- and backend
- Frontend: http://localhost:3000
- Backend: http://localhost:8000/docs
