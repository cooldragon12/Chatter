import useAuth from "../../hooks/useAuth"
import { Outlet,Navigate, useLocation } from "react-router-dom";
const AuthLayout = ()=>{
    const {user} = useAuth;
    const location = useLocation();
    return(
        <>
        {user?.user? <Outlet/>:<Navigate to={"/login"} state={{from: location}} replace/>}
        </>
    )
}
export default AuthLayout;