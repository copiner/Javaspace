package com.kitten.dao.impl;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;

import com.kitten.dao.UserDao;
import com.kitten.domain.User;
import com.kitten.exception.DaoException;
import com.kitten.util.JdbcUtil;

public class UserDaoMySQLImpl  implements UserDao {
	
	public UserDaoMySQLImpl() {
		
	}
	
	public void addUser(User user) {
		System.out.println("利用Statement保存到了数据库中");
		Connection conn = null;
		Statement stmt = null;
		try{
			conn = JdbcUtil.getConnection();
			stmt = conn.createStatement();
			String sql = "insert into users (username,nick,password,email,birthday) "
					+ " values('"+user.getUsername()+"','"+user.getNick()+"','"+user.getPassword()+"','"+user.getEmail()+"','"+user.getBirthday().toLocaleString()+"')";
			System.out.println(sql);
			stmt.executeUpdate(sql);
		}catch(Exception e){
			throw new DaoException(e);
		}finally{
			JdbcUtil.release(null, stmt, conn);
		}
	}
	
	public User findUser(String username, String password) {
		Connection conn = null;
		Statement stmt = null;
		ResultSet rs = null;
		try{
			conn = JdbcUtil.getConnection();
			stmt = conn.createStatement();
			String sql = "select * from users where username='"+username+"' and password='"+password+"'";
			System.out.println(sql);
			rs = stmt.executeQuery(sql);
			if(rs.next()){
				User user = new User();
				user.setUsername(rs.getString("username"));
				user.setNick(rs.getString("nick"));
				user.setPassword(rs.getString("password"));
				user.setEmail(rs.getString("email"));
				user.setBirthday(rs.getDate("birthday"));
				return user;
			}else
				return null;
		}catch(Exception e){
			throw new DaoException(e);
		}finally{
			JdbcUtil.release(rs, stmt, conn);
		}
	}
	

	public User findUserByUsername(String username) {
		Connection conn = null;
		Statement stmt = null;
		ResultSet rs = null;
		try{
			conn = JdbcUtil.getConnection();
			stmt = conn.createStatement();
			rs = stmt.executeQuery("select * from users where username='"+username+"'");
			if(rs.next()){
				User user = new User();
				user.setUsername(rs.getString("username"));
				user.setNick(rs.getString("nick"));
				user.setPassword(rs.getString("password"));
				user.setEmail(rs.getString("email"));
				user.setBirthday(rs.getDate("birthday"));
				return user;
			}else
				return null;
		}catch(Exception e){
			throw new DaoException(e);
		}finally{
			JdbcUtil.release(rs, stmt, conn);
		}
	}


}
