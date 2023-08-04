import AppShellLayout from './components/layout/AppShellLayout'
import { Outlet } from 'react-router-dom'
import  routes  from './pages'
function App() {


  return (
    <div className='flex'>
        <AppShellLayout routes={routes}>
          <Outlet/>
        </AppShellLayout>
      
    </div>
  )
}

export default App
