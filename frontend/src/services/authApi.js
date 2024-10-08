import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export const registerUser = async (user) => {
  try {
    const response = await axios.post(`${API_URL}/users/`, user);
    return response.data;
  } catch (error) {
    throw error.response?.data?.detail || 'Registrierung fehlgeschlagen';
  }
};

export const loginUser = async (user) => {
  try {
    const response = await axios.post(`${API_URL}/users/login`, user);
    return response.data;
  } catch (error) {
    throw error.response?.data?.detail || 'Login fehlgeschlagen';
  }
};