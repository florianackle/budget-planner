import React, { useState, useEffect } from 'react';
import { Button, Dialog, DialogActions, DialogContent, DialogTitle, Switch, TextField, MenuItem, Box } from '@mui/material';
import { getCategories } from '../services/categoryService';
import { addIncome, addExpense, getUserBudget } from '../services/budgetApi';

const AddIncomeExpense = ({ open, handleClose, handleSubmit }) => {
  const [isIncome, setIsIncome] = useState(true);
  const [description, setDescription] = useState('');
  const [amount, setAmount] = useState('');
  const [category, setCategory] = useState('');
  const [categories, setCategories] = useState([]);
  const [error, setError] = useState({ description: false, amount: false }); // Error state for validation

  // Get categories from backend
  useEffect(() => {
    const fetchCategories = async () => {
      const data = await getCategories();
      setCategories(data);
      if (data.length > 0) {
        setCategory(data[0].id); // set default category
      }
    };
    fetchCategories();
  }, []);

  // Reset form fields after submission or closing dialog
  const resetForm = () => {
    setIsIncome(true);
    setDescription('');
    setAmount('');
    if (categories.length > 0) {
      setCategory(categories[0].id);  // Reset to the default category
    }
    setError({ description: false, amount: false });  // Reset error state
  };

  // Validate form before submitting
  const validateForm = () => {
    let isValid = true;

    if (!description) {
      setError((prev) => ({ ...prev, description: true }));
      isValid = false;
    }

    if (!amount || isNaN(amount) || parseFloat(amount) <= 0) {
      setError((prev) => ({ ...prev, amount: true }));
      isValid = false;
    }

    return isValid;
  };

  const onSubmit = async () => {
    if (!validateForm()) {
      return;  // Stop if validation fails
    }

    const username = localStorage.getItem('username');  // Get username from local storage

    console.log("Username retrieved from localStorage: ", username);  // Debugging

    if (!username) {
      console.error("User ist möglicherweise nicht eingeloggt.");
      return;
    }

    try {
      const budget = await getUserBudget(username);  // Fetch budget to get the budget_id
      const data = {
        description,
        amount,
        category_id: category,
        budget_id: budget.id  // Add budget_id to the request data
      };

      if (isIncome) {
        await addIncome(data, username);  // Pass username to addIncome
      } else {
        await addExpense(data, username);  // Pass username to addExpense
      }

      handleSubmit(data);  // Handle success after API call
      resetForm();  // Reset form fields after submission
      handleClose();  // Close the dialog
    } catch (error) {
      console.error("Fehler beim Hinzufügen der Einnahme/Ausgabe:", error);
    }
  };

  // When the dialog is closed, reset the form fields
  const handleDialogClose = () => {
    resetForm();  // Reset form fields when closing
    handleClose();  // Close the dialog
  };

  return (
    <Dialog open={open} onClose={handleDialogClose}>
      <DialogTitle>Neue Einnahme/Ausgabe hinzufügen</DialogTitle>
      <DialogContent>
        <Box display="flex" alignItems="center" mb={2}>
          <Switch
            checked={isIncome}
            onChange={() => setIsIncome(!isIncome)}
            name="incomeExpenseSwitch"
            color="primary"
          />
          <label>{isIncome ? 'Einnahme' : 'Ausgabe'}</label>
        </Box>

        <Box mb={2}>
          <TextField
            autoFocus
            label="Beschreibung"
            type="text"
            fullWidth
            value={description}
            onChange={(e) => {
              setDescription(e.target.value);
              setError((prev) => ({ ...prev, description: false }));  // Clear error
            }}
            error={error.description}
            helperText={error.description ? 'Beschreibung ist erforderlich' : ''}
          />
        </Box>

        <Box mb={2}>
          <TextField
            label="Betrag"
            type="number"
            fullWidth
            value={amount}
            onChange={(e) => {
              setAmount(e.target.value);
              setError((prev) => ({ ...prev, amount: false }));  // Clear error
            }}
            error={error.amount}
            helperText={error.amount ? 'Betrag muss grösser als 0 sein' : ''}
          />
        </Box>

        <Box mb={2}>
          <TextField
            select
            label="Kategorie"
            value={category}
            onChange={(e) => setCategory(e.target.value)}
            fullWidth
          >
            {categories.map((option) => (
              <MenuItem key={option.id} value={option.id}>
                {option.name}
              </MenuItem>
            ))}
          </TextField>
        </Box>
      </DialogContent>
      <DialogActions>
        <Button onClick={handleDialogClose} color="secondary">
          Abbrechen
        </Button>
        <Button onClick={onSubmit} color="primary">
          Hinzufügen
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default AddIncomeExpense;
