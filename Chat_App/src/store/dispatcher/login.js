import { types } from "../reducer";
import useAuth from "../../hooks/useAuth";
import { axiosPrivate } from "./axios";
import API_URL from "../../helper/api-url";

export const login =  (dispatch,loginPayload)=>{
    dispatch({types:types.LOGIN_REQUEST})
    axiosPrivate
    .post(API_URL.LOGIN, loginPayload)
    .then((resp)=>{
        console.log(resp.data)
        dispatch({type: types.LOGIN_SUCCESS, payload:resp.data})
    })
    .catch((err)=>{
        dispatch({type:types.LOGIN_ERROR, payload:err})
    })

}
// export const logout = async (dispatch)=>{
//     dispatch()
    
// }