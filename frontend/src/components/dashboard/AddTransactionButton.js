import React from 'react';
import { Button } from '@mui/material';

function AddTransactionButton() {
  const handleAddTransaction = () => {
    // Logik zum Hinzufügen einer Transaktion
    console.log('Transaktion hinzufügen');
  };

  return (
    <Button variant="contained" color="primary" onClick={handleAddTransaction} style={{ float: 'right', margin: '20px 0' }}>
      Transaktion hinzufügen
    </Button>
  );
}

export default AddTransactionButton;
