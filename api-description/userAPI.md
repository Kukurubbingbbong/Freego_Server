# user table 관련 API 명세

## 기기 등록

```
    POST /auth/register
```

- Request

```
{
    "id" : "test",
    "pwd" : "password"
}
```

- Response

```
{
    SUCCESS { "code" : 200, "message": "register success" }
    SUCCESS id existed { "code" 400, "message": "id already existed"}
    FAIL { "code" : 400, "message" : "fail" }
}
```

## 로그인

```
    POST /auth/login
```

- Request

```
{
    "id" : "test",
    "pwd" : "password"
}

```

- Response

```
{
    SUCCESS { "code" : 200, "message": "login success" }
    SUCCESS pwd not found {"code" : 404, "message": "pwd is wrong"}
    SUCCESS id not found {"code" : 404, "message": "id not found"}
    FAIL { "code" : 400, "message" : "fail" }
}
```
