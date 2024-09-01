package com.tp.spendsmart.web.dto;

import jakarta.validation.constraints.NotEmpty;
import jakarta.validation.constraints.Size;

public class UserProfileDto extends UserDto{

    @SuppressWarnings("checkstyle:MagicNumber")
    @Size(max = 50, message = "User id must not longer than 50")
    private String id;


}
