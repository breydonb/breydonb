import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { initializeApp } from "firebase/app";
import { getAuth } from 'firebase/auth';
import { AuthContextProvider } from './contexts/AuthContext';


export const firebaseConfig = initializeApp({
  apiKey: "AIzaSyBx5iO2zA3DnWx7swuU6uvJFTnUo48GztE",
  authDomain: "portfolio-breydonb.firebaseapp.com",
  projectId: "portfolio-breydonb",
  storageBucket: "portfolio-breydonb.appspot.com",
  messagingSenderId: "395264269390",
  appId: "1:395264269390:web:2d9bf8d4ddc24a6977371f",
  measurementId: "G-P821T6KLCS"
});

export const auth = getAuth(firebaseConfig);

ReactDOM.render(
    <React.StrictMode>
      <AuthContextProvider>
        <App />
      </AuthContextProvider>
    </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
