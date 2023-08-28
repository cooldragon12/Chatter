
export type AuthState = {
    userinfo: {
        id: string;
        name: string;
    }
    privateCode: string;
    publicCode: string;
}