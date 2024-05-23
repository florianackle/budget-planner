import React from 'react';
import { AppBar, Toolbar, Typography, Container } from '@mui/material';

function App() {
  return (
    <div>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6">
            Budget Planner
          </Typography>
        </Toolbar>
      </AppBar>
      <Container>
        <Typography variant="h4" style={{ marginTop: '20px' }}>
          Welcome to the Budget Planner!
        </Typography>
      </Container>
    </div>
  );
}

export default App;