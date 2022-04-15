import * as yup from 'yup';

const LoginValidation =  yup.object({
    email:yup.string("Type your email").email('Must be valid email').required('Email is required').max(200),
    password:yup.string('Type your password').min(8, 'Password should be 8 characters and above').required('Password is required')
})

export default LoginValidation;