import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { registerUser } from '../services/api';
import { Grid, TextField, Button, Typography, Box } from '@mui/material';

function Register() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate();

  const handleRegister = async (e) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      setErrorMessage('Passwörter stimmen nicht überein');
      return;
    }
    try {
      await registerUser({ username, password });
      navigate('/');
    } catch (error) {
      setErrorMessage(error);
    }
  };

  const handleBackToLogin = () => {
    navigate('/');
  };

  return (
    <Box maxWidth="400px" mx="auto" my={5} p={3} border={1} borderRadius={2} borderColor="grey.400">
      <Typography variant="h4" component="h2" align="center" gutterBottom>
        Registrieren
      </Typography>
      {errorMessage && (
        <Typography color="error" align="center" gutterBottom>
          {errorMessage}
        </Typography>
      )}
      <form onSubmit={handleRegister}>
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
            <TextField
              label="Kennwort bestätigen"
              variant="outlined"
              fullWidth
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              required
            />
          </Grid>
          <Grid item xs={12}>
            <Button type="submit" variant="contained" color="primary" fullWidth>
              Konto erstellen
            </Button>
          </Grid>
          <Grid item xs={12}>
            <Button onClick={handleBackToLogin} variant="outlined" fullWidth>
              Zurück zum Login
            </Button>
          </Grid>
        </Grid>
      </form>
    </Box>
  );
}

export default Register;
