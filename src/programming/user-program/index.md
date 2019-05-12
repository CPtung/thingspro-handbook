# Develop Your Own User Program to the ThingsPro Gateway

In the latest ThingsPro v2.3, we're making updates `User Program` which consists of WebUI, Bundle and Executables. Integrated various WebUI to current program which means the program is more than just executable or bundle but user interface and experience are considered as well this time. In the following parts, we're going through how to build the new user program.

## Prerequisites

#### Install Ubuntu (64-bit only)

Here we use Ubuntu 16.04 for demonstration. [Download Ubuntu]([https://www.ubuntu.com/download](https://www.ubuntu.com/download)

#### Install Docker

Refer to the web page to install Docker on Ubuntu 16.04 PC.

#### Create a user account in Ubuntu

Create a user account named `moxa` when you install Ubuntu in the first place. The default user ID and group ID should be set to 1000. If the user ID 1000 has been taken by another user in your Ubuntu, use usermod/groupmod commands to assign correct user ID and group ID to the user `moxa`.

#### Setup network environment

* Make sure PC is able to access public network.

* Make sure PC can connect to ThingsPro Gateway \(ex. UC-8112-LX, UC-8112-ME-T-LX\) via local area network.

#### Install Chrome & Postman

Install [Google Chrome browser](https://www.google.com/chrome/browser/desktop/index.html) and [Postman](https://www.getpostman.com/apps) on your PC to test the bundle created in this document.

#### Development environment

After finishing OS and Docker installation, next step is to setup alias for Docker.

On PC, login as user `moxa` and use a text editor to add following line in `/home/moxa/.bashrc`

```bash
alias mxdev="docker run --name mxdev -it -v $(pwd):/home/moxa/workspace --workdir=/home/moxa/workspace --rm -p 3000:8080 moxa/thingspro101
```

Adding the current user to the docker group:

```bash
sudo usermod -a -G docker $USER
```

Download thingspro2.0 development environment for developing your own WebUI and bundle programs. Execute the following command under command prompt:

```bash
docker pull moxa/thingspro101
```

To verify the environment you are ready to go, execute the following command under command prompt:

```
mxdev bash -c "pip freeze && node -v && npm -v"
```

> Note: If you are first time to this command, it will pull Docker image from hub.docker.com automatically. Please keep your internet access available.

![](images/web_env.png)
