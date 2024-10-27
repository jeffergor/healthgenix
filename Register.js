// src/Register.js

import React, { useState } from 'react';
import { auth } from './firebase';
import { createUserWithEmailAndPassword } from 'firebase/auth';

function Register() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      await createUserWithEmailAndPassword(auth, email, password);
      alert('Registro exitoso');
    } catch (error) {
      console.error("Error en el registro:", error);
      alert('Error en el registro');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Correo Electrónico:
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
      </label>
      <label>
        Contraseña:
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
      </label>
      <button type="submit">Registrarse</button>
    </form>
  );
}

export default Register;
// src/App.js

import Register from './Register';

function App() {
  return (
    <div className="App">
      {/* ... */}
      <section id="about">
        <h2>Registro de Usuario</h2>
        <Register />
      </section>
      {/* ... */}
    </div>
  );
}
