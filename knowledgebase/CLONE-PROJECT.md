Clone the project

```bash
  git clone https://github.com/florianackle/budget-planner.git
```

### start database
Go to the root directory
```bash
  docker-compose up --build
```


### start backend
Go to the backend directory

```bash
  cd budget-planner\backend
```

Install dependencies

```bash
  poetry install
```

Start the server

```bash
  poetry run uvicorn app.main:app --reload
```

### start frontend
Go to the frontend directory

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
