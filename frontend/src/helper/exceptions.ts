
export class LoginError extends Error {
    constructor(message:string) {
        super(message); // (1)
        this.name = "LoginError"; // (2)
    }
}

export class ValidationError extends Error {
    constructor(message:string) {
        super(message);
        this.name = "ValidationError"; 
    }
}

export class ConnectionError extends Error {
    constructor(message:string) {
        super(message);
        this.name = "ConnectionError"; 
    }
}