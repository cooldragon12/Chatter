import React,{ useEffect, useState} from "react";
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'

import { AuthProvider } from '../store/context';
// import { logout } from "../store/dispatcher";
import Login from "../routes/Login";
import AuthLayout from "./auth/AuthRoute";
import GlobalStyle from "./GlobalStyle";
import ChatRoom from "../routes/ChatRoom";
const App = ()=>{
    

    // const logoutHandler = () =>{
    //     logout(dispatch);
        
    // }
    // useEffect(()=>{
    
    // })
    return(
        <AuthProvider>
            <GlobalStyle/>
            <div id="main">
                <Router>
                    {/* <Nav toLogout={logoutHandler} isAuthUser={userDetails}/> */}
                    <Routes>
                        <Route
                            path="/"
                            element={<Login/>}
                        />
                        
                            {/* <Route
                                path="/" element={<AuthLayout/>}
                            >
                                <Route path="room" element>
                                    <Route path=":roomId" element={ChatRoom}/>

                                </Route>

                            </Route>
                         */}
                        
                    </Routes>
                </Router>
            </div>
        </AuthProvider>
    )
};

export default App;