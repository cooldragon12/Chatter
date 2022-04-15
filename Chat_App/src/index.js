import App from './components/App' 
import "babel-polyfill"
import React from 'react';
import { render } from 'react-dom';
/*
    Index of React App
*/
const cont = document.getElementById("main");
render(<App />, cont)