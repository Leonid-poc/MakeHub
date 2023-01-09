import React from 'react';
import Info from './components/Info';
import Main from './components/Main';
import Navbar from './components/navbar/Navbar';
import Restouran from './components/Restouran';
import Service from './components/Service';

const App = () => {
  return (
    <>
      <Navbar />    
      <Main />
      <Info />
      <Restouran />
      <Service />
    </>
  )
}

export default App