# How to get AWS IoT parameters for ThingsPro AWS IoT connection UI

## To fill up the parameters below, do the following steps:
![](./media/image1.png)

1.  Login AWS services, click AWS IoT
![](./media/image2.png)
You will see the dashboard.
![](./media/image3.png)

2.  Click **connect** and Click **Get started**.
![](./media/image4.png)

3.  Click Linux/OSX and Click Python
![](./media/image5.png)

4.  Click Get started
![](./media/image6.png)

5.  Fill in the thing name. e.g.:8112. This name will be used for
    **Client ID** and **My Thing name** of ThingsPro AWS IoT connection
    UI.
    Click next step when finishing fill the name.
![](./media/image7.png)

6.  Click Download connect kit. After finish download, click next step.
![](./media/image8.png)

7.  Click Done.
![](./media/image9.png)

8.  Unzip the downloaded connect\_device\_package.zip, you will get
    private key, certificate file …etc.
![](./media/image10.png)

9.  Download AWS root-CA file from following URL:
    [*https://www.symantec.com/content/en/us/enterprise/verisign/roots/VeriSign-Class%203-Public-Primary-Certification-Authority-G5.pem*](https://www.symantec.com/content/en/us/enterprise/verisign/roots/VeriSign-Class%203-Public-Primary-Certification-Authority-G5.pem)

10.  Copy the content, save it as **root-CA.crt** together with private
    key, certificate file. **root-CA.crt** , **private key** and
    **certificate file** will be used for ThingsPro AWS IoT connection
    UI
![](./media/image11.png)

11.  Back to your Dashborad click Registry and Things. You should see the
    “thing” you just created. Click it.
![](./media/image12.png)

12.  Click interact
![](./media/image13.png)

14.  The Endpoint is the target host of ThingsPro AWS IoT connection UI.
![](./media/image14.png)

15.  The topic is as below:
![](./media/image15.png)

Finally, you should be able to fill up all required information for
connecting to AWS IoT service.

![](./media/image16.png)
