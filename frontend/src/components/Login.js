import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { loginUser } from '../services/authApi';
import { Grid, TextField, Button, Typography, Box } from '@mui/material';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const userData = await loginUser({ username, password });
      // Save JWT-Token and Username in LocalStorage
      localStorage.setItem('token', userData.access_token);
      localStorage.setItem('username', username);
      navigate('/dashboard');
    } catch (error) {
      setErrorMessage(error);
    }
  };

  const handleRegister = () => {
    navigate('/register');
  };

  return (
    <Box maxWidth="400px" mx="auto" my={5} p={3} border={1} borderRadius={2} borderColor="grey.400">
      <Typography variant="h4" component="h2" align="center" gutterBottom>
        Login
      </Typography>
      {errorMessage && (
        <Typography color="error" align="center" gutterBottom>
          {errorMessage}
        </Typography>
      )}
      <form onSubmit={handleLogin}>
        <Grid container spacing={2}>
          <Grid item xs={12}>
            <TextField
              label="Benutzername"
              variant="outlined"
              fullWidth
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </Grid>
          <Grid item xs={12}>
            <TextField
              label="Kennwort"
              variant="outlined"
              fullWidth
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </Grid>
          <Grid item xs={12}>
            <Button type="submit" variant="contained" color="primary" fullWidth>
              Login
            </Button>
          </Grid>
          <Grid item xs={12}>
            <Button onClick={handleRegister} variant="outlined" fullWidth>
              Registrieren
            </Button>
          </Grid>
        </Grid>
      </form>
    </Box>
  );
}

export default Login;
