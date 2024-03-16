### IDE setup (Development)
IDE : IntelliJ IDEA
1. Setup Run Configuration.
   - Edit Configurations > + > Application
2. Build and run setting as follows.
   - Java 17
   - com.tp.spendsmart.SpendsmartApplication


### Plugins
1. Enable annotation processing 
   - Go to File -> Settings -> Build, Execution, Deployment -> Compiler -> Annotation Processors. Make sure the checkbox for "Enable annotation processing" is checked.
2. Install lombok plugin.
   - Go to File -> Settings -> Plugins, and search for "Lombok".[README.md](..%2FREADME.md)
   - "Installed" Lombok.

### Run in local (Development)

1. Start db
   - Go to root directory.
   - Start mysql docker container
    ```
    docker-compose up -d
    ```
2. (Optional) For checking the initialized data, access to mysql db container.
    ```
    docker-compose exec mysql bash
    ```

3. (Optional) Login to mysql
    ```
    mysql -u root -p
    ```
   Enter password.
   (Check MYSQL_ROOT_PASSWORD at docker-compose.yml)

4. (Optional) Check tables are created. Default user is inserted in USER table.
     ```
    SHOW DATABASES;
    USE spendsmart; 
    SHOW TABLES;
    SELECT * FROM USER;
     ```
5. Run server in local.


### Temp login user
Access http://localhost:8080/api/{version}/login

Check version number at {api.version} in application.properties.

username : temp_user
password : my_temp_user
*Note
This is only for development purpose.
To delete temp_user in deployment.

### (Optional) Redis

Frequently use commands.

1. Access the redis container.
```
docker-compose exec redis bash
```

2. Access redis cli inside the container
```
redis-cli
```

3. Set the key and value with expiration time (sec). Put the right id at <id> and display user name at <username>.

```
SET profile:<id>:username "<username>" EX 86400
```

4. Get the value by key. Put the right id at <id>.
```
GET profile:<id>:username
```

5. Delete the existing key.
```
DEL profile:<id>:username
```

6. Check after deleting.
```
EXISTS profile:<id>:username
```