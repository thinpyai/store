package com.tp.spendsmart.domain.service;

import com.tp.spendsmart.domain.model.User;
import com.tp.spendsmart.infra.repository.UserRepository;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.security.core.userdetails.UserDetailsService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

@Service
public class UserService implements UserDetailsService {

    @Autowired
    private UserRepository userRepository;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        User user = userRepository.findByUsername(username);
        if (user == null) {
            throw new UsernameNotFoundException("User not found with username: " + username);
        }
        return org.springframework.security.core.userdetails.User
            .withUsername(user.getUsername())
            .password(user.getPassword())
            .build();
    }

    public User getUserByUsername(String username){
        User user = userRepository.findByUsername(username);
        return user;
    }

    @Cacheable(value = "userProfile", key = "#id")
    public User getUserProfile(String id){
        User user = userRepository.findById(id);
        return user;

    }

}