import './App.css';
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Display from './display.js';
import FirstPage from './FirstPage.js';

function App() {
    
    return (
      <Router>
        <Routes>
          <Route path='/' element={<FirstPage/>}/>
          <Route path='/second-page' element={<Display/>}/>
        </Routes>
      </Router>
    )
}

export default App;
