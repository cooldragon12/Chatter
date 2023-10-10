import axios from 'axios';
import { URL } from '../config';
export const axiosPrivate = axios.create({
    /**
     * Axios private manages the request and response of authenticated user
     */
    baseURL:URL,
    timeout:6000,
    headers:{
        'Content-Type': 'application/json',
        accept:'application/json',
    }
})