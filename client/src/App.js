import React from 'react';
import Info from './components/Info';
import Main from './components/Main';
import Navbar from './components/navbar/Navbar';

const App = () => {
  return (
    <>
      <Navbar />    
      <Main />
      <Info />
    </>
  )
}

export default App