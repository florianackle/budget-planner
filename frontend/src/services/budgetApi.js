import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

// Helper function to get JWT token
const getAuthHeader = () => {
  const token = localStorage.getItem('token');
  return token ? `Bearer ${token}` : '';
};

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
