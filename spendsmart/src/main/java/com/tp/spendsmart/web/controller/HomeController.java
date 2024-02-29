package com.tp.spendsmart.web.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
@RequestMapping("${api.base_path}")
public class HomeController {

    @GetMapping({"/","/home"})
    public ModelAndView homeInitialize() {
        ModelAndView modelAndView = new ModelAndView("home");
        return modelAndView;
    }
}
