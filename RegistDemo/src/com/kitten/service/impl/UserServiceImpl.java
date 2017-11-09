package com.kitten.service.impl;

import com.kitten.dao.UserDao;
import com.kitten.dao.impl.UserDaoMySQLImpl;
import com.kitten.domain.User;
import com.kitten.exception.UsernameExistException;
import com.kitten.service.UserService;
import com.kitten.util.MD5Util;

public class UserServiceImpl implements UserService {
	private UserDao dao = new UserDaoMySQLImpl();

	public UserServiceImpl() {
		
	}

	@Override
	public User login(String username, String password) {
		password = MD5Util.encode(password);
		return dao.findUser(username, password);
	}

	@Override
	public void regist(User user) throws UsernameExistException {
		//判断用户名是否存在
		User u = dao.findUserByUsername(user.getUsername());
		if(u!=null)
			throw new UsernameExistException("用户名已经存在了");
		//密码要加密
		user.setPassword(MD5Util.encode(user.getPassword()));
		//调用Dao保存
		dao.addUser(user);

	}

}
