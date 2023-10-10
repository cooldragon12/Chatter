import AppShellLayout from './components/layout/AppShellLayout'
import { RouterProvider, createBrowserRouter } from 'react-router-dom'
import routes from './pages'
import Login from './pages/Login.js'
import Lobby from './pages/Lobby.js'

const router = createBrowserRouter([
  {
    id:'root',
    path: '/',
    element: <AppShellLayout routes={routes}/>,
    children:[
      {
        id:'lobby',
        path: '',
        Component: Lobby,
      }
    ]
  },
  {
    id:'login',
    // action:
    path: '/login',
    Component: Login
  }
])
function App() {
  return (
    <RouterProvider router={router} fallbackElement={<p>Loading...</p>}/>
  )
}

export default App
