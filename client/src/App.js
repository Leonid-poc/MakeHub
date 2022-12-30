import React from 'react';
import Info from './components/Info';
import Main from './components/Main';
import Navbar from './components/navbar/Navbar';
import Restouran from './components/Restouran';

const App = () => {
  return (
    <>
      <Navbar />    
      <Main />
      <Info />
      <Restouran />
    </>
  )
}

export default App