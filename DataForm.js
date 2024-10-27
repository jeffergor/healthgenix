// src/DataForm.js

import React, { useState } from 'react';

function DataForm() {
  const [inputData, setInputData] = useState('');

  const handleChange = (event) => {
    setInputData(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`Datos ingresados: ${inputData}`);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Ingrese sus datos genéticos:
        <input type="text" value={inputData} onChange={handleChange} />
      </label>
      <button type="submit">Enviar</button>
    </form>
  );
}

export default DataForm;
