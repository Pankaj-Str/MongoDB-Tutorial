# MongoDB Getting Started

To get started with MongoDB, you'll need to install it on your machine. Here are the general steps for installing MongoDB:

### Step 1: Download MongoDB

1. Go to the official MongoDB website: [MongoDB Download Center](https://www.mongodb.com/try/download/community).

2. Choose the appropriate version of MongoDB for your operating system. For example, if you're using Windows, select the Windows tab. If you're using macOS, select the macOS tab.

3. Download the installer package for your operating system.

### Step 2: Install MongoDB

#### Windows:

1. Run the downloaded installer (.msi) file.

2. Follow the installation wizard, and choose the "Complete" setup type for a standard installation.

3. MongoDB will be installed in the "C:\Program Files\MongoDB\Server\<version>" directory by default.

#### macOS:

1. Open the downloaded .dmg file.

2. Drag the MongoDB icon to the Applications folder.

#### Linux:

1. Extract the downloaded tar.gz file to a location of your choice.

```bash
tar -zxvf mongodb-linux-*-<version>.tgz
```

2. Move the extracted folder to a desired location, for example:

```bash
sudo mv mongodb-linux-*-<version> /usr/local/mongodb
```

### Step 3: Set Up MongoDB Environment

#### Windows:

1. Add the MongoDB bin directory to the system PATH:
   - Open the System Properties.
   - Click on "Environment Variables."
   - In the "System Variables" section, select the "Path" variable, then click "Edit."
   - Add a new entry for the MongoDB bin directory (e.g., C:\Program Files\MongoDB\Server\<version>\bin).

2. Create a data directory for MongoDB. The default data directory is `C:\data\db`. Create this directory or specify a different one by setting the `dbpath` in the MongoDB configuration.

#### macOS/Linux:

1. Add the MongoDB bin directory to the system PATH by adding the following line to your shell configuration file (e.g., `~/.bashrc`, `~/.bash_profile`, `~/.zshrc`):

```bash
export PATH=/usr/local/mongodb/bin:$PATH
```

2. Create a data directory for MongoDB. The default data directory is `/data/db`. Create this directory or specify a different one by setting the `dbpath` in the MongoDB configuration.

### Step 4: Start MongoDB

1. Open a terminal or command prompt.

2. Run the MongoDB server:

```bash
mongod
```

This command starts the MongoDB server. Leave the terminal or command prompt open while the server is running.

### Step 5: Connect to MongoDB

1. Open a new terminal or command prompt.

2. Run the MongoDB shell:

```bash
mongo
```

Now you can start interacting with MongoDB using the MongoDB shell.

Congratulations! You've successfully installed MongoDB on your machine and are ready to start working with it. Remember to consult the MongoDB documentation for more in-depth information and usage guides: [MongoDB Documentation](https://docs.mongodb.com/).
