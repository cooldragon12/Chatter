import axios from "axios";


const API_URL = "http://localhost:8080/auth/";

class AuthService{

    async register(username:string, email:string, password:string){
        const response = await axios.post(API_URL + "register", {
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
        if (response.data.error)
          throw new Error(response.data.error);
        return response.data;
    }
    async login(username:string, password:string){
        const response = await axios.post(API_URL + "login", {
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
        return response.data;
    }
    
}
export default new AuthService();