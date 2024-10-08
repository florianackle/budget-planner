import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

// Hilfsfunktion, um das JWT-Token zu holen
const getAuthHeader = () => {
  const token = localStorage.getItem('token');
  return token ? `Bearer ${token}` : '';
};

// Budget des Benutzers abfragen mit JWT
export const getUserBudget = async () => {
  try {
    const response = await axios.get(`${API_URL}/budget`, {
      headers: { Authorization: getAuthHeader() },
    });
    return response.data;
  } catch (error) {
    console.error('Fehler beim Abrufen des Budgets:', error.response || error.message);
    throw error.response?.data?.detail || 'Fehler beim Abrufen des Budgets';
  }
};

// Budget für den Benutzer erstellen mit JWT
export const createUserBudget = async () => {
  try {
    const response = await axios.post(`${API_URL}/budget`, {}, {
      headers: { Authorization: getAuthHeader() },
    });
    return response.data;
  } catch (error) {
    console.error('Fehler beim Erstellen des Budgets:', error.response || error.message);
    throw error.response?.data?.detail || 'Fehler beim Erstellen des Budgets';
  }
};
