import React from 'react';
import { Card, CardContent, Typography } from '@mui/material';

function BudgetDisplay() {
  const currentBudget = 100; // Beispielwert, dies sollte von deinem Backend oder Zustand kommen.
  const budgetColor = currentBudget >= 0 ? 'green' : 'red';

  return (
    <Card style={{ backgroundColor: budgetColor }}>
      <CardContent>
        <Typography variant="h5" align="center">
          Aktuelles Budget: {currentBudget}€
        </Typography>
      </CardContent>
    </Card>
  );
}

export default BudgetDisplay;
