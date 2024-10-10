import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

// Helper function to get JWT token
const getAuthHeader = () => {
  const token = localStorage.getItem('token');
  return token ? `Bearer ${token}` : '';
};

export const getCategories = async () => {
  try {
    const response = await axios.get(`${API_URL}/categories`, {
      headers: { Authorization: getAuthHeader() },
    });
    return response.data;
  } catch (error) {
    console.error('Fehler beim Abrufen der Kategorien:', error.response || error.message);
    throw error.response?.data?.detail || 'Fehler beim Abrufen der Kategorien';
  }
};
