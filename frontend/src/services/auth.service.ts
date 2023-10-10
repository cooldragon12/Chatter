
import { ConnectionError, LoginError, ValidationError } from "../helper/exceptions";
import { axiosPrivate } from "./axios";


const API_URL = "http://localhost:8080/auth/";

class AuthService{
    async register(username:string, email:string, password:string){
      try{
        const response = await axiosPrivate.post(API_URL + "auth/register", {
            "username":username,
            "email":email,
            "password":password
        }, {
          withCredentials:true,
          headers:{
            "Content-Type":"application/json"
          },
          responseType:"json"
        });
        if (response.status !== 400)
          throw new ValidationError(response.data.error);
        
          return response.data;


      }catch (error){
        if (error instanceof ValidationError)
          throw error;
        else if (error instanceof ConnectionError)
          throw error;
        else
          throw new ConnectionError("Something went wrong. Please try again later.");
      }
    }
    async login(username:string, password:string){
      try{
        const response = await axiosPrivate.post(API_URL + "auth/login", {
            "username":username,
            "password":password
        }, {
          withCredentials:true,
          headers:{
            "Content-Type":"application/json"
          },
          responseType:"json"
        });
        if(response.data.isAuthenticated){
            localStorage.setItem("user", JSON.stringify(response.data));
        }
        if (response.data.error)
          throw new LoginError(response.data.error);
        
        return response.data;
        
      }catch (error){
        if (error instanceof LoginError)
          throw error;
        else if (error instanceof ConnectionError)
          throw error;
        else
          throw new ConnectionError("Something went wrong. Please try again later.");
      }
    }
    async logout(){
      try{
        const response = await axiosPrivate.post(API_URL + "auth/logout", {}, {
          withCredentials:true,
          headers:{
            "Content-Type":"application/json"
          },
          responseType:"json"
        });
        localStorage.removeItem("user");
        return response.data;
      }catch (error){
        throw new ConnectionError("Something went wrong. Please try again later.");
      }
    }
}
export default new AuthService();