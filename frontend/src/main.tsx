import React from 'react'
import ReactDOM from 'react-dom/client'
import Layout from './App.jsx'
import './index.css'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import Login from './pages/Login.js'
import Lobby from './pages/Lobby.js'


const router = createBrowserRouter([
  {
    path: '/',
    element: <Layout />,
    children:[
      {
        path: '',
        element: <Lobby/>,
      }
    ]
  },
  {
    path: '/login',
    element: <Login/>
  }
])
ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>,
)
