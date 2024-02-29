### IDE setup (Development)
IDE : IntelliJ IDEA
1. Setup Run Configuration.
Edit Configurations > + > Application
2. Build and run setting as follows.
- Java 17
- com.tp.spendsmart.SpendsmartApplication


### Run in local (Development)

1. Start db
Go to root directory.
Start mysql docker container
    ```
    docker-compose up -d
    ```
2. (Optional) For checking the initialized data, access to mysql db container.
    ```
    docker-compose exec db bash
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
2. Run server in local


### Temp login user
Access http://localhost:8080/api/{version}/login

Check version number at api.version in application.properties.

username : temp_user
password : my_temp_user
*Note
This is only for development purpose.
To delete temp_user in deployment.

