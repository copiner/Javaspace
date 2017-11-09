package com.kitten.service;

import com.kitten.domain.User;
import com.kitten.exception.UsernameExistException;

public interface UserService {
	// User login
	User login(String username,String password);
	// User regist
	void regist(User user) throws UsernameExistException;

}
