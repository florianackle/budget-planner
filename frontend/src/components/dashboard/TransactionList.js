import React from 'react';
import { Grid } from '@mui/material';
import Transaction from './Transaction';

function TransactionList() {
  const transactions = [
    { id: 1, date: '2023-05-23', description: 'Einnahme 1', category: 'Kategorie 1', type: 'income' },
    { id: 2, date: '2023-05-22', description: 'Ausgabe 1', category: 'Kategorie 2', type: 'expense' },
    { id: 3, date: '2023-05-21', description: 'Ausgabe 2', category: 'Kategorie 2', type: 'expense' },
    { id: 4, date: '2023-05-20', description: 'Ausgabe 3', category: 'Kategorie 3', type: 'expense' },
    { id: 5, date: '2023-05-19', description: 'Einnahme 2', category: 'Kategorie 1', type: 'income' },
  ]; // Beispielwerte, dies sollte von deinem Backend kommen.

  return (
    <Grid container spacing={2}>
      {transactions.map((transaction) => (
        <Grid item xs={12} key={transaction.id}>
          <Transaction transaction={transaction} />
        </Grid>
      ))}
    </Grid>
  );
}

export default TransactionList;
