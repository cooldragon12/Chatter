import { useActionData, useLocation, useNavigation, Form } from "react-router-dom";

const Login = () => {
  let location = useLocation();
  let params = new URLSearchParams(location.search);
  let from = params.get("from") || "/";

  let navigation = useNavigation();
  let isLoggingIn = navigation.formData?.get("username") != null;

  let actionData = useActionData() as { error: string } | undefined;
  return (
    <div className='bg-background flex justify-center items-center w-screen h-screen'>
      <div id="login" className='shadow-md w-full lg:w-1/4 h-full lg:h-1/2 flex justify-center items-center rounded-xl' >
        <div className='flex flex-col gap-6'>
          {/* Title */}
          <div id="login-title">
            <h1 className='text-text text-3xl font-semibold text-center tracking-wide'>Start the Conversation</h1>
          </div>
          {/* Form */}
          <Form className='flex flex-col justify-center items-center gap-4'>
            {actionData && actionData.error ? (
              <p style={{ color: "red" }}>{actionData.error}</p>
            ) : null}

            <input type="hidden" name="redirectTo" value={from} />
            {/* Username */}
            <div id="login-username" className='text-sm flex flex-col justify-center items-center py-2 px-3 text-text border border-primary rounded-md '>
              <input type="text" placeholder="Username or Email" name="username" id="username" className='outline-none bg-transparent' />
            </div>
            {/* Password */}
            <div id="login-password" className='text-sm flex flex-col justify-center items-center py-2 px-3 text-text border border-primary rounded-md '>
              <input type="password" placeholder="Password" name="password" id="password" className='outline-none bg-transparent' />
            </div>
            {/* Submit */}
            <div id="login-submit" className='flex flex-col justify-center items-center'>
              <button type="submit" disabled={isLoggingIn} className='text-text bg-primary text-accent-100 px-6 py-2 rounded-md hover:bg-primary-700 transition-colors' >{isLoggingIn ? "Logging in..." : "Login"}</button>
            </div>

          </Form>
        </div>

      </div>
    </div>
  )
}
export default Login;