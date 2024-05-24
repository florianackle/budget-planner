import React from 'react';
import { Card, CardContent, Grid, Typography } from '@mui/material';

function Transaction({ transaction }) {
  const { date, description, category, type } = transaction;
  const transactionColor = type === 'income' ? 'lightgreen' : 'lightcoral';

  return (
    <Card style={{ backgroundColor: transactionColor }}>
      <CardContent>
        <Grid container spacing={2}>
          <Grid item xs={3}>
            <Typography variant="body1">{date}</Typography>
          </Grid>
          <Grid item xs={6}>
            <Typography variant="body1">{description}</Typography>
          </Grid>
          <Grid item xs={3}>
            <Typography variant="body1">{category}</Typography>
          </Grid>
        </Grid>
      </CardContent>
    </Card>
  );
}

export default Transaction;
