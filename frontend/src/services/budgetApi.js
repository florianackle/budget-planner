import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

// Helper function to get JWT token
const getAuthHeader = () => {
  const token = localStorage.getItem('token');
  return token ? `Bearer ${token}` : '';
};

// Fetch user budget
export const getUserBudget = async (username) => {
  try {
    const response = await axios.get(`${API_URL}/budget?username=${username}`, {
      headers: { Authorization: getAuthHeader() },
    });
    return response.data;
  } catch (error) {
    console.error('Fehler beim Abrufen des Budgets:', error.response || error.message);
    throw error.response?.data?.detail || 'Fehler beim Abrufen des Budgets';
  }
};

// Create budget for user
export const createUserBudget = async (username) => {
  try {
    const response = await axios.post(`${API_URL}/budget?username=${username}`, {}, {
      headers: { Authorization: getAuthHeader() },
    });
    return response.data;
  } catch (error) {
    console.error('Fehler beim Erstellen des Budgets:', error.response || error.message);
    throw error.response?.data?.detail || 'Fehler beim Erstellen des Budgets';
  }
};

// Add income
export const addIncome = async (incomeData, username) => {
  try {
    const response = await axios.post(`${API_URL}/incomes?username=${username}`, incomeData, {
      headers: { Authorization: getAuthHeader() },
    });
    return response.data;
  } catch (error) {
    console.error('Fehler beim Hinzufügen der Einnahme:', error.response || error.message);
    throw error.response?.data?.detail || 'Fehler beim Hinzufügen der Einnahme';
  }
};

// Add expense
export const addExpense = async (expenseData, username) => {
  try {
    const response = await axios.post(`${API_URL}/expenses?username=${username}`, expenseData, {
      headers: { Authorization: getAuthHeader() },
    });
    return response.data;
  } catch (error) {
    console.error('Fehler beim Hinzufügen der Ausgabe:', error.response || error.message);
    throw error.response?.data?.detail || 'Fehler beim Hinzufügen der Ausgabe';
  }
};
