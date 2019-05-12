# Getting the API Token for a ThingsPro Gateway

You will require a token from the ThingsPro Gateway to be able to use the ThingsPro RESTful API. The token will be used to authenticate HTTP requests and should be included in the `mx-api-token: <token>` parameter of a HTTP request header. 
You can get the API token for a Gateway in the following two ways: 

### 1.Via the ThingsPro Gateway Web Console

1. Log in into ThingsPro Gateway or Server web console using the **root account**
2. Click on the **Token** link in the main menu.
2. In the Token page, click on the **Add Token** button.
3. Specify a **Description**, select the **Scope**, and click **SAVE**
3. Copy the token value shown at the top of screen.

> Note: The token value is displayed only once at the top of screen. Make sure you copy the token as soon as it is displayed and save it for later use before you close the page. 

### 2.Use the Token File on the ThingsPro Gateway

1. Make sure you have **root permission** on the ThingsPro Gateway computer.
2. Open the file located at `/etc/mx-api-token` and copy the token value.

> Note: The token file is automatically created on the ThingsPro Gateway during boot up if the file is not found.


