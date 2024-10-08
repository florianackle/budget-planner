import React, { useState, useEffect } from 'react';
import { Button, Typography, CircularProgress, Paper, Grid } from '@mui/material';
import { getUserBudget } from '../services/budgetApi';
import { handleCreateBudget } from '../services/budgetService';  // Import the external function
import CustomSnackbar from './CustomSnackbar';  // Import the snackbar component

const Dashboard = () => {
  const [budget, setBudget] = useState(null);
  const [loading, setLoading] = useState(true);
  const [username, setUsername] = useState(localStorage.getItem('username'));
  const [snackbarOpen, setSnackbarOpen] = useState(false);  // State for Snackbar open/close
  const [snackbarMessage, setSnackbarMessage] = useState('');  // Message to show in Snackbar
  const [snackbarSeverity, setSnackbarSeverity] = useState('success');  // Snackbar type (success, error, etc.)

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
            <Typography variant="h4" component="h2" gutterBottom align="center">
              dein aktuelles Budget
            </Typography>
            <Paper elevation={3} sx={{ padding: 2 }}>
              <Typography variant="h5" align="center">CHF {budget.total_amount}</Typography>
            </Paper>
          </>
        ) : (
          <>
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
                Get Started
              </Button>
            </Grid>
          </>
        )}
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
