import React, { useState, useEffect } from 'react';
import { Button, Dialog, DialogActions, DialogContent, DialogTitle, Switch, TextField, MenuItem, Box } from '@mui/material';
import { getCategories } from '../services/categoryService';

const AddIncomeExpense = ({ open, handleClose, handleSubmit }) => {
  const [isIncome, setIsIncome] = useState(true);
  const [description, setDescription] = useState('');
  const [amount, setAmount] = useState(0);
  const [category, setCategory] = useState('');
  const [categories, setCategories] = useState([]);

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
    setAmount(0);
    if (categories.length > 0) {
      setCategory(categories[0].id);  // Reset to the default category
    }
  };

  const onSubmit = () => {
    handleSubmit({ isIncome, description, amount, category });
    resetForm();  // Reset form fields after submission
    handleClose();  // Close the dialog
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
            onChange={(e) => setDescription(e.target.value)}
          />
        </Box>

        <Box mb={2}>
          <TextField
            label="Betrag"
            type="number"
            fullWidth
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
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
