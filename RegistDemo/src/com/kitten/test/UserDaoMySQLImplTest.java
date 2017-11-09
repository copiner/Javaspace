package com.kitten.test;

import static org.junit.Assert.*;

import java.util.Date;

import org.junit.Test;

import com.kitten.dao.UserDao;
import com.kitten.dao.impl.UserDaoMySQLImpl;
import com.kitten.domain.User;

public class UserDaoMySQLImplTest {
	
	private UserDao dao = new UserDaoMySQLImpl();
	@Test
	public void testAddUser() {
		User user = new User();
		user.setUsername("Francis");
		user.setPassword("123");
		user.setNick("fran");
		user.setEmail("fran@kitten.cn");
		user.setBirthday(new Date());
		dao.addUser(user);
	}

	@Test
	public void testFindUser() {
		User user = dao.findUser("gfy", "123");
		assertNotNull(user);
		user = dao.findUser("gfy1", "123");
		assertNull(user);
		user = dao.findUser("gfy", "1233");
		assertNull(user);
		user = dao.findUser("gfy1", "1233");
		assertNull(user);
	}

	@Test
	public void testFindUserByUsername() {
		User user = dao.findUserByUsername("gfy");
		assertNotNull(user);
		user = dao.findUserByUsername("gfy1");
		assertNull(user);
	}

}
