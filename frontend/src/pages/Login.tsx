
const Login = () => {
  return (
    <div className='bg-background flex justify-center items-center w-screen h-screen'>
      <div id="login" className='shadow-md w-full lg:w-1/4 h-full lg:h-1/2 flex justify-center items-center rounded-xl' >
        <div className='flex flex-col justi'>
          {/* Title */}
          <div id="login-title">
            <h1 className='text-3xl font-semibold text-center tracking-wide'>Start the Conversation</h1>
          </div>
          {/* Form */}
          <form id="login-form" className='flex flex-col justify-center items-center gap-6  '>
            {/* Username */}
            <div id="login-username" className='flex flex-col justify-center items-center  border-2 border-primary rounded-md p-2'>
              <input type="text" placeholder="Username or Email" name="username" id="username" className='outline-none bg-transparent' />
            </div>
            {/* Password */}
            <div id="login-password" className='flex flex-col justify-center items-center  border-2 border-primary rounded-md p-2'>
              <input type="password" placeholder="Password" name="password" id="password" className='outline-none bg-transparent' />
            </div>
            {/* Submit */}
            <div id="login-submit" className='flex flex-col justify-center items-center'>
              <button type="submit"  className='bg-primary text-accent-100 px-6 py-2 rounded-md hover:bg-primary-700 transition-colors' >Login</button>
            </div>
          </form>
        </div>

      </div>
    </div>
  )
}
export default Login;