import React, { useState, useEffect } from 'react';
import { Button, Typography, CircularProgress, Paper, Grid, Box } from '@mui/material';
import { getUserBudget } from '../services/budgetApi';
import { handleCreateBudget } from '../services/budgetService';  // Import the external function
import CustomSnackbar from './CustomSnackbar';  // Import the snackbar component
import AddIncomeExpense from './AddIncomeExpense'; // Import the AddIncomeExpense component
import IncomeExpenseTable from './IncomeExpenseTable'; // Import the table component

const Dashboard = () => {
  const [budget, setBudget] = useState(null);
  const [loading, setLoading] = useState(true);
  const [username] = useState(localStorage.getItem('username'));
  const [snackbarOpen, setSnackbarOpen] = useState(false);  // State for Snackbar open/close
  const [snackbarMessage, setSnackbarMessage] = useState('');  // Message to show in Snackbar
  const [snackbarSeverity, setSnackbarSeverity] = useState('success');  // Snackbar type (success, error, etc.)
  const [dialogOpen, setDialogOpen] = useState(false);  // State for opening AddIncomeExpense dialog
  const [tableKey, setTableKey] = useState(0);  // State to force refresh of the table

  // Fetch the user's budget
  useEffect(() => {
    const fetchBudget = async () => {
      try {
        const response = await getUserBudget(username);
        setBudget(response);  // Set the fetched budget
      } catch (error) {
        console.error('Error fetching budget:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchBudget();
  }, [username]);

  // Handler for opening the AddIncomeExpense dialog
  const handleDialogOpen = () => {
    setDialogOpen(true);
  };

  // Handler for closing the AddIncomeExpense dialog
  const handleDialogClose = () => {
    setDialogOpen(false);
  };

  // Handler for refreshing the table
  const refreshTable = () => {
    setTableKey(prevKey => prevKey + 1); // Increment the key to force table reload
  };

  // Handler for submitting new income or expense
  const handleAddIncomeExpense = async (data) => {
    setSnackbarMessage('Einnahme/Ausgabe erfolgreich hinzugefügt!');
    setSnackbarSeverity('success');
    setSnackbarOpen(true);

    // Reload the budget after adding a new income/expense
    const fetchBudget = async () => {
      try {
        const response = await getUserBudget(username);
        setBudget(response);  // Update the budget with the new value
      } catch (error) {
        console.error('Error fetching updated budget:', error);
      }
    };

    await fetchBudget();  // Fetch updated budget after submission
    refreshTable(); // Refresh the table after adding income/expense
    handleDialogClose();
  };

  if (loading) {
    return (
      <Grid container justifyContent="center" alignItems="center" style={{ minHeight: '100vh' }}>
        <CircularProgress />
      </Grid>
    );
  }

  return (
    <Grid container justifyContent="center" alignItems="center" style={{ minHeight: '100vh' }}>
      <Grid item xs={12} md={6} lg={4}>
        {budget ? (
          <>
            {/* User has a budget */}
            <Typography variant="h4" component="h2" gutterBottom align="center">
              Dein aktuelles Budget
            </Typography>
            <Paper elevation={3} sx={{ padding: 2 }}>
              <Box display="flex" justifyContent="space-between" alignItems="center">
                <Typography variant="h5" align="center">CHF {budget.total_amount}</Typography>
                <Button
                  variant="contained"
                  color="primary"
                  onClick={handleDialogOpen}
                  style={{ marginLeft: '10px' }}
                >
                  Neue Einnahme/Ausgabe
                </Button>
              </Box>
            </Paper>

            {/* Table for incomes and expenses */}
            <Box mt={3}>
              <IncomeExpenseTable key={tableKey} /> {/* Add key to refresh the table */}
            </Box>

          </>
        ) : (
          <>
            {/* User has no budget */}
            <Typography variant="h2" component="h2" gutterBottom align="center">
              Hi {username}! 💖
            </Typography>
            <Typography variant="h5" component="h5" gutterBottom align="center">
              Willkommen beim besten Budget-Planner der HF-ICT
            </Typography>
            <Grid container justifyContent="center">
              <Button
                variant="contained"
                color="primary"
                onClick={() => handleCreateBudget(username, setBudget, setSnackbarMessage, setSnackbarSeverity, setSnackbarOpen)}
              >
                Budget erstellen
              </Button>
            </Grid>
          </>
        )}
        {/* AddIncomeExpense dialog */}
        <AddIncomeExpense
          open={dialogOpen}
          handleClose={handleDialogClose}
          handleSubmit={handleAddIncomeExpense}
          refreshTable={refreshTable} // Pass refreshTable to refresh the table
        />
        {/* Snackbar for feedback */}
        <CustomSnackbar
          open={snackbarOpen}
          message={snackbarMessage}
          severity={snackbarSeverity}
          onClose={() => setSnackbarOpen(false)}
        />
      </Grid>
    </Grid>
  );
};

export default Dashboard;
