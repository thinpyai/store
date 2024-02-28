package com.tp.spendsmart.web.dto;

import jakarta.validation.constraints.NotEmpty;
import jakarta.validation.constraints.Size;
import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;
import org.apache.commons.lang3.builder.ToStringBuilder;

public class UserDto {

    public UserDto() {
    }

    @SuppressWarnings("checkstyle:MagicNumber")
    @Size(max = 100, message = "User name must not longer than 100")
    @NotEmpty(message = "User name must not be empty.")
    private String username;

    @Override
    public String toString() {
        return ToStringBuilder.reflectionToString(this);
    }

    @Override
    public int hashCode() {
        return HashCodeBuilder.reflectionHashCode(this);
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof UserDto)) {
            return false;
        }
        return EqualsBuilder.reflectionEquals(this, obj);
    }

}
