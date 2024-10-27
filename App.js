// src/App.js

import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Plataforma de Detección de Cáncer y Edición Genética</h1>
        <nav>
          <ul>
            <li><a href="#home">Inicio</a></li>
            <li><a href="#detect">Detección de Cáncer</a></li>
            <li><a href="#crispr">Edición Genética</a></li>
            <li><a href="#about">Acerca de</a></li>
          </ul>
        </nav>
      </header>
      <main>
        <section id="home">
          <h2>Bienvenido a nuestra Plataforma</h2>
          <p>Estamos comprometidos con la investigación y el desarrollo en la detección de cáncer y edición genética.</p>
        </section>
        <section id="detect">
          <h2>Detección de Cáncer</h2>
          <p>Aquí podrás realizar análisis de datos genéticos.</p>
        </section>
        <section id="crispr">
          <h2>Edición Genética CRISPR</h2>
          <p>Explora las posibilidades de la edición genética.</p>
        </section>
        <section id="about">
          <h2>Acerca de</h2>
          <p>Información sobre el equipo y nuestra misión.</p>
        </section>
      </main>
    </div>
  );
}

export default App;
// src/App.js

import DataForm from './DataForm';

function App() {
  return (
    <div className="App">
      {/* ... */}
      <section id="detect">
        <h2>Detección de Cáncer</h2>
        <p>Aquí podrás realizar análisis de datos genéticos.</p>
        <DataForm />
      </section>
      {/* ... */}
    </div>
  );
}
