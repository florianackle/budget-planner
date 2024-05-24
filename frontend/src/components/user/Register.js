import React, { useState } from 'react';
import { Button, Container, Typography, Grid } from '@mui/material';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import LogonFields from './LogonFields';
import Error from '../Error';

function Register() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleRegister = async () => {
    try {
      await axios.post('http://localhost:8000/users/', {
        username,
        password,
      });
      navigate('/login');
    } catch (error) {
      setError('Registration failed: ' + error.message);
    }
  };

  return (
    <Container>
      <Grid container spacing={3} justifyContent="center">
        <Grid item xs={12}>
          <Typography variant="h4" align="center">Register</Typography>
        </Grid>
        <Error message={error} />
        <LogonFields
          username={username}
          setUsername={setUsername}
          password={password}
          setPassword={setPassword}
        />
        <Grid item xs={12} md={6}>
          <Button onClick={handleRegister} variant="contained" color="primary" fullWidth>
            Register
          </Button>
        </Grid>
        <Grid item xs={12} md={6}>
          <Button onClick={() => navigate('/login')} color="secondary" fullWidth>
            Login
          </Button>
        </Grid>
      </Grid>
    </Container>
  );
}

export default Register;
