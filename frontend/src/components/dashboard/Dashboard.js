import React from 'react';
import { Container, Grid } from '@mui/material';
import BudgetDisplay from './BudgetDisplay';
import TransactionList from './TransactionList';
import AddTransactionButton from './AddTransactionButton';
import Logoff from '../user/Logoff';

function Dashboard({ setIsAuthenticated }) {
  return (
    <Container>
      <Grid container spacing={3} justifyContent="space-between" alignItems="center">
        <Grid item xs={9}>
          <BudgetDisplay />
        </Grid>
        <Grid item>
          <Logoff setIsAuthenticated={setIsAuthenticated} />
        </Grid>
      </Grid>
      <Grid container spacing={3} justifyContent="center">
        <Grid item xs={12}>
          <AddTransactionButton />
        </Grid>
        <Grid item xs={12}>
          <TransactionList />
        </Grid>
      </Grid>
    </Container>
  );
}

export default Dashboard;
