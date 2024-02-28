package com.tp.spendsmart.web.dto;

import jakarta.validation.constraints.NotEmpty;
import jakarta.validation.constraints.Size;

public class UserCreateDto extends UserDto{

//    @SuppressWarnings("checkstyle:MagicNumber")
//    @Size(max = 50, message = "User id must not longer than 50")
//    private String id;

    @SuppressWarnings("checkstyle:MagicNumber")
    @Size(max = 100, message = "Password must not longer than 100")
    @NotEmpty(message = "Password must not be empty.")
    private String password;
}
