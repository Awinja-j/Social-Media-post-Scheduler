## Dev


## How to get access to the Twitter API

### Step one: Apply and receive approval for a developer account

In order to get started with the new Twitter API, you need an approved developer account. If you do not have one yet, you can [apply for one](https://developer.twitter.com/en/apply-for-access). Once you have an approved developer account, proceed to the next step.

### Create a Project and connect an App
Next, in the [developer portal](https://developer.twitter.com/en/portal/dashboard), create a new Project.

Give it a name, select the appropriate use-case, provide a project description. Next, you can either create a new App or connect an existing App (an App is a container for your API Keys that you need in order to make an HTTP request to the Twitter API).

Click ‘create a new App instead’ and give your App a name in order to create a new App.

### Step two: Save your App's key and tokens and keep them secure

Once you click complete, you will get your API Keys and the Bearer Token that you can then use to connect to the new endpoints in the Twitter API v2.

Click the (+) next to API Key, API Secret Key and Bearer Token and copy it in a safe place on your local machine, you will need these to make the API calls in the next step.

### Step three: Set up your access

create a .env file on the root of your application if it does not exist already. 

replace `a bearer token` in  
twitter_bearer_token= <a bearer token> with the bearer token given in step two

### Step four: Make your first request


Non-Dev

