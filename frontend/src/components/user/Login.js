import React, { useState } from 'react';
import { Button, Container, Typography, Grid } from '@mui/material';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import LogonFields from './LogonFields';
import Error from '../Error';

function Login({ setIsAuthenticated }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const response = await axios.post('http://localhost:8000/token', {
        username,
        password,
      });
      localStorage.setItem('token', response.data.access_token);
      setIsAuthenticated(true); // Authentifizierungsstatus aktualisieren
      navigate('/dashboard'); // Benutzer zur Dashboard-Seite weiterleiten
    } catch (error) {
      setError('Login failed: Incorrect username or password');
    }
  };

  return (
    <Container>
      <Grid container spacing={3} justifyContent="center" style={{ marginTop: '20px' }}>
        <Grid item xs={12}>
          <Typography variant="h4" align="center">Login</Typography>
        </Grid>
        <Error message={error} />
        <LogonFields
          username={username}
          setUsername={setUsername}
          password={password}
          setPassword={setPassword}
        />
        <Grid item xs={12}>
          <Button onClick={handleLogin} variant="contained" color="primary" fullWidth style={{ marginTop: '16px' }}>
            Login
          </Button>
        </Grid>
        <Grid item xs={12}>
          <Button onClick={() => navigate('/register')} color="secondary" fullWidth style={{ marginTop: '16px' }}>
            Registrieren
          </Button>
        </Grid>
      </Grid>
    </Container>
  );
}

export default Login;
