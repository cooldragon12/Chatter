const DEBUG =true;
export const URLS = DEBUG? 'http://127.0.0.1:8000':'';
export {default as WebSocketProvider} from './websocket';