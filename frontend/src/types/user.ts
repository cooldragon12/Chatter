import { IRoom } from "./room"

export interface IUser{
    id:string,
    username:string,
    status:string,
    icon:string,
   
}
export interface UserCurrentInterface{
    user:IUser,
    rooms_list: IRoom[] | []
    access_token: string
}

export  interface AuthState {
    isAuthenticated: boolean;
    userinfo: IUser | null;
    private_key: string;
    public_key: string;
}