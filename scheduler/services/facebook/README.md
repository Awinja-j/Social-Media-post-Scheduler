# Setup your Facebook

The Graph API is the primary way to get data into and out of the Facebook platform. It's an HTTP-based API that apps can use to programmatically query data, post new stories, manage ads, upload photos, and perform a wide variety of other tasks.

Most Graph API requests require an access token. The easiest way to get access tokens for your app is to implement Facebook Login

Step 1: 

1. Go to [link](https://developers.facebook.com/apps/), create an account there.

Step 2:

1. Enter Your Redirect URL in the App Dashboard

In the App Dashboard, choose your app and scroll to Add a Product Click Set Up in the Facebook Login card. Select Settings in the left side navigation panel and under Client OAuth Settings, enter your redirect URL in the Valid OAuth Redirect URIs field for successful authorization.

Enter this as redirect URL: 

2. Check Login Status of a Person
The first step when your webpage loads is determining if a person is already logged into your webpage with Facebook Login. A call to FB.getLoginStatus starts a call to Facebook to get the login status. Facebook then calls your callback function with the results.