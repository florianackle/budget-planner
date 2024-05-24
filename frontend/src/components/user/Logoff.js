import React from 'react';
import { Button } from '@mui/material';
import { useNavigate } from 'react-router-dom';

function Logoff({ setIsAuthenticated }) {
  const navigate = useNavigate();

  const handleLogoff = () => {
    localStorage.removeItem('token'); // Token entfernen
    setIsAuthenticated(false); // Authentifizierungsstatus aktualisieren
    navigate('/login'); // Benutzer zur Login-Seite weiterleiten
  };

  return (
    <Button variant="contained" color="secondary" onClick={handleLogoff}>
      Abmelden
    </Button>
  );
}

export default Logoff;
