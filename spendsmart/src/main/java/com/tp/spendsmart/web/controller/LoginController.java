package com.tp.spendsmart.web.controller;

import com.tp.spendsmart.common.config.ApiProperties;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
@RequestMapping("${api.base_path}")
public class LoginController {

    @Autowired
    ApiProperties apiProperties;

    @GetMapping("/login")
    ModelAndView loginInitializer(HttpSession session) {
        ModelAndView modelAndView = new ModelAndView("login");
        session.setAttribute("apiBasePath", apiProperties.getApiBasePath());
        return modelAndView;
    }
}
