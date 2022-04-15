import { useContext } from "react";
import { AuthContext } from "../store/context/auth";
const useAuth = ()=>{
    const {user, dispatch} =useContext(AuthContext);

    if (user === undefined || dispatch === undefined){
        throw Error("useAuth should be use inside the AuthPrivider");
    }
    return {user, dispatch};
} 
export default useAuth;