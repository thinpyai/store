package com.tp.spendsmart.web.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
@RequestMapping("/user")
public class UserController {


    @GetMapping("/create")
    public ModelAndView createInitializeUser() {
        ModelAndView modelAndView = new ModelAndView("user/user-create");
        modelAndView.addObject("message", "Hello! Welcome");
        return modelAndView;
    }
}