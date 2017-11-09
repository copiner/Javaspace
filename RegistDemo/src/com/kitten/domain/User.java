package com.kitten.domain;

import java.io.Serializable;
import java.util.Date;

/*
 * create table users(
	username varchar(40) primary key,
	nick varchar(40),
	password varchar(40),
	email varchar(60),
	birthday date
	);
 * */
public class User implements Serializable {
	private String username;
	private String nick;
	private String password;
	private String email;
	private Date birthday;
	public String getUsername() {
		return username;
	}
	public void setUsername(String username) {
		this.username = username;
	}
	public String getNick() {
		return nick;
	}
	public void setNick(String nick) {
		this.nick = nick;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public Date getBirthday() {
		return birthday;
	}
	public void setBirthday(Date birthday) {
		this.birthday = birthday;
	}
	

}
