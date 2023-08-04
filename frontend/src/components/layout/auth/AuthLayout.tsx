import React from "react";
import useAuth from "../../../hooks/useCurrentUser";
import { Outlet,Navigate, useLocation } from "react-router-dom";
const AuthLayout = ()=>{
    const {auth} = useAuth();
    const location = useLocation();
    return(
        <>
            {auth?.user? <Outlet/>:<Navigate to={"/login"} state={{from: location}} replace/>}
        </>
    )
}
export default AuthLayout;