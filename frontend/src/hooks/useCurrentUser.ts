import { useContext } from "react";
import { AuthContext } from "../store/context/auth";
const useCurrentUser = ()=>{
    const {auth, dispatch} = useContext(AuthContext);

    const onLogout = ()=>{
        if (!auth)
            return;
        
    }

    

    if (auth === undefined || dispatch === undefined){
        throw Error("useAuth should be use inside the AuthPrivider");
    }
    return {auth, dispatch};
} 
export default useCurrentUser;