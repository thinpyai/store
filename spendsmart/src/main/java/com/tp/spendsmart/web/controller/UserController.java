package com.tp.spendsmart.web.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
@RequestMapping("/user")
public class UserController {


    @GetMapping("/create")
    public ModelAndView createInitializer() {
        ModelAndView modelAndView = new ModelAndView("user/user-create");
        modelAndView.addObject("message", "Create User");
        return modelAndView;
    }

    @PostMapping("/create-confirm")
    public ModelAndView createConfirmUser() {
        ModelAndView modelAndView = new ModelAndView("user/user-create-confirm");
        modelAndView.addObject("message", "Create Confirm User");
        return modelAndView;
    }

    @PostMapping("/create-complete")
    public ModelAndView createCompleteUser() {
        ModelAndView modelAndView = new ModelAndView("user/user-create-complete");
        modelAndView.addObject("message", "Create Complete User");
        return modelAndView;
    }

    @GetMapping("/list")
    public ModelAndView listUser() {
        ModelAndView modelAndView = new ModelAndView("user/user-list");
        modelAndView.addObject("message", "List User");
        return modelAndView;
    }
}