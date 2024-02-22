package com.tp.spendsmart.infra.mapper;
import com.tp.spendsmart.infra.data.UserData;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;


@Mapper
public interface UserMapper {

    List<UserData> findAll();

    UserData findByUsername(String username);
}
