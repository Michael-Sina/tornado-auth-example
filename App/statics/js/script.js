function getCookie(name){
    var x = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return x ? x[1]:undefined;
}

$(document).ready(function(){
    $("#login").click(function(){
        var user = $("#username").val();
        var pwd = $("#password").val();
        var pd = {"username":user, "password":pwd, "_xsrf":getCookie("_xsrf")};
        $.ajax({
            type:"post",
            url:"/",
            data:pd,
            cache:false,
            success:function(data){
                window.location.href = "/login?user="+data;
            },
            error:function(){
                alert("error!");
            },
        });
    });

    $("#logout").click(function(){
        $.ajax({
            type:"get",
            url:"/logout",
            success:function(){
                window.location.href = "/";
            },
            error:function(){
                alert("error!");
            },
        });
    });


    $("#register").click(function(){
        $.ajax({
            type:"get",
            url:"/register",
            success:function(){
                window.location.href = "/register";
            },
            error:function(){
                alert("error!");
            },
        });
    });

    $("#registersubmit").click(function(){
        var user = $("#username").val();
        var pwd = $("#password").val();
        var adr = $("#mailaddress").val();
        var pd = {"username":user, "password":pwd, "mailaddress": adr, "_xsrf":getCookie("_xsrf")};
        $.ajax({
            type:"post",
            url:"/register",
            data:pd,
            cache:false,
            success:function(){
                window.location.href = "/";
            },
            error:function(){
                alert("error!");
            },
        });
    });
});



