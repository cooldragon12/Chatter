import { IMessage } from "./message";
import { IUser } from "./user";

export interface IRoom{
    search_id:string,
    name: string,
    max_users: number,
    host: number | IUser
    code: string,
    created_on:string,
    members?:number[] | IUser[] |null,
    messages?: [] | IMessage[]
}

export interface IRoomState{
    rooms:IRoom[];
    error?:{};
    loading:boolean;
}