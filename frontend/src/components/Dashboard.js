import React, { useEffect, useState } from 'react';
import { Box, Typography, Paper } from '@mui/material';
import axios from 'axios';

const Dashboard = () => {
  const [budget, setBudget] = useState(0);
  const [error, setError] = useState('');

  const fetchBudget = async () => {
    try {
      // Abrufen der Einnahmen
      const incomeResponse = await axios.get('/incomes');
      const totalIncome = incomeResponse.data.reduce((sum, income) => sum + income.amount, 0);

      // Abrufen der Ausgaben
      const expenseResponse = await axios.get('/expenses');
      const totalExpense = expenseResponse.data.reduce((sum, expense) => sum + expense.amount, 0);

      // Berechnung des Budgets (Einnahmen - Ausgaben)
      setBudget(totalIncome - totalExpense);
    } catch (err) {
      setError('Fehler beim Abrufen der Budgetdaten');
    }
  };

  useEffect(() => {
    fetchBudget();
  }, []);

  return (
    <Box sx={{ padding: 4 }}>
      <Typography variant="h4" gutterBottom>
        Dein aktuelles Budget
      </Typography>
      {error ? (
        <Typography color="error">{error}</Typography>
      ) : (
        <Paper elevation={3} sx={{ padding: 2 }}>
          <Typography variant="h5">€ {budget}</Typography>
        </Paper>
      )}
    </Box>
  );
};

export default Dashboard;
