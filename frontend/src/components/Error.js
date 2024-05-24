import React from 'react';
import { Alert, Grid } from '@mui/material';

function Error({ message }) {
  if (!message) return null;

  return (
    <Grid item xs={12}>
      <Alert severity="error" style={{ marginBottom: '16px' }}>
        {message}
      </Alert>
    </Grid>
  );
}

export default Error;
