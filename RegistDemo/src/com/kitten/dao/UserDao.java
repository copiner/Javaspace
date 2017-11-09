package com.kitten.dao;

import com.kitten.domain.User;

public interface UserDao {
	void addUser(User user);
	User findUserByUsername(String username);
	User findUser(String username, String password);
}
