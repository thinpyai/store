package com.tp.spendsmart.infra.repository;


import com.tp.spendsmart.common.util.DataConverter;
import com.tp.spendsmart.domain.model.User;
import com.tp.spendsmart.infra.data.UserData;
import com.tp.spendsmart.infra.mapper.UserMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public class UserRepository implements BaseRepository<User> {

    @Autowired
    UserMapper userMapper;

    @Override
    public List<User> findAll() {
        List<UserData> userDataList = this.userMapper.findAll();
        List<User> userList = DataConverter.convertList(userDataList, User.class);
        return userList;
    }

    public User findByUsername(String username){
        UserData userData = this.userMapper.findByUsername(username);
        User user = DataConverter.convert(userData, User.class);
        return user;
    }

}