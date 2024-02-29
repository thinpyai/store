package com.tp.spendsmart.web.controller;

import com.tp.spendsmart.common.util.DataConverter;
import com.tp.spendsmart.domain.model.User;
import com.tp.spendsmart.domain.service.UserService;

import com.tp.spendsmart.web.dto.UserCreateDto;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.MessageSource;
import org.springframework.stereotype.Controller;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.ModelAndView;

import java.util.Locale;

@Controller
@RequestMapping("${api.base_path}/user")
public class UserController {

    private final UserService userService;

    @Autowired
    private MessageSource messageSource;


    @GetMapping("/create")
    public ModelAndView createInitializer(@RequestParam(defaultValue = "en") String lang) {
        ModelAndView modelAndView = new ModelAndView("user/user-create");
        Locale locale = new Locale(lang);
        modelAndView.addObject("message", messageSource.getMessage("title.user.create", null, locale));
        return modelAndView;
    }

    @PostMapping("/create-confirm")
    public ModelAndView createConfirmUser(@RequestParam(defaultValue = "en") String lang,
                                          @Valid @ModelAttribute("userCreateDto") UserCreateDto userCreateDto,
                                          BindingResult bindingResult, HttpServletRequest request) {

        ModelAndView modelAndView = new ModelAndView("user/create");
        Locale locale = new Locale(lang);

        if (bindingResult.hasErrors()) {
            modelAndView.addObject("errorMessage", messageSource.getMessage("error.data.insufficient", null, locale));
            return modelAndView;
        }

        User user = DataConverter.convert(userCreateDto, User.class);

        User existingUser = userService.getUserByUsername(user.getUsername());
        if (existingUser != null){
            modelAndView.addObject("errorMessage", messageSource.getMessage("error.user.create.duplicate_user", null, locale));
            return modelAndView;
        }

        modelAndView = new ModelAndView("user/user-create-confirm");
        modelAndView.addObject("message", messageSource.getMessage("title.user.create_confirm", null, locale));
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