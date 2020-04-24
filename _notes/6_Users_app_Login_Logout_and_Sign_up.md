# 6. Users app: Login, Logout and Sign up

# 14 User Log in & Log out

- FormView to replace Django's default class LoginView

# 15 Sign Up

# 16 Verify Email

https://docs.djangoproject.com/en/3.0/topics/email/

http://mailgun.com/

# 17 Log in with Github

- Github OAuth Documentation
  https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/
- Using Github OAuth
  https://github.com/settings/developers

  - Users are redirected to request their GitHub identity
  - Users are redirected back to your site by GitHub
  - Your app accesses the API with the user's access token

- views.py is redirecting to GitHub.
  "Authorization callback URL" is where github redirects to our webpage after authentification is completed at Github

- Refer to urls.py (router) for callback url

  ```
  http://127.0.0.1:8000/users/login/github/callback
  ```

# 18 Google Log in
