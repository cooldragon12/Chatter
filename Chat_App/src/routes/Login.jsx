import React from 'react';
import { Typography, Box, Container, Button, TextField as GTextField } from '@mui/material';

import { Link,useNavigate, useLocation } from "react-router-dom";
import {useFormik} from 'formik';



import  LoginValidation from '../validations/schema/login';
import {login} from '../store/dispatcher'


import useAuth from '../hooks/useAuth';

const Login = ()=>{
    const {user,dispatch} = useAuth();
    const navigate = useNavigate();
    const location = useLocation();
    const from = location.state?.from?.pathname || "/";

    const formik = useFormik({
      initialValues:{
        email: "",
        password:""
      },
      validationSchema:LoginValidation,
      onSubmit: (values)=>{
          login(dispatch,values)
          console.log(values)
          
          // navigate(from, {replace:true});
          console.log(user)
      },
        
    })
    return( 
        <Container 
        sx={{
          
          alignItems: 'center',
          display: 'flex',
          flexGrow: 1,
          height: '100%',
          width:'100vw',
          flexDirection:'column',
          justifyContent:'center',
        }}
        >
        {/* <Box sx={{
            alignItems: 'center',
            display: 'flex',
            flexGrow: 1,
            minHeight: '4rem',
            minWidth: '100%'

          }}>
          <title>Login | GE Staff</title>
        </Box> */}
        <Box
          component="main"
          sx={{
            alignItems: 'center',
            justifyContent:'center',

            display: 'flex',
            flexGrow: 1,
            minHeight: '90vh',
            // minWidth: '100vw'

          }}
        >
          <Container maxWidth="sm">
            {/* <Link
              to="/"
              
            >
              <Button
                component="a"
                startIcon={<AiOutlineArrowLeft fontSize="small" />}
              >
                Dashboard
              </Button>
            </Link> */}
            <form onSubmit={formik.handleSubmit}>
              <Box sx={{ my: 3 }}>
                <Typography
                  color="textPrimary"
                  variant="h4"
                  style={{textAlign:'center'}}
                >
                  Sign in
                </Typography>
              </Box>
              <Box
                sx={{
                  pb: 1,
                  pt: 3
                }}
              >
                <Typography
                  align="center"
                  color="textSecondary"
                  variant="body1"
                >
                  login with email address
                </Typography>
              </Box>
              <GTextField
                error={Boolean(formik.touched.email && formik.errors.email)}
                fullWidth
                helperText={formik.touched.email && formik.errors.email}
                label="Email Address"
                margin="normal"
                name="email"
                onBlur={formik.handleBlur}
                onChange={formik.handleChange}
                type="email"
                value={formik.values.email}
                variant="outlined"
                color='primary'
                
              />
              <GTextField
                error={Boolean(formik.touched.password && formik.errors.password)}
                fullWidth
                helperText={formik.touched.password && formik.errors.password}
                label="Password"
                margin="normal"
                name="password"
                onBlur={formik.handleBlur}
                onChange={formik.handleChange}
                type="password"
                value={formik.values.password}
                variant="outlined"
                color='primary'
                autoComplete='true'
              />
              <Box sx={{ py: 2 }}>
                <Button
                  
                  disabled={formik.isSubmitting}
                  fullWidth
                  size="large"
                  type="submit"
                  variant="contained"
                  color="primary"
                >
                  Sign In
                </Button>
              </Box>
            </form>
          </Container>
        </Box>
      </Container>
    )
}
export default Login;