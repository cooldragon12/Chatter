import React, { createContext } from "react"



export interface IAuthContext{}

export const AuthContext = createContext<IAuthContext>({})

export const AuthProvider = ({children}:{children:React.ReactNode}) =>{
    return(
        <AuthContext.Provider value={{}}>
            {children}
        </AuthContext.Provider>
    )
}