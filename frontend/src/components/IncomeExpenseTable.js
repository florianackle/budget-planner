import React, { useState, useEffect } from 'react';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Chip, Select, MenuItem, FormControl, InputLabel, Box } from '@mui/material';
import { makeStyles } from '@mui/styles'; // Import makeStyles
import { getIncomes, getExpenses } from '../services/incomeExpenseApi'; // API calls for fetching income/expenses
import { getCategories } from '../services/categoryService'; // API call for fetching categories

// Define custom styles using makeStyles
const useStyles = makeStyles((theme) => ({
  tableHeader: {
    fontWeight: 'bold',
    backgroundColor: '#f5f5f5',
  },
  incomeRow: {
    backgroundColor: '#e0fae4',
  },
  expenseRow: {
    backgroundColor: '#ffebee',
  },
}));

const IncomeExpenseTable = () => {
  const classes = useStyles(); // Use custom styles
  const [incomes, setIncomes] = useState([]);
  const [expenses, setExpenses] = useState([]);
  const [filteredData, setFilteredData] = useState([]);
  const [categories, setCategories] = useState([]);
  const [filterType, setFilterType] = useState('all'); // Filter: all, incomes, expenses
  const [filterCategory, setFilterCategory] = useState('all'); // Filter by category

  useEffect(() => {
    const fetchData = async () => {
      const username = localStorage.getItem('username');
      const fetchedIncomes = await getIncomes(username);
      const fetchedExpenses = await getExpenses(username);
      const fetchedCategories = await getCategories();

      // Add isIncome property to the fetched expenses
      const expensesWithFlag = fetchedExpenses.map(expense => ({
        ...expense,
        isIncome: false // Set isIncome to false for expenses
      }));

      setIncomes(fetchedIncomes);
      setExpenses(expensesWithFlag); // Set the updated expenses
      setCategories(fetchedCategories);
      setFilteredData([...fetchedIncomes, ...expensesWithFlag]); // Initially show all data
    };
    fetchData();
  }, []);

  // Handle filter changes
  useEffect(() => {
    let data = [];

    if (filterType === 'incomes') {
      data = incomes;
    } else if (filterType === 'expenses') {
      data = expenses;
    } else {
      data = [...incomes, ...expenses];
    }

    if (filterCategory !== 'all') {
      data = data.filter(item => item.category_id === filterCategory);
    }

    // Sort by created_at (newest first)
    data.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
    setFilteredData(data);
  }, [filterType, filterCategory, incomes, expenses]);

  return (
    <Box p={2}>
      <Box display="flex" justifyContent="space-between" mb={2}>
        {/* Filter by type (All, Incomes, Expenses) */}
        <FormControl variant="outlined">
          <InputLabel>Typ</InputLabel>
          <Select
            value={filterType}
            onChange={(e) => setFilterType(e.target.value)}
            label="Typ"
          >
            <MenuItem value="all">Alle</MenuItem>
            <MenuItem value="incomes">Einnahmen</MenuItem>
            <MenuItem value="expenses">Ausgaben</MenuItem>
          </Select>
        </FormControl>

        {/* Filter by category */}
        <FormControl variant="outlined">
          <InputLabel>Kategorie</InputLabel>
          <Select
            value={filterCategory}
            onChange={(e) => setFilterCategory(e.target.value)}
            label="Kategorie"
          >
            <MenuItem value="all">Alle Kategorien</MenuItem>
            {categories.map((category) => (
              <MenuItem key={category.id} value={category.id}>
                {category.name}
              </MenuItem>
            ))}
          </Select>
        </FormControl>
      </Box>

      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell className={classes.tableHeader}>Beschreibung</TableCell>
              <TableCell className={classes.tableHeader}>Betrag</TableCell>
              <TableCell className={classes.tableHeader}>Datum</TableCell>
              <TableCell className={classes.tableHeader}>Kategorie</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {filteredData.map((row) => (
              <TableRow
                key={row.id}
                className={row.isIncome ? classes.incomeRow : classes.expenseRow} // Use conditional classes
              >
                <TableCell>{row.description}</TableCell>
                <TableCell>{row.amount}</TableCell>
                <TableCell>
                  {new Date(row.created_at).toLocaleDateString('de-DE', {
                    day: '2-digit',
                    month: '2-digit',
                    year: 'numeric',
                  })}
                </TableCell>
                <TableCell>
                  <Chip
                    label={categories.find((cat) => cat.id === row.category_id)?.name || 'Unbekannt'}
                    color="primary"
                  />
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
};

export default IncomeExpenseTable;
