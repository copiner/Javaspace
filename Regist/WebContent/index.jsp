<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <title>HangZhou</title>
    
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    

  </head>
  
  <body>
  	<c:if test="${sessionScope.user==null}">
  		<a href="${pageContext.request.contextPath}/login.jsp">LOGIN</a>&nbsp;&nbsp;
  		<a href="${pageContext.request.contextPath}/regist.jsp">NOT A ACCOUNT</a>
  	</c:if>
  	<c:if test="${sessionScope.user!=null}">
  		Welcome : ${sessionScope.user.nick==""?sessionScope.user.username:sessionScope.user.nick}------;
  		<a href="${pageContext.request.contextPath}/CenterController?operation=logout">LOGINOUT</a>
  	</c:if>
   	<hr/>
    <h1>Welcome to HangZhou</h1>
  </body>
</html>
