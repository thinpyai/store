package com.tp.spendsmart.web.controller;

import com.tp.spendsmart.common.util.DataConverter;
import com.tp.spendsmart.domain.model.User;
import com.tp.spendsmart.domain.service.UserService;

import com.tp.spendsmart.web.dto.UserCreateDto;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.validation.Valid;
import org.springframework.stereotype.Controller;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

@Controller
@RequestMapping("/user")
public class UserController {

    private final UserService userService;


    @GetMapping("/create")
    public ModelAndView createInitializer() {
        ModelAndView modelAndView = new ModelAndView("user/user-create");
        modelAndView.addObject("message", "Create User");
        return modelAndView;
    }

    @PostMapping("/create-confirm")
    public ModelAndView createConfirmUser(@Valid @ModelAttribute("userCreateDto") UserCreateDto userCreateDto,
                                          BindingResult bindingResult, HttpServletRequest request) {

        ModelAndView modelAndView = new ModelAndView("user/create");

        if (bindingResult.hasErrors()) {
            modelAndView.addObject("errorMessage", "User information is not enough.");
            return modelAndView;
        }

        User user = DataConverter.convert(userCreateDto, User.class);

        User existingUser = userService.getUserByUsername(user.getUsername());
        if (existingUser != null){
            modelAndView.addObject("errorMessage", "User is already created.");
            return modelAndView;
        }

        modelAndView = new ModelAndView("user/user-create-confirm");
        modelAndView.addObject("message", "Create Confirm User");
        modelAndView.addObject("userCreateDto", userCreateDto);
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