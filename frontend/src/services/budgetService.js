import { createUserBudget } from './budgetApi';

// Function to create a budget and update the budget state
export const handleCreateBudget = async (username, setBudget, setSnackbarMessage, setSnackbarSeverity, setSnackbarOpen) => {
  try {
    const newBudget = await createUserBudget(username);  // Create a budget for the user
    setBudget(newBudget);  // Update the budget state
    setSnackbarMessage('Budget created successfully!');
    setSnackbarSeverity('success');
    setSnackbarOpen(true);  // Open the snackbar
  } catch (error) {
    setSnackbarMessage('Error creating budget');
    setSnackbarSeverity('error');
    setSnackbarOpen(true);  // Open the snackbar
    console.error('Error creating budget:', error);
  }
};
