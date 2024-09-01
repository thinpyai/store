package com.tp.spendsmart.web.controller;

import com.tp.spendsmart.common.util.DataConverter;
import com.tp.spendsmart.domain.model.User;
import com.tp.spendsmart.domain.service.UserService;
import com.tp.spendsmart.web.dto.UserProfileDto;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
@RequestMapping("${api.base_path}")
public class HomeController {

    private final UserService userService;

    public HomeController(UserService userService){
        this.userService = userService;
    }

    @GetMapping({"/","/home"})
    public ModelAndView homeInitialize() {
        ModelAndView modelAndView = new ModelAndView("home");
        modelAndView.addObject("content", "balance/main");

        // set up user profile to show in top menu
        // TODO get userid
        String userId = "";
        User user = userService.getUserProfile(userId);
        UserProfileDto userProfileDto = DataConverter.convert(user, UserProfileDto.class);
        modelAndView.addObject("UserProfileDto", userProfileDto);

        return modelAndView;
    }
}
