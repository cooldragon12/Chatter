import React, { useState } from 'react';

const Register =(props)=>{
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');

    const [password, setPassword] = useState('');
    const [password2, setPassword2] = useState('');

    const usernameHandler = (e)=>{
        setUsername(e.target.value)
    }
    const emailHandler = (e:)=>{
        setEmail(e.target.value)
    }
    const passwordHandler = (e)=>{
        setPassword(e.target.value)
    }
    const password2Handler = (e)=>{
        setPassword2(e.target.value)
    }


    const registerHandler = async(e)=>{
        e.preventDefault();
        var payload = {username, password};
        try{
            let response = await register(dispatch, payload);
            if (!response.user) return
            props.history.push('/lobby');

        }catch (error){
            
        }

    }
    return(
        <Container>
            <Box component="form">
                
                <TextField id="username" label="Username" 
                    variant="outlined" 
                    value={username} 
                    onChange={usernameHandler}
                    
                />
                <TextField id="username" label="E-mail" 
                    variant="outlined" 
                    value={email} 
                    onChange={emailHandler}
                />
                <TextField  id="password" label="Password" 
                    variant="outlined" 
                    type="password" 
                    value={password} 
                    onChange={passwordHandler}
                    
                />
                <TextField  id="password" label="Confirm Password" 
                    variant="outlined" 
                    type="password" 
                    value={password2} 
                    onChange={password2Handler}

                />
                
                <LoadingButton loading={loading} variant="contained" 
                    onClick={registerHandler}
                >Sign Up</LoadingButton>
            </Box>

        </Container>    
    )
}
export default Login;