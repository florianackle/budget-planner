import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

// Helper function to get JWT token
const getAuthHeader = () => {
  const token = localStorage.getItem('token');
  return token ? `Bearer ${token}` : '';
};

// Fetch all incomes for the current user
export const getIncomes = async (username) => {
  try {
    const response = await axios.get(`${API_URL}/incomes?username=${username}`, {
      headers: { Authorization: getAuthHeader() },
    });
    return response.data.map(income => ({ ...income, isIncome: true })); // Set isIncome property for filtering
  } catch (error) {
    console.error('Fehler beim Abrufen der Einnahmen:', error.response || error.message);
    throw error.response?.data?.detail || 'Fehler beim Abrufen der Einnahmen';
  }
};

// Fetch all expenses for the current user
export const getExpenses = async (username) => {
  try {
    const response = await axios.get(`${API_URL}/expenses?username=${username}`, {
      headers: { Authorization: getAuthHeader() },
    });
    return response.data.map(expense => ({ ...expense, isIncome: false })); // Set isIncome property for filtering
  } catch (error) {
    console.error('Fehler beim Abrufen der Ausgaben:', error.response || error.message);
    throw error.response?.data?.detail || 'Fehler beim Abrufen der Ausgaben';
  }
};
