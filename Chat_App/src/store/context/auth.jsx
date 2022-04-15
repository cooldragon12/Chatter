import React,{ useEffect } from 'react';
import {createContext, useReducer} from 'react';
import { initStateLogin, authReducer } from '../reducer';

export const AuthContext = createContext();

export const AuthProvider = ({children}) =>{
    const [user, dispatch] = useReducer(authReducer, initStateLogin)
    return(
        <AuthContext.Provider value={{user, dispatch}}>
            
                {children}
            
        </AuthContext.Provider>
    )
}