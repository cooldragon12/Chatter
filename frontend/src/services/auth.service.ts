import axios from "axios";


const API_URL = "http://localhost:8080/auth/";

class AuthService{
    login(username:string, password:string){
        return axios
        .post(API_URL + "token/obtain/", {
          username,
          password
        })
        .then(response => {
          if (response.data.accessToken) {
            localStorage.setItem("user", JSON.stringify(response.data));
          }
  
          return response.data;
        });
    }
    
}