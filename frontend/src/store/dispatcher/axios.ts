import axios from 'axios';
import { URLS } from '../../config';
export const axiosPrivate = axios.create({
    /**
     * Axios private manages the request and response of authenticated user
     */
    baseURL:URLS,
    timeout:6000,
    headers:{
        'Content-Type': 'application/json',
        accept:'application/json',
    }
})